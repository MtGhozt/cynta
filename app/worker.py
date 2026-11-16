from __future__ import annotations

import json
import queue
import shutil
import threading
from pathlib import Path
from typing import Any, Callable

from app.db import get_job, update_job
from app.paths import job_dir
from transcribe.engine import transcribe_file
from transcribe.export import merge_timelines, write_merged_artifacts
from transcribe.media import prepare_audio

EventCb = Callable[[str, dict[str, Any]], None]


class JobWorker:
    def __init__(self) -> None:
        self._q: queue.Queue[str] = queue.Queue()
        self._stop = threading.Event()
        self._thread: threading.Thread | None = None
        self._listeners: list[EventCb] = []
        self._listeners_lock = threading.Lock()
        self._cancel: set[str] = set()

    def start(self) -> None:
        if self._thread and self._thread.is_alive():
            return
        self._stop.clear()
        self._thread = threading.Thread(target=self._loop, name="transcribe-worker", daemon=True)
        self._thread.start()

    def stop(self) -> None:
        self._stop.set()
        self._q.put("__STOP__")

    def enqueue(self, job_id: str) -> None:
        self._cancel.discard(job_id)
        self._q.put(job_id)

    def cancel(self, job_id: str) -> None:
        self._cancel.add(job_id)
        update_job(job_id, status="cancelled", error="Cancelado por el usuario")
        self._emit(job_id, {"event": "cancelled"})

    def add_listener(self, cb: EventCb) -> None:
        with self._listeners_lock:
            self._listeners.append(cb)

    def remove_listener(self, cb: EventCb) -> None:
        with self._listeners_lock:
            if cb in self._listeners:
                self._listeners.remove(cb)

    def _emit(self, job_id: str, payload: dict[str, Any]) -> None:
        with self._listeners_lock:
            listeners = list(self._listeners)
        for cb in listeners:
            try:
                cb(job_id, payload)
            except Exception:  # noqa: BLE001
                pass

    def _loop(self) -> None:
        while not self._stop.is_set():
            job_id = self._q.get()
            if job_id == "__STOP__":
                break
            if job_id in self._cancel:
                continue
            try:
                self._run_job(job_id)
            except Exception as exc:  # noqa: BLE001
                update_job(job_id, status="error", error=str(exc))
                self._emit(job_id, {"event": "error", "error": str(exc)})

    def _run_job(self, job_id: str) -> None:
        job = get_job(job_id)
        if not job:
            return
        if job["status"] == "cancelled":
            return

        kind = job.get("kind") or "file"
        parts = job.get("parts")
        if kind == "class" and isinstance(parts, list) and len(parts) >= 1:
            self._run_class_job(job_id, job, parts)
            return

        self._run_file_job(job_id, job)

    def _run_file_job(self, job_id: str, job: dict[str, Any]) -> None:
        folder = job_dir(job_id)
        folder.mkdir(parents=True, exist_ok=True)
        source = Path(job["source_path"])

        update_job(job_id, status="preparing")
        self._emit(job_id, {"event": "preparing"})

        source_copy = folder / "source" / source.name
        source_copy.parent.mkdir(parents=True, exist_ok=True)
        if source.resolve() != source_copy.resolve():
            shutil.copy2(source, source_copy)

        if job_id in self._cancel:
            return

        audio_path = prepare_audio(source_copy, folder / "work")
        update_job(job_id, status="running", progress_json={"event": "audio_ready"})
        self._emit(job_id, {"event": "audio_ready", "audio": audio_path.name})

        def on_progress(payload: dict[str, Any]) -> None:
            if job_id in self._cancel:
                raise RuntimeError("Cancelado")
            update_job(job_id, progress_json=payload)
            self._emit(job_id, payload)

        lang = job.get("language") or "es"
        result = transcribe_file(
            audio_path,
            out_dir=folder,
            title=job["title"],
            language=None if lang == "auto" else lang,
            initial_prompt=job.get("initial_prompt"),
            model_size=job.get("model"),
            device=job.get("device"),
            write_subs=True,
            on_progress=on_progress,
        )

        if job_id in self._cancel:
            return

        update_job(job_id, status="done", result_json=result, progress_json={"event": "done"})
        self._emit(job_id, {"event": "done", "result": result})

    def _run_class_job(
        self,
        job_id: str,
        job: dict[str, Any],
        parts: list[dict[str, Any]],
    ) -> None:
        folder = job_dir(job_id)
        folder.mkdir(parents=True, exist_ok=True)
        part_count = len(parts)
        lang = job.get("language") or "es"
        title = job["title"]

        # Normalize mutable copy of parts state
        parts_state: list[dict[str, Any]] = [dict(p) for p in parts]

        update_job(job_id, status="preparing", parts_json=parts_state)
        self._emit(
            job_id,
            {
                "event": "preparing",
                "part_index": 0,
                "part_count": part_count,
            },
        )

        for i, part in enumerate(parts_state):
            if job_id in self._cancel:
                return

            part_dir = folder / "parts" / str(i)
            part_json = part_dir / "segmentos.json"
            part_name = str(part.get("source_name") or part.get("name") or f"part-{i}")

            if part.get("status") == "done" and part_json.is_file():
                self._emit(
                    job_id,
                    {
                        "event": "part_skip",
                        "part_index": i,
                        "part_count": part_count,
                        "part_name": part_name,
                    },
                )
                continue

            parts_state[i]["status"] = "running"
            update_job(job_id, status="running", parts_json=parts_state)
            self._emit(
                job_id,
                {
                    "event": "part_start",
                    "part_index": i,
                    "part_count": part_count,
                    "part_name": part_name,
                },
            )

            try:
                upload_path = Path(str(part["source_path"]))
                source_copy = part_dir / "source" / upload_path.name
                source_copy.parent.mkdir(parents=True, exist_ok=True)
                if upload_path.resolve() != source_copy.resolve():
                    shutil.copy2(upload_path, source_copy)

                if job_id in self._cancel:
                    return

                audio_path = prepare_audio(source_copy, part_dir / "work")
                progress_base = {
                    "part_index": i,
                    "part_count": part_count,
                    "part_name": part_name,
                }
                update_job(
                    job_id,
                    progress_json={"event": "audio_ready", **progress_base},
                )
                self._emit(job_id, {"event": "audio_ready", **progress_base, "audio": audio_path.name})

                def on_progress(payload: dict[str, Any], *, _i: int = i, _name: str = part_name) -> None:
                    if job_id in self._cancel:
                        raise RuntimeError("Cancelado")
                    enriched = {
                        **payload,
                        "part_index": _i,
                        "part_count": part_count,
                        "part_name": _name,
                    }
                    update_job(job_id, progress_json=enriched)
                    self._emit(job_id, enriched)

                # Part artifacts stay under parts/{i}/; root merge writes final MD/SRT.
                result = transcribe_file(
                    audio_path,
                    out_dir=part_dir,
                    title=f"{title} — parte {i + 1}",
                    language=None if lang == "auto" else lang,
                    initial_prompt=job.get("initial_prompt"),
                    model_size=job.get("model"),
                    device=job.get("device"),
                    write_subs=False,
                    on_progress=on_progress,
                )

                if job_id in self._cancel:
                    return

                duration = result.get("duration_sec")
                parts_state[i]["status"] = "done"
                parts_state[i]["duration_sec"] = duration
                parts_state[i]["error"] = None
                update_job(job_id, parts_json=parts_state)
                self._emit(
                    job_id,
                    {
                        "event": "part_done",
                        "part_index": i,
                        "part_count": part_count,
                        "part_name": part_name,
                        "duration_sec": duration,
                    },
                )
            except Exception as exc:  # noqa: BLE001
                parts_state[i]["status"] = "error"
                parts_state[i]["error"] = str(exc)
                update_job(
                    job_id,
                    status="error",
                    error=f"Parte {i + 1}/{part_count} ({part_name}): {exc}",
                    parts_json=parts_state,
                )
                self._emit(
                    job_id,
                    {
                        "event": "error",
                        "error": str(exc),
                        "part_index": i,
                        "part_count": part_count,
                        "part_name": part_name,
                    },
                )
                return

        if job_id in self._cancel:
            return

        # Merge all part JSON into root artifacts
        part_payloads: list[dict[str, Any]] = []
        for i in range(part_count):
            part_json = folder / "parts" / str(i) / "segmentos.json"
            if not part_json.is_file():
                raise RuntimeError(f"Falta segmentos.json de la parte {i}")
            payload = json.loads(part_json.read_text(encoding="utf-8"))
            # Prefer measured duration from parts_state
            dur = parts_state[i].get("duration_sec")
            if dur is not None:
                payload["duration_sec"] = dur
            part_payloads.append(payload)

        merged = merge_timelines(
            part_payloads,
            clase=title,
            model=job.get("model"),
            language=None if lang == "auto" else lang,
        )
        paths = write_merged_artifacts(folder, merged, write_subs=True, clean=False)

        total_segments = len(merged.get("segments") or [])
        result = {
            "title": title,
            "kind": "class",
            "parts": part_count,
            "model": merged.get("model") or job.get("model"),
            "device": job.get("device"),
            "language": job.get("language"),
            "segments": total_segments,
            "duration_sec": merged.get("duration_sec"),
            "paths": {k: str(v) for k, v in paths.items()},
        }
        update_job(
            job_id,
            status="done",
            result_json=result,
            parts_json=parts_state,
            progress_json={"event": "done", "part_count": part_count},
        )
        self._emit(job_id, {"event": "done", "result": result})


WORKER = JobWorker()
