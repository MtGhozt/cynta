from __future__ import annotations

import asyncio
import os
import subprocess
import sys
import uuid
from pathlib import Path
from typing import Any

from fastapi import FastAPI, File, Form, HTTPException, UploadFile, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.db import create_job, delete_jobs, get_job, init_db, list_jobs, update_job
from app.paths import artifact_path, job_dir, openable_folder
from app.prompts import PROMPT_TEMPLATES
from app.settings import get_output_dir, set_output_dir
from app.worker import WORKER
from transcribe import config
from transcribe.media import AUDIO_EXTENSIONS, VIDEO_EXTENSIONS

STATIC_DIR = Path(__file__).resolve().parent / "static"

app = FastAPI(title="Cynta", version="0.2.0")
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


class OutputDirBody(BaseModel):
    path: str


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
    return HTMLResponse((STATIC_DIR / "index.html").read_text(encoding="utf-8"))


@app.get("/api/health")
def health() -> dict[str, Any]:
    out = get_output_dir()
    return {
        "ok": True,
        "output_dir": str(out),
        "jobs_dir": str(out / "jobs"),
    }


@app.get("/api/settings")
def api_get_settings() -> dict[str, Any]:
    out = get_output_dir()
    return {"output_dir": str(out), "jobs_dir": str(out / "jobs")}


@app.post("/api/settings/output-dir")
def api_set_output_dir(body: OutputDirBody) -> dict[str, Any]:
    path = body.path.strip()
    if not path:
        raise HTTPException(400, "Path vacío")
    out = set_output_dir(path)
    return {"output_dir": str(out), "jobs_dir": str(out / "jobs")}


@app.post("/api/settings/pick-output-dir")
def api_pick_output_dir() -> dict[str, Any]:
    """Native folder picker (local app only)."""
    try:
        import tkinter as tk
        from tkinter import filedialog
    except ImportError as exc:
        raise HTTPException(500, "tkinter no disponible para elegir carpeta") from exc

    root = tk.Tk()
    root.withdraw()
    try:
        root.attributes("-topmost", True)
    except tk.TclError:
        pass
    initial = str(get_output_dir())
    chosen = filedialog.askdirectory(title="Carpeta de salida de Cynta", initialdir=initial)
    root.destroy()
    if not chosen:
        raise HTTPException(400, "Selección cancelada")
    out = set_output_dir(chosen)
    return {"output_dir": str(out), "jobs_dir": str(out / "jobs")}


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


@app.post("/api/jobs")
async def api_create_job(
    file: UploadFile = File(...),
    title: str | None = Form(None),
    language: str = Form("es"),
    model: str = Form(config.DEFAULT_MODEL),
    device: str = Form(config.DEFAULT_DEVICE),
    prompt_template: str = Form("lenguajes"),
    custom_prompt: str | None = Form(None),
) -> dict[str, Any]:
    if not file.filename:
        raise HTTPException(400, "Falta nombre de archivo")

    suffix = Path(file.filename).suffix.lower()
    if suffix not in AUDIO_EXTENSIONS | VIDEO_EXTENSIONS:
        raise HTTPException(
            400,
            f"Formato no soportado: {suffix}. "
            f"Audio {sorted(AUDIO_EXTENSIONS)} / Video {sorted(VIDEO_EXTENSIONS)}",
        )

    job_id = uuid.uuid4().hex[:12]
    folder = job_dir(job_id)
    upload_dir = folder / "upload"
    upload_dir.mkdir(parents=True, exist_ok=True)
    dest = upload_dir / Path(file.filename).name

    with dest.open("wb") as out:
        while True:
            chunk = await file.read(1024 * 1024)
            if not chunk:
                break
            out.write(chunk)

    if prompt_template == "custom":
        prompt = (custom_prompt or "").strip() or None
    else:
        tmpl = PROMPT_TEMPLATES.get(prompt_template) or PROMPT_TEMPLATES["general"]
        prompt = tmpl["prompt"].strip() or None

    job_title = (title or Path(file.filename).stem).strip() or job_id
    job = create_job(
        job_id,
        title=job_title,
        source_name=file.filename,
        source_path=str(dest),
        language=language,
        model=model,
        device=device,
        initial_prompt=prompt,
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
    update_job(job_id, status="queued", error=None, progress_json=None, result_json=None)
    WORKER.enqueue(job_id)
    return get_job(job_id)  # type: ignore[return-value]


@app.get("/api/jobs/{job_id}/files/{kind}")
def api_download(job_id: str, kind: str) -> FileResponse:
    mapping = {
        "md": "transcripcion.md",
        "json": "segmentos.json",
        "srt": "subtitulos.srt",
    }
    if kind not in mapping:
        raise HTTPException(400, "kind debe ser md|json|srt")
    path = artifact_path(job_id, mapping[kind])
    if not path:
        raise HTTPException(404, "Archivo no listo")
    media = {
        "md": "text/markdown; charset=utf-8",
        "json": "application/json",
        "srt": "application/x-subrip",
    }[kind]
    return FileResponse(path, media_type=media, filename=f"{job_id}-{mapping[kind]}")


@app.get("/api/jobs/{job_id}/transcript")
def api_transcript(job_id: str) -> dict[str, str]:
    path = artifact_path(job_id, "transcripcion.md")
    if not path:
        raise HTTPException(404, "Transcripción no lista")
    return {"markdown": path.read_text(encoding="utf-8")}


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
