from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from .config import CLASSES_DIR

_CLASS_RE = re.compile(r"^Clase\s+(\d+)$", re.IGNORECASE)

AUDIO_SUFFIXES = {".m4a", ".wav", ".mp3", ".flac", ".ogg"}


@dataclass(frozen=True)
class ClassAudio:
    """One class folder with one or more audio files (sorted)."""

    class_name: str
    class_number: int
    audio_paths: tuple[Path, ...]

    @property
    def audio_path(self) -> Path:
        """First audio (back-compat for single-file callers)."""
        return self.audio_paths[0]


def _list_audios(folder: Path) -> list[Path]:
    audios = sorted(folder.glob("audio*.m4a"))
    if not audios:
        audios = sorted(
            p
            for p in folder.iterdir()
            if p.is_file() and p.suffix.lower() in AUDIO_SUFFIXES
        )
    return audios


def discover_class_audios(
    classes_dir: Path | None = None,
    class_number: int | None = None,
) -> list[ClassAudio]:
    """Find audio files under Clases/Clase N/ (all parts, sorted by name)."""
    root = classes_dir or CLASSES_DIR
    if not root.is_dir():
        raise FileNotFoundError(f"No existe la carpeta de clases: {root}")

    found: list[ClassAudio] = []
    for folder in sorted(root.iterdir(), key=_folder_sort_key):
        if not folder.is_dir():
            continue
        match = _CLASS_RE.match(folder.name.strip())
        if not match:
            continue
        number = int(match.group(1))
        if class_number is not None and number != class_number:
            continue

        audios = _list_audios(folder)
        if not audios:
            continue

        found.append(
            ClassAudio(
                class_name=folder.name,
                class_number=number,
                audio_paths=tuple(audios),
            )
        )

    return found


def _folder_sort_key(path: Path) -> tuple[int, str]:
    match = _CLASS_RE.match(path.name.strip())
    if match:
        return (int(match.group(1)), path.name.lower())
    return (10_000, path.name.lower())
