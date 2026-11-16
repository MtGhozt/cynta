from __future__ import annotations

import asyncio
import json
import os
import subprocess
import sys
import uuid
from pathlib import Path
from typing import Any

from fastapi import FastAPI, File, Form, HTTPException, UploadFile, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.db import create_job, delete_jobs, get_job, init_db, list_jobs, update_job
from app.envcheck import collect_health
from app.paths import artifact_dir, artifact_path, job_dir, openable_folder
from app.prompts import PROMPT_TEMPLATES
from app.settings import get_ollama_model, get_output_dir, set_ollama_model, set_output_dir
from app.worker import WORKER
from transcribe import config
from transcribe.export import rewrite_job_artifacts
from transcribe.media import AUDIO_EXTENSIONS, VIDEO_EXTENSIONS
from transcribe.study import DEFAULT_OLLAMA_URL, generate_study

STATIC_DIR = Path(__file__).resolve().parent / "static"

app = FastAPI(title="Cynta", version="0.4.0")
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


class OutputDirBody(BaseModel):
    path: str


class OllamaModelBody(BaseModel):
    model: str | None = None


class SegmentItem(BaseModel):
    start: float
    end: float
    text: str = ""


class SegmentsBody(BaseModel):
    segments: list[SegmentItem] = Field(default_factory=list)


class StudyBody(BaseModel):
    force: bool = True
    use_ollama: bool = True


@app.on_event("startup")
def _startup() -> None:
    init_db()
    get_output_dir()
    WORKER.start()


@app.on_event("shutdown")
def _shutdown() -> None:
    WORKER.stop()


@app.get("/", response_class=HTMLResponse)
def index() -> HTMLResponse:
    return HTMLResponse(
        (STATIC_DIR / "index.html").read_text(encoding="utf-8"),
        headers={"Cache-Control": "no-store, max-age=0"},
    )


@app.get("/api/health")
def health() -> dict[str, Any]:
    out = get_output_dir()
    info = collect_health()
    return {
        **info,
        "output_dir": str(out),
        "jobs_dir": str(out / "jobs"),
    }


@app.get("/api/settings")
def api_get_settings() -> dict[str, Any]:
    out = get_output_dir()
    return {
        "output_dir": str(out),
        "jobs_dir": str(out / "jobs"),
        "ollama_model": get_ollama_model(),
    }


@app.post("/api/settings/output-dir")
def api_set_output_dir(body: OutputDirBody) -> dict[str, Any]:
    path = body.path.strip()
    if not path:
        raise HTTPException(400, "Path vacío")
    out = set_output_dir(path)
    return {"output_dir": str(out), "jobs_dir": str(out / "jobs")}


@app.post("/api/settings/ollama-model")
def api_set_ollama_model(body: OllamaModelBody) -> dict[str, Any]:
    model = set_ollama_model(body.model)
    return {"ollama_model": model}


def _allow_foreground() -> None:
    """Best-effort: let the picker process steal focus after a browser click."""
    if sys.platform != "win32":
        return
    try:
        import ctypes

        # ASFW_ANY = -1
        ctypes.windll.user32.AllowSetForegroundWindow(-1)
    except Exception:  # noqa: BLE001
        pass


def _pick_folder_native(initial: str) -> str | None:
    """Folder picker in a separate process (safe under uvicorn worker threads)."""
    if sys.platform == "win32":
        _allow_foreground()
        script = Path(__file__).resolve().parent / "pick_folder.ps1"
        proc = subprocess.run(
            [
                "powershell",
                "-NoProfile",
                "-STA",
                "-ExecutionPolicy",
                "Bypass",
                "-File",
                str(script),
                "-Initial",
                initial,
            ],
            capture_output=True,
            text=True,
            check=False,
            timeout=300,
        )
        if proc.returncode == 2:
            return None  # cancelled
        path = (proc.stdout or "").strip()
        return path or None

    code = (
        "import tkinter as tk\n"
        "from tkinter import filedialog\n"
        "root = tk.Tk(); root.withdraw()\n"
        f"p = filedialog.askdirectory(initialdir={initial!r})\n"
        "print(p or '', end='')\n"
    )
    proc = subprocess.run(
        [sys.executable, "-c", code],
        capture_output=True,
        text=True,
        check=False,
        timeout=300,
    )
    chosen = (proc.stdout or "").strip()
    return chosen or None


@app.post("/api/settings/pick-output-dir")
def api_pick_output_dir() -> dict[str, Any]:
    """Native folder picker (local app only). Cancel returns cancelled=true (not an error)."""
    initial = str(get_output_dir())
    try:
        chosen = _pick_folder_native(initial)
    except subprocess.TimeoutExpired as exc:
        raise HTTPException(504, "Se agotó el tiempo del diálogo de carpeta") from exc
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(500, f"No se pudo abrir el selector: {exc}") from exc

    if not chosen:
        return {
            "cancelled": True,
            "output_dir": str(get_output_dir()),
            "jobs_dir": str(get_output_dir() / "jobs"),
        }
    out = set_output_dir(chosen)
    return {"cancelled": False, "output_dir": str(out), "jobs_dir": str(out / "jobs")}


