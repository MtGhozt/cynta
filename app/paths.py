from __future__ import annotations

from pathlib import Path

from app.settings import jobs_dir


def job_dir(job_id: str) -> Path:
    return jobs_dir() / job_id


def artifact_path(job_id: str, filename: str) -> Path | None:
    """Prefer flat job folder; fall back to legacy out/."""
    base = job_dir(job_id)
    flat = base / filename
    if flat.is_file():
        return flat
    legacy = base / "out" / filename
    if legacy.is_file():
        return legacy
    return None


def artifact_dir(job_id: str) -> Path | None:
    """Directory that already holds transcript artifacts (flat or legacy out/)."""
    json_path = artifact_path(job_id, "segmentos.json")
    if json_path:
        return json_path.parent
    return None


def openable_folder(job_id: str) -> Path:
    """Folder that already shows transcript files when possible."""
    base = job_dir(job_id)
    if (base / "transcripcion.md").is_file():
        return base
    out = base / "out"
    if out.is_dir() and any(out.iterdir()):
        return out
    return base
