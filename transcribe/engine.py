from __future__ import annotations

import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable

from . import config
from .cuda_path import ensure_cuda_dll_path
from .export import filter_segments, write_json, write_markdown, write_srt

ProgressCb = Callable[[dict[str, Any]], None]


@dataclass
class ModelHandle:
    model: Any
    model_name: str
    device: str
    compute_type: str


_MODEL: ModelHandle | None = None


def load_model(
    model_size: str | None = None,
    device: str | None = None,
    compute_type: str | None = None,
) -> ModelHandle:
    global _MODEL
    ensure_cuda_dll_path()
    from faster_whisper import WhisperModel

    model_size = model_size or config.DEFAULT_MODEL
    device = device or config.DEFAULT_DEVICE
    compute_type = compute_type or config.DEFAULT_COMPUTE_TYPE

    if (
        _MODEL is not None
        and _MODEL.model_name == model_size
        and _MODEL.device == device
        and _MODEL.compute_type == compute_type
    ):
        return _MODEL

    tried: list[tuple[str, str, str]] = []
    candidates: list[tuple[str, str, str]] = [(model_size, device, compute_type)]
    if device == "auto":
        candidates = [
            (model_size, "cuda", "float16"),
            (model_size, "cpu", config.FALLBACK_COMPUTE_TYPE),
            (config.FALLBACK_MODEL, "cpu", config.FALLBACK_COMPUTE_TYPE),
        ]
    elif device == "cuda":
        candidates.extend(
            [
                (model_size, "cuda", "int8_float16"),
                (config.FALLBACK_MODEL, "cuda", "float16"),
                (config.FALLBACK_MODEL, config.FALLBACK_DEVICE, config.FALLBACK_COMPUTE_TYPE),
            ]
        )
    else:
        candidates.append(
            (config.FALLBACK_MODEL, config.FALLBACK_DEVICE, config.FALLBACK_COMPUTE_TYPE)
        )

    last_error: Exception | None = None
    for size, dev, ctype in candidates:
        key = (size, dev, ctype)
        if key in tried:
            continue
        tried.append(key)
        try:
            model = WhisperModel(size, device=dev, compute_type=ctype)
            _MODEL = ModelHandle(model=model, model_name=size, device=dev, compute_type=ctype)
            return _MODEL
        except Exception as exc:  # noqa: BLE001
            last_error = exc

    raise RuntimeError(f"No se pudo cargar Whisper. Último error: {last_error}")


def transcribe_file(
    audio_path: Path,
    *,
    out_dir: Path,
    title: str,
    language: str | None = config.DEFAULT_LANGUAGE,
    initial_prompt: str | None = config.INITIAL_PROMPT,
    model_size: str | None = None,
    device: str | None = None,
    compute_type: str | None = None,
    write_subs: bool = True,
    on_progress: ProgressCb | None = None,
) -> dict[str, Any]:
    handle = load_model(model_size, device, compute_type)
    out_dir.mkdir(parents=True, exist_ok=True)

    if on_progress:
        on_progress({"event": "model_ready", "model": handle.model_name, "device": handle.device})

    started = time.perf_counter()
    lang_arg = None if language in (None, "", "auto") else language
    segments_iter, info = handle.model.transcribe(
        str(audio_path),
        language=lang_arg,
        beam_size=config.BEAM_SIZE,
        vad_filter=config.VAD_FILTER,
        initial_prompt=initial_prompt,
        condition_on_previous_text=config.CONDITION_ON_PREVIOUS_TEXT,
        compression_ratio_threshold=config.COMPRESSION_RATIO_THRESHOLD,
        log_prob_threshold=config.LOG_PROB_THRESHOLD,
        no_speech_threshold=config.NO_SPEECH_THRESHOLD,
        temperature=0.0,
    )

    raw_segments: list[dict[str, Any]] = []
    last_report = started
    for seg in segments_iter:
        text = (seg.text or "").strip()
        if not text:
            continue
        raw_segments.append(
            {
                "start": round(float(seg.start), 3),
                "end": round(float(seg.end), 3),
                "text": text,
            }
        )
        now = time.perf_counter()
        if on_progress and now - last_report >= 2.0:
            on_progress(
                {
                    "event": "progress",
                    "segments": len(raw_segments),
                    "audio_sec": raw_segments[-1]["end"],
                }
            )
            last_report = now

    segments = filter_segments(raw_segments)
    elapsed = time.perf_counter() - started
    duration = float(getattr(info, "duration", 0.0) or 0.0)

    md_path = out_dir / "transcripcion.md"
    json_path = out_dir / "segmentos.json"
    srt_path = out_dir / "subtitulos.srt"

    write_json(
        json_path,
        clase=title,
        source=audio_path.name,
        model=handle.model_name,
        language=lang_arg or "auto",
        duration=duration or None,
        segments=segments,
        curso=None,
        temas=None,
    )
    write_markdown(
        md_path,
        clase=title,
        source=audio_path.name,
        model=handle.model_name,
        language=lang_arg or "auto",
        duration=duration or None,
        segments=segments,
        curso=None,
        temas=None,
    )
    if write_subs:
        write_srt(srt_path, segments)

    result = {
        "title": title,
        "model": handle.model_name,
        "device": handle.device,
        "compute_type": handle.compute_type,
        "language": language,
        "segments": len(segments),
        "dropped": len(raw_segments) - len(segments),
        "duration_sec": duration,
        "elapsed_sec": elapsed,
        "rtf": (elapsed / duration) if duration > 0 else None,
        "paths": {
            "md": str(md_path),
            "json": str(json_path),
            "srt": str(srt_path) if write_subs else None,
        },
    }
    if on_progress:
        on_progress({"event": "done", **result})
    return result
