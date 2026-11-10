from __future__ import annotations

import os
import sys
from pathlib import Path


def ensure_cuda_dll_path() -> None:
    """Add pip-installed NVIDIA CUDA bin dirs to PATH (Windows)."""
    if sys.platform != "win32":
        return
    try:
        import nvidia  # type: ignore
    except ImportError:
        return

    nvidia_root = Path(nvidia.__path__[0])
    bin_dirs = [
        nvidia_root / "cublas" / "bin",
        nvidia_root / "cudnn" / "bin",
        nvidia_root / "cuda_runtime" / "bin",
        nvidia_root / "cuda_nvrtc" / "bin",
    ]
    existing = [str(p) for p in bin_dirs if p.is_dir()]
    if not existing:
        return

    if hasattr(os, "add_dll_directory"):
        for path in existing:
            os.add_dll_directory(path)
    os.environ["PATH"] = os.pathsep.join(existing + [os.environ.get("PATH", "")])