@app.get("/api/meta")
def meta() -> dict[str, Any]:
    return {
        "models": ["large-v3", "medium", "small", "base", "tiny"],
        "devices": ["cuda", "cpu", "auto"],
        "languages": ["es", "en", "auto"],
        "audio_extensions": sorted(AUDIO_EXTENSIONS),
        "video_extensions": sorted(VIDEO_EXTENSIONS),
        "prompt_templates": {
            key: {"label": val["label"]} for key, val in PROMPT_TEMPLATES.items()
        },
        "defaults": {
            "model": config.DEFAULT_MODEL,
            "device": config.DEFAULT_DEVICE,
            "language": config.DEFAULT_LANGUAGE,
            "prompt_template": "lenguajes",
        },
    }


@app.get("/api/jobs")
def api_list_jobs() -> list[dict[str, Any]]:
    return list_jobs()


@app.get("/api/jobs/{job_id}")
def api_get_job(job_id: str) -> dict[str, Any]:
    job = get_job(job_id)
    if not job:
        raise HTTPException(404, "Job no encontrado")
    return job


async def _save_upload(upload: UploadFile, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    with dest.open("wb") as out:
        while True:
            chunk = await upload.read(1024 * 1024)
            if not chunk:
                break
            out.write(chunk)


def _validate_media_name(filename: str | None) -> str:
    if not filename:
        raise HTTPException(400, "Falta nombre de archivo")
    suffix = Path(filename).suffix.lower()
    if suffix not in AUDIO_EXTENSIONS | VIDEO_EXTENSIONS:
        raise HTTPException(
            400,
            f"Formato no soportado: {suffix}. "
            f"Audio {sorted(AUDIO_EXTENSIONS)} / Video {sorted(VIDEO_EXTENSIONS)}",
        )
    return filename


def _resolve_prompt(prompt_template: str, custom_prompt: str | None) -> str | None:
    if prompt_template == "custom":
        return (custom_prompt or "").strip() or None
    tmpl = PROMPT_TEMPLATES.get(prompt_template) or PROMPT_TEMPLATES["general"]
    return tmpl["prompt"].strip() or None


@app.post("/api/jobs")
async def api_create_job(
    files: list[UploadFile] | None = File(None),
    file: UploadFile | None = File(None),
    title: str | None = Form(None),
    language: str = Form("es"),
    model: str = Form(config.DEFAULT_MODEL),
    device: str = Form(config.DEFAULT_DEVICE),
    prompt_template: str = Form("lenguajes"),
    custom_prompt: str | None = Form(None),
) -> dict[str, Any]:
    uploads: list[UploadFile] = []
    if files:
        uploads.extend(files)
    if file is not None:
        uploads.append(file)
    # Deduplicate if client sent both (same object unlikely); keep order
    if not uploads:
        raise HTTPException(400, "Falta archivo (file o files)")

    for upload in uploads:
        _validate_media_name(upload.filename)

    prompt = _resolve_prompt(prompt_template, custom_prompt)
    job_id = uuid.uuid4().hex[:12]
    folder = job_dir(job_id)

    if len(uploads) == 1:
        upload = uploads[0]
        assert upload.filename
        dest = folder / "upload" / Path(upload.filename).name
        await _save_upload(upload, dest)
        job_title = (title or Path(upload.filename).stem).strip() or job_id
        job = create_job(
            job_id,
            title=job_title,
            source_name=upload.filename,
            source_path=str(dest),
            language=language,
            model=model,
            device=device,
            initial_prompt=prompt,
            kind="file",
        )
    else:
        parts: list[dict[str, Any]] = []
        names: list[str] = []
        for index, upload in enumerate(uploads):
            assert upload.filename
            dest = folder / "parts" / str(index) / "upload" / Path(upload.filename).name
            await _save_upload(upload, dest)
            names.append(upload.filename)
            parts.append(
                {
                    "index": index,
                    "source_name": upload.filename,
                    "source_path": str(dest),
                    "status": "queued",
                }
            )
        job_title = (title or Path(names[0]).stem).strip() or job_id
        source_label = " + ".join(names)
        job = create_job(
            job_id,
            title=job_title,
            source_name=source_label,
            source_path=str(folder / "parts"),
            language=language,
            model=model,
            device=device,
            initial_prompt=prompt,
            kind="class",
            parts=parts,
        )

    WORKER.enqueue(job_id)
    return job


@app.post("/api/jobs/clear")
def api_clear_jobs() -> dict[str, Any]:
    """Remove finished jobs from the queue (keeps ones still running)."""
    removed = delete_jobs(statuses=["done", "error", "cancelled"], delete_files=True)
    return {"removed": removed}


@app.post("/api/jobs/{job_id}/cancel")
def api_cancel(job_id: str) -> dict[str, str]:
    if not get_job(job_id):
        raise HTTPException(404, "Job no encontrado")
    WORKER.cancel(job_id)
    return {"status": "cancelled"}


@app.post("/api/jobs/{job_id}/retry")
def api_retry(job_id: str) -> dict[str, Any]:
    job = get_job(job_id)
    if not job:
        raise HTTPException(404, "Job no encontrado")
    if job["status"] not in {"error", "cancelled", "done"}:
        raise HTTPException(400, "Solo se puede reintentar jobs terminados/error/cancelados")

    fields: dict[str, Any] = {
        "status": "queued",
        "error": None,
        "progress_json": None,
        "result_json": None,
    }
    if job.get("kind") == "class" and isinstance(job.get("parts"), list):
        # Keep done parts (and their on-disk JSON); reset the rest for fail-fast resume.
        reset_parts: list[dict[str, Any]] = []
        for part in job["parts"]:
            p = dict(part)
            if p.get("status") == "done":
                reset_parts.append(p)
            else:
                p["status"] = "queued"
                p["error"] = None
                reset_parts.append(p)
        fields["parts_json"] = reset_parts

    update_job(job_id, **fields)
    WORKER.enqueue(job_id)
    return get_job(job_id)  # type: ignore[return-value]


@app.get("/api/jobs/{job_id}/files/{kind}")
def api_download(job_id: str, kind: str) -> FileResponse:
    mapping = {
        "md": "transcripcion.md",
        "json": "segmentos.json",
        "srt": "subtitulos.srt",
        "outline": "outline.json",
        "outline_md": "outline.md",
        "opencards": "open-cards.json",
    }
    if kind not in mapping:
        raise HTTPException(
            400, "kind debe ser md|json|srt|outline|outline_md|opencards"
        )
    path = artifact_path(job_id, mapping[kind])
    if not path:
        raise HTTPException(404, "Archivo no listo")
    media = {
        "md": "text/markdown; charset=utf-8",
        "json": "application/json",
        "srt": "application/x-subrip",
        "outline": "application/json",
        "outline_md": "text/markdown; charset=utf-8",
        "opencards": "application/json",
    }[kind]
    return FileResponse(path, media_type=media, filename=f"{job_id}-{mapping[kind]}")


@app.post("/api/jobs/{job_id}/study")
def api_generate_study(job_id: str, body: StudyBody | None = None) -> dict[str, Any]:
    opts = body or StudyBody()
    job = get_job(job_id)
    if not job:
        raise HTTPException(404, "Job no encontrado")
    if job["status"] != "done":
        raise HTTPException(400, "Solo se puede generar estudio en jobs done")

    segmentos = artifact_path(job_id, "segmentos.json")
    if not segmentos:
        raise HTTPException(404, "Falta segmentos.json")

    out_dir = artifact_dir(job_id) or job_dir(job_id)
    outline_existing = artifact_path(job_id, "outline.json")
    cards_existing = artifact_path(job_id, "open-cards.json")
    if not opts.force and outline_existing and cards_existing:
        return api_get_study(job_id)

    try:
        result = generate_study(
            segmentos,
            out_dir,
            title=job.get("title"),
            ollama_url=DEFAULT_OLLAMA_URL,
            model=get_ollama_model(),
            use_ollama=opts.use_ollama,
        )
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(500, f"No se pudo generar estudio: {exc}") from exc

    return {
        "ok": True,
        "mode": result.get("mode"),
        "outline": result.get("outline"),
        "deck": result.get("deck"),
        "ollama": result.get("ollama"),
        "paths": result.get("paths"),
    }


@app.get("/api/jobs/{job_id}/study")
def api_get_study(job_id: str) -> dict[str, Any]:
    if not get_job(job_id):
        raise HTTPException(404, "Job no encontrado")
    outline_path = artifact_path(job_id, "outline.json")
    cards_path = artifact_path(job_id, "open-cards.json")
    if not outline_path or not cards_path:
        raise HTTPException(404, "Estudio no generado aún")

    try:
        outline = json.loads(outline_path.read_text(encoding="utf-8"))
        library = json.loads(cards_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        raise HTTPException(500, f"No se pudo leer estudio: {exc}") from exc

    decks = library.get("decks") if isinstance(library, dict) else None
    deck = decks[0] if isinstance(decks, list) and decks else {}
    cards = deck.get("cards") if isinstance(deck, dict) else []
    preview_cards: list[dict[str, str]] = []
    if isinstance(cards, list):
        for card in cards:
            if not isinstance(card, dict):
                continue
            front_blocks = card.get("front") or []
            back_blocks = card.get("back") or []
            front = ""
            back = ""
            if isinstance(front_blocks, list) and front_blocks:
                front = str((front_blocks[0] or {}).get("content") or "")
            if isinstance(back_blocks, list) and back_blocks:
                back = str((back_blocks[0] or {}).get("content") or "")
            preview_cards.append({"front": front, "back": back})

    return {
        "mode": outline.get("mode"),
        "outline": outline,
        "deck": {
            "name": deck.get("name") if isinstance(deck, dict) else None,
            "tags": (deck.get("tags") if isinstance(deck, dict) else None) or [],
            "cards_count": len(preview_cards),
            "cards": preview_cards,
        },
        "ollama": outline.get("ollama"),
    }


@app.get("/api/jobs/{job_id}/transcript")
def api_transcript(job_id: str) -> dict[str, str]:
    path = artifact_path(job_id, "transcripcion.md")
    if not path:
        raise HTTPException(404, "Transcripción no lista")
    return {"markdown": path.read_text(encoding="utf-8")}


@app.get("/api/jobs/{job_id}/segments")
def api_get_segments(job_id: str) -> dict[str, Any]:
    path = artifact_path(job_id, "segmentos.json")
    if not path:
        raise HTTPException(404, "Segmentos no listos")
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        raise HTTPException(500, f"No se pudo leer segmentos: {exc}") from exc
    segments = data.get("segments") or []
    if not isinstance(segments, list):
        raise HTTPException(500, "segmentos.json inválido")
    return {
        "clase": data.get("clase"),
        "curso": data.get("curso"),
        "temas": data.get("temas") or [],
        "source": data.get("source"),
        "model": data.get("model"),
        "language": data.get("language"),
        "duration_sec": data.get("duration_sec"),
        "parts": data.get("parts") if isinstance(data.get("parts"), list) else None,
        "segments": segments,
    }


@app.put("/api/jobs/{job_id}/segments")
def api_put_segments(job_id: str, body: SegmentsBody) -> dict[str, Any]:
    if not get_job(job_id):
        raise HTTPException(404, "Job no encontrado")
    out_dir = artifact_dir(job_id)
    if not out_dir:
        raise HTTPException(404, "Segmentos no listos")

    normalized: list[dict[str, Any]] = []
    for i, seg in enumerate(body.segments):
        if seg.end < seg.start:
            raise HTTPException(400, f"Segmento {i}: end < start")
        normalized.append(
            {
                "start": float(seg.start),
                "end": float(seg.end),
                "text": str(seg.text),
            }
        )

    json_path = out_dir / "segmentos.json"
    md_path = out_dir / "transcripcion.md"
    srt_path = out_dir / "subtitulos.srt"
    try:
        rewrite_job_artifacts(json_path, md_path, srt_path, normalized)
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(500, f"No se pudo guardar: {exc}") from exc

    return {
        "ok": True,
        "segments_count": len(normalized),
        "regenerated": ["md", "json", "srt"],
    }


@app.post("/api/jobs/{job_id}/open-folder")
def api_open_folder(job_id: str) -> dict[str, str]:
    folder = openable_folder(job_id)
    if not folder.is_dir():
        raise HTTPException(404, "Carpeta no existe")
    if sys.platform == "win32":
        os.startfile(folder)  # type: ignore[attr-defined]
    elif sys.platform == "darwin":
        subprocess.Popen(["open", str(folder)])
    else:
        subprocess.Popen(["xdg-open", str(folder)])
    return {"opened": str(folder)}


@app.websocket("/ws/jobs/{job_id}")
async def ws_job(websocket: WebSocket, job_id: str) -> None:
    await websocket.accept()
    loop = asyncio.get_running_loop()
    q: asyncio.Queue[dict[str, Any]] = asyncio.Queue()

    def listener(jid: str, payload: dict[str, Any]) -> None:
        if jid != job_id:
            return
        loop.call_soon_threadsafe(q.put_nowait, payload)

    WORKER.add_listener(listener)
    try:
        job = get_job(job_id)
        if job:
            await websocket.send_json({"event": "snapshot", "job": job})
        while True:
            try:
                payload = await asyncio.wait_for(q.get(), timeout=15.0)
                await websocket.send_json(payload)
                if payload.get("event") in {"done", "error", "cancelled"}:
                    break
            except asyncio.TimeoutError:
                job = get_job(job_id)
                await websocket.send_json({"event": "ping", "job": job})
                if job and job["status"] in {"done", "error", "cancelled"}:
                    break
    except WebSocketDisconnect:
        pass
    finally:
        WORKER.remove_listener(listener)
