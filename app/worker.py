from __future__ import annotations

import queue
import shutil
import threading
from pathlib import Path
from typing import Any, Callable

from app.db import get_job, update_job
from app.paths import job_dir
from transcribe.engine import transcribe_file
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
        # Write transcripts flat in the job folder (no nested out/)
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


WORKER = JobWorker()
