from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

AUDIO_EXTENSIONS = {".m4a", ".mp3", ".wav", ".flac", ".ogg", ".aac", ".wma"}
VIDEO_EXTENSIONS = {".mp4", ".mkv", ".webm", ".avi", ".mov", ".m4v"}


def is_audio(path: Path) -> bool:
    return path.suffix.lower() in AUDIO_EXTENSIONS


def is_video(path: Path) -> bool:
    return path.suffix.lower() in VIDEO_EXTENSIONS


def require_ffmpeg() -> str:
    exe = shutil.which("ffmpeg")
    if not exe:
        raise RuntimeError(
            "ffmpeg no está en el PATH. Instálalo (winget install Gyan.FFmpeg) y reinicia la terminal."
        )
    return exe


def prepare_audio(source: Path, work_dir: Path) -> Path:
    """
    Return a path to audio usable by Whisper.
    Copies audio as-is, or extracts mono 16k wav from video.
    """
    work_dir.mkdir(parents=True, exist_ok=True)
    source = source.resolve()
    if not source.is_file():
        raise FileNotFoundError(f"No existe el archivo: {source}")

    if is_audio(source):
        dest = work_dir / f"audio{source.suffix.lower()}"
        if source.resolve() != dest.resolve():
            shutil.copy2(source, dest)
        return dest

    if is_video(source):
        ffmpeg = require_ffmpeg()
        dest = work_dir / "audio.wav"
        cmd = [
            ffmpeg,
            "-y",
            "-i",
            str(source),
            "-vn",
            "-ac",
            "1",
            "-ar",
            "16000",
            "-c:a",
            "pcm_s16le",
            str(dest),
        ]
        proc = subprocess.run(cmd, capture_output=True, text=True)
        if proc.returncode != 0 or not dest.is_file():
            err = (proc.stderr or proc.stdout or "").strip()[-2000:]
            raise RuntimeError(f"No se pudo extraer audio del video.\n{err}")
        return dest

    raise ValueError(
        f"Formato no soportado: {source.suffix}. "
        f"Audio: {', '.join(sorted(AUDIO_EXTENSIONS))} | "
        f"Video: {', '.join(sorted(VIDEO_EXTENSIONS))}"
    )
