from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DATA_DIR = ROOT / "data"
SETTINGS_PATH = DEFAULT_DATA_DIR / "settings.json"


def _read() -> dict:
    DEFAULT_DATA_DIR.mkdir(parents=True, exist_ok=True)
    if not SETTINGS_PATH.is_file():
        return {"output_dir": str(DEFAULT_DATA_DIR)}
    try:
        return json.loads(SETTINGS_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {"output_dir": str(DEFAULT_DATA_DIR)}


def _write(data: dict) -> None:
    DEFAULT_DATA_DIR.mkdir(parents=True, exist_ok=True)
    SETTINGS_PATH.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def get_output_dir() -> Path:
    raw = _read().get("output_dir") or str(DEFAULT_DATA_DIR)
    path = Path(raw).expanduser()
    if not path.is_absolute():
        path = (ROOT / path).resolve()
    path.mkdir(parents=True, exist_ok=True)
    (path / "jobs").mkdir(parents=True, exist_ok=True)
    return path


def set_output_dir(path_str: str) -> Path:
    path = Path(path_str).expanduser()
    if not path.is_absolute():
        path = (ROOT / path).resolve()
    path.mkdir(parents=True, exist_ok=True)
    (path / "jobs").mkdir(parents=True, exist_ok=True)
    data = _read()
    data["output_dir"] = str(path)
    _write(data)
    return path


def jobs_dir() -> Path:
    return get_output_dir() / "jobs"


def get_ollama_model() -> str | None:
    raw = _read().get("ollama_model")
    if raw is None:
        return None
    text = str(raw).strip()
    return text or None


def set_ollama_model(model: str | None) -> str | None:
    data = _read()
    if model is None or not str(model).strip():
        data.pop("ollama_model", None)
        _write(data)
        return None
    value = str(model).strip()
    data["ollama_model"] = value
    _write(data)
    return value
