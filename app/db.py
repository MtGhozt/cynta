from __future__ import annotations

import json
import sqlite3
import threading
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
DB_PATH = DATA_DIR / "jobs.sqlite3"

_LOCK = threading.Lock()


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def connect() -> sqlite3.Connection:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    with _LOCK:
        conn = connect()
        try:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS jobs (
                    id TEXT PRIMARY KEY,
                    title TEXT NOT NULL,
                    status TEXT NOT NULL,
                    source_name TEXT,
                    source_path TEXT,
                    language TEXT,
                    model TEXT,
                    device TEXT,
                    initial_prompt TEXT,
                    error TEXT,
                    progress_json TEXT,
                    result_json TEXT,
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL
                )
                """
            )
            conn.commit()
        finally:
            conn.close()


def create_job(
    job_id: str,
    *,
    title: str,
    source_name: str,
    source_path: str,
    language: str,
    model: str,
    device: str,
    initial_prompt: str | None,
) -> dict[str, Any]:
    now = _utc_now()
    with _LOCK:
        conn = connect()
        try:
            conn.execute(
                """
                INSERT INTO jobs (
                    id, title, status, source_name, source_path, language, model, device,
                    initial_prompt, error, progress_json, result_json, created_at, updated_at
                ) VALUES (?, ?, 'queued', ?, ?, ?, ?, ?, ?, NULL, NULL, NULL, ?, ?)
                """,
                (
                    job_id,
                    title,
                    source_name,
                    source_path,
                    language,
                    model,
                    device,
                    initial_prompt,
                    now,
                    now,
                ),
            )
            conn.commit()
        finally:
            conn.close()
    return get_job(job_id)  # type: ignore[return-value]


def update_job(job_id: str, **fields: Any) -> None:
    if not fields:
        return
    fields["updated_at"] = _utc_now()
    cols = []
    vals: list[Any] = []
    for key, value in fields.items():
        if key in {"progress_json", "result_json"} and value is not None and not isinstance(value, str):
            value = json.dumps(value, ensure_ascii=False)
        cols.append(f"{key} = ?")
        vals.append(value)
    vals.append(job_id)
    with _LOCK:
        conn = connect()
        try:
            conn.execute(f"UPDATE jobs SET {', '.join(cols)} WHERE id = ?", vals)
            conn.commit()
        finally:
            conn.close()


def get_job(job_id: str) -> dict[str, Any] | None:
    with _LOCK:
        conn = connect()
        try:
            row = conn.execute("SELECT * FROM jobs WHERE id = ?", (job_id,)).fetchone()
        finally:
            conn.close()
    return _row_to_dict(row) if row else None


def list_jobs(limit: int = 100) -> list[dict[str, Any]]:
    with _LOCK:
        conn = connect()
        try:
            rows = conn.execute(
                "SELECT * FROM jobs ORDER BY created_at DESC LIMIT ?",
                (limit,),
            ).fetchall()
        finally:
            conn.close()
    return [_row_to_dict(r) for r in rows]


def _row_to_dict(row: sqlite3.Row) -> dict[str, Any]:
    data = dict(row)
    for key in ("progress_json", "result_json"):
        raw = data.get(key)
        if isinstance(raw, str) and raw:
            try:
                data[key.replace("_json", "")] = json.loads(raw)
            except json.JSONDecodeError:
                data[key.replace("_json", "")] = None
        else:
            data[key.replace("_json", "")] = None
        data.pop(key, None)
    return data
