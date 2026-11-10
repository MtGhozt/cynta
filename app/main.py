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

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.db import DATA_DIR, create_job, get_job, init_db, list_jobs, update_job
from app.prompts import PROMPT_TEMPLATES
from app.worker import WORKER
from transcribe import config
from transcribe.media import AUDIO_EXTENSIONS, VIDEO_EXTENSIONS

STATIC_DIR = Path(__file__).resolve().parent / "static"

app = FastAPI(title="Transcriptor Local", version="0.1.0")
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.on_event("startup")
def _startup() -> None:
    init_db()
    WORKER.start()


@app.on_event("shutdown")
def _shutdown() -> None:
    WORKER.stop()


@app.get("/", response_class=HTMLResponse)
def index() -> HTMLResponse:
    return HTMLResponse((STATIC_DIR / "index.html").read_text(encoding="utf-8"))


@app.get("/api/health")
def health() -> dict[str, Any]:
    return {"ok": True, "data_dir": str(DATA_DIR)}


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
    job_dir = DATA_DIR / "jobs" / job_id
    upload_dir = job_dir / "upload"
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
    path = DATA_DIR / "jobs" / job_id / "out" / mapping[kind]
    if not path.is_file():
        raise HTTPException(404, "Archivo no listo")
    media = {
        "md": "text/markdown; charset=utf-8",
        "json": "application/json",
        "srt": "application/x-subrip",
    }[kind]
    return FileResponse(path, media_type=media, filename=f"{job_id}-{mapping[kind]}")


@app.get("/api/jobs/{job_id}/transcript")
def api_transcript(job_id: str) -> dict[str, str]:
    path = DATA_DIR / "jobs" / job_id / "out" / "transcripcion.md"
    if not path.is_file():
        raise HTTPException(404, "Transcripción no lista")
    return {"markdown": path.read_text(encoding="utf-8")}


@app.post("/api/jobs/{job_id}/open-folder")
def api_open_folder(job_id: str) -> dict[str, str]:
    folder = DATA_DIR / "jobs" / job_id
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
                # keepalive + refresh snapshot
                job = get_job(job_id)
                await websocket.send_json({"event": "ping", "job": job})
                if job and job["status"] in {"done", "error", "cancelled"}:
                    break
    except WebSocketDisconnect:
        pass
    finally:
        WORKER.remove_listener(listener)
