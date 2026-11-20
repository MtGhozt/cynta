from __future__ import annotations

import shutil
import subprocess
import sys
from typing import Any


def _ffmpeg() -> dict[str, Any]:
    path = shutil.which("ffmpeg")
    if not path:
        return {"ok": False, "path": None, "version": None}
    version = None
    try:
        proc = subprocess.run(
            [path, "-version"],
            capture_output=True,
            text=True,
            check=False,
            timeout=8,
        )
        first = (proc.stdout or "").splitlines()[:1]
        version = first[0] if first else None
    except Exception:  # noqa: BLE001
        pass
    return {"ok": True, "path": path, "version": version}


def _nvidia_smi() -> dict[str, Any]:
    smi = shutil.which("nvidia-smi")
    if not smi:
        return {"ok": False, "name": None, "driver": None}
    try:
        proc = subprocess.run(
            [smi, "--query-gpu=name,driver_version", "--format=csv,noheader"],
            capture_output=True,
            text=True,
            check=False,
            timeout=8,
        )
        line = (proc.stdout or "").strip().splitlines()[:1]
        if not line:
            return {"ok": False, "name": None, "driver": None}
        parts = [p.strip() for p in line[0].split(",")]
        name = parts[0] if parts else None
        driver = parts[1] if len(parts) > 1 else None
        return {"ok": True, "name": name, "driver": driver}
    except Exception:  # noqa: BLE001
        return {"ok": False, "name": None, "driver": None}


def _cublas_wheels() -> bool:
    try:
        import nvidia  # type: ignore  # noqa: F401
        from pathlib import Path

        root = Path(nvidia.__path__[0])
        return (root / "cublas" / "bin").is_dir()
    except Exception:  # noqa: BLE001
        return False


def _cuda_runtime_probe() -> dict[str, Any]:
    """Cheap probe: GPU visible + cublas wheels present (not a full Whisper load)."""
    from transcribe.cuda_path import ensure_cuda_dll_path

    dll_ok = True
    dll_error: str | None = None
    try:
        ensure_cuda_dll_path()
    except Exception as exc:  # noqa: BLE001
        dll_ok = False
        dll_error = str(exc)

    gpu = _nvidia_smi()
    wheels = _cublas_wheels()
    ok = bool(gpu.get("ok") and wheels and dll_ok)
    hint = None
    if not gpu.get("ok"):
        hint = "No se ve GPU NVIDIA (nvidia-smi). Usá device=cpu o instalá drivers."
    elif not wheels:
        hint = "Faltan wheels CUDA de pip (cublas/cudnn). Corré: py -3.11 -m pip install -r requirements.txt"
    elif not dll_ok:
        hint = (
            "CUDA DLL path falló (ruta larga del Python Store / WinError 206). "
            "Reintentá; si sigue, usá device=cpu o Python de python.org."
        )
        if dll_error:
            hint = f"{hint} Detalle: {dll_error}"
    return {
        "ok": ok,
        "gpu": gpu,
        "cublas_wheels": wheels,
        "dll_path_ok": dll_ok,
        "hint": hint,
    }


def _ollama() -> dict[str, Any]:
    from transcribe.study import DEFAULT_OLLAMA_URL, probe_ollama

    info = probe_ollama(DEFAULT_OLLAMA_URL)
    return {
        "ok": bool(info.get("ok")),
        "url": info.get("url") or DEFAULT_OLLAMA_URL,
        "models": info.get("models") or [],
        "recommended_model": info.get("recommended_model"),
        "error": info.get("error"),
    }


def collect_health() -> dict[str, Any]:
    ffmpeg = _ffmpeg()
    try:
        cuda = _cuda_runtime_probe()
    except Exception as exc:  # noqa: BLE001
        cuda = {
            "ok": False,
            "gpu": {"ok": False, "name": None, "driver": None},
            "cublas_wheels": False,
            "dll_path_ok": False,
            "hint": f"No se pudo chequear CUDA: {exc}",
        }
    try:
        ollama = _ollama()
    except Exception as exc:  # noqa: BLE001
        ollama = {
            "ok": False,
            "url": "http://127.0.0.1:11434",
            "models": [],
            "recommended_model": None,
            "error": str(exc),
        }
    warnings: list[str] = []
    if not ffmpeg["ok"]:
        warnings.append("ffmpeg no está en PATH — los videos van a fallar.")
    if cuda.get("hint"):
        warnings.append(cuda["hint"])
    if not ollama.get("ok"):
        warnings.append(
            "Sin Ollama — Estudio usará outline/cards heurísticos "
            "(opcional: instalá Ollama en 127.0.0.1:11434)."
        )
    return {
        "ok": True,
        "python": sys.version.split()[0],
        "platform": sys.platform,
        "ffmpeg": ffmpeg,
        "cuda": cuda,
        "ollama": ollama,
        "warnings": warnings,
        "recommended_device": "cuda" if cuda.get("ok") else "cpu",
    }
