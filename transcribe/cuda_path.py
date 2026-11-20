from __future__ import annotations

import os
import sys
from pathlib import Path


def _win_short_path(path: str) -> str:
    """Best-effort 8.3 short path (avoids WinError 206 on Store Python)."""
    try:
        import ctypes

        GetShortPathNameW = ctypes.windll.kernel32.GetShortPathNameW
        needed = GetShortPathNameW(path, None, 0)
        if needed <= 0:
            return path
        buf = ctypes.create_unicode_buffer(needed)
        if GetShortPathNameW(path, buf, needed) == 0:
            return path
        return buf.value or path
    except Exception:  # noqa: BLE001
        return path


def ensure_cuda_dll_path() -> list[str]:
    """Add pip-installed NVIDIA CUDA bin dirs to DLL search / PATH (Windows).

    Returns the directories that were registered (may be empty).
    Never raises: Store-Python long paths can trip WinError 206.
    """
    if sys.platform != "win32":
        return []
    try:
        import nvidia  # type: ignore
    except ImportError:
        return []

    nvidia_root = Path(nvidia.__path__[0])
    bin_dirs = [
        nvidia_root / "cublas" / "bin",
        nvidia_root / "cudnn" / "bin",
        nvidia_root / "cuda_runtime" / "bin",
        nvidia_root / "cuda_nvrtc" / "bin",
    ]
    existing = [str(p.resolve()) for p in bin_dirs if p.is_dir()]
    if not existing:
        return []

    registered: list[str] = []
    if hasattr(os, "add_dll_directory"):
        for path in existing:
            candidates = [path]
            short = _win_short_path(path)
            if short and short not in candidates:
                candidates.insert(0, short)
            for candidate in candidates:
                try:
                    os.add_dll_directory(candidate)
                    registered.append(candidate)
                    break
                except OSError:
                    continue

    # Always prepend long paths to PATH as a fallback for loaders that use it.
    os.environ["PATH"] = os.pathsep.join(existing + [os.environ.get("PATH", "")])
    return registered or existing
