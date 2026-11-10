#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path
from typing import Any

from transcribe.cuda_path import ensure_cuda_dll_path

ensure_cuda_dll_path()

from transcribe.config import (
    BEAM_SIZE,
    COMPRESSION_RATIO_THRESHOLD,
    CONDITION_ON_PREVIOUS_TEXT,
    COURSE_NAME,
    COURSE_TOPICS,
    DEFAULT_COMPUTE_TYPE,
    DEFAULT_DEVICE,
    DEFAULT_LANGUAGE,
    DEFAULT_MODEL,
    FALLBACK_COMPUTE_TYPE,
    FALLBACK_DEVICE,
    FALLBACK_MODEL,
    INITIAL_PROMPT,
    LOG_PROB_THRESHOLD,
    NO_SPEECH_THRESHOLD,
    OUTPUT_DIR,
    VAD_FILTER,
)
from transcribe.discover import ClassAudio, discover_class_audios
from transcribe.export import filter_segments, write_json, write_markdown, write_srt


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Transcribe audios de Clases/ a Markdown + JSON "
            "(faster-whisper, español)."
        )
    )
    parser.add_argument(
        "--clase",
        type=int,
        default=None,
        help="Número de clase a transcribir (ej. 1). Sin esto, procesa todas.",
    )
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help=f"Modelo Whisper (default: {DEFAULT_MODEL})",
    )
    parser.add_argument(
        "--device",
        default=DEFAULT_DEVICE,
        choices=["cuda", "cpu", "auto"],
        help=f"Dispositivo (default: {DEFAULT_DEVICE})",
    )
    parser.add_argument(
        "--compute-type",
        default=DEFAULT_COMPUTE_TYPE,
        help=f"Tipo de cómputo CTranslate2 (default: {DEFAULT_COMPUTE_TYPE})",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Re-transcribir aunque ya exista segmentos.json",
    )
    parser.add_argument(
        "--srt",
        action="store_true",
        help="También escribir subtítulos .srt",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=OUTPUT_DIR,
        help=f"Carpeta de salida (default: {OUTPUT_DIR})",
    )
    return parser.parse_args()


def load_model(model_size: str, device: str, compute_type: str):
    from faster_whisper import WhisperModel

    tried: list[tuple[str, str, str]] = []
    candidates: list[tuple[str, str, str]] = [
        (model_size, device, compute_type),
    ]

    if device == "auto":
        candidates = [
            (model_size, "cuda", compute_type if compute_type != "int8" else "float16"),
            (model_size, "cpu", FALLBACK_COMPUTE_TYPE),
            (FALLBACK_MODEL, "cpu", FALLBACK_COMPUTE_TYPE),
        ]
    elif device == "cuda":
        candidates.extend(
            [
                (model_size, "cuda", "int8_float16"),
                (FALLBACK_MODEL, "cuda", "float16"),
                (FALLBACK_MODEL, FALLBACK_DEVICE, FALLBACK_COMPUTE_TYPE),
            ]
        )
    else:
        candidates.append((FALLBACK_MODEL, FALLBACK_DEVICE, FALLBACK_COMPUTE_TYPE))

    last_error: Exception | None = None
    for size, dev, ctype in candidates:
        key = (size, dev, ctype)
        if key in tried:
            continue
        tried.append(key)
        try:
            print(f"Cargando modelo '{size}' en {dev} ({ctype})...")
            model = WhisperModel(size, device=dev, compute_type=ctype)
            print(f"Modelo listo: {size} / {dev} / {ctype}")
            return model, size, dev, ctype
        except Exception as exc:  # noqa: BLE001 - want any load failure fallback
            last_error = exc
            print(f"No se pudo cargar ({size}, {dev}, {ctype}): {exc}")

    raise RuntimeError(f"No se pudo cargar ningún modelo Whisper. Último error: {last_error}")


def output_paths(out_root: Path, item: ClassAudio) -> dict[str, Path]:
    folder = out_root / item.class_name
    return {
        "dir": folder,
        "md": folder / "transcripcion.md",
        "json": folder / "segmentos.json",
        "srt": folder / "subtitulos.srt",
    }


def already_done(paths: dict[str, Path], force: bool) -> bool:
    return (not force) and paths["json"].is_file() and paths["md"].is_file()


def transcribe_one(
    model,
    item: ClassAudio,
    *,
    model_name: str,
    language: str,
    write_subs: bool,
    out_root: Path,
) -> dict[str, Any]:
    paths = output_paths(out_root, item)
    paths["dir"].mkdir(parents=True, exist_ok=True)

    print(f"\n=== {item.class_name} ===")
    print(f"Audio: {item.audio_path}")

    started = time.perf_counter()
    segments_iter, info = model.transcribe(
        str(item.audio_path),
        language=language,
        beam_size=BEAM_SIZE,
        vad_filter=VAD_FILTER,
        initial_prompt=INITIAL_PROMPT,
        condition_on_previous_text=CONDITION_ON_PREVIOUS_TEXT,
        compression_ratio_threshold=COMPRESSION_RATIO_THRESHOLD,
        log_prob_threshold=LOG_PROB_THRESHOLD,
        no_speech_threshold=NO_SPEECH_THRESHOLD,
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
        if now - last_report >= 60:
            print(
                f"  ... {len(raw_segments)} segs, "
                f"hasta {raw_segments[-1]['end']/60:.1f} min de audio"
            )
            last_report = now

    segments = filter_segments(raw_segments)
    dropped = len(raw_segments) - len(segments)

    elapsed = time.perf_counter() - started
    duration = float(getattr(info, "duration", 0.0) or 0.0)
    rtf = (elapsed / duration) if duration > 0 else None

    write_json(
        paths["json"],
        clase=item.class_name,
        source=item.audio_path.name,
        model=model_name,
        language=language,
        duration=duration or None,
        segments=segments,
        curso=COURSE_NAME,
        temas=list(COURSE_TOPICS),
    )
    write_markdown(
        paths["md"],
        clase=item.class_name,
        source=item.audio_path.name,
        model=model_name,
        language=language,
        duration=duration or None,
        segments=segments,
        curso=COURSE_NAME,
        temas=list(COURSE_TOPICS),
    )
    if write_subs:
        write_srt(paths["srt"], segments)

    print(
        f"Listo: {len(segments)} segmentos"
        + (f" (filtrados {dropped})" if dropped else "")
        + f" | audio {duration/60:.1f} min | "
        f"wall {elapsed/60:.1f} min"
        + (f" | RTF {rtf:.2f}x" if rtf is not None else "")
    )
    print(f"MD:   {paths['md']}")
    print(f"JSON: {paths['json']}")
    return {
        "clase": item.class_name,
        "segments": len(segments),
        "duration": duration,
        "elapsed": elapsed,
    }


def main() -> int:
    args = parse_args()
    out_root: Path = args.output_dir
    out_root.mkdir(parents=True, exist_ok=True)

    # Prefer renaming legacy typo folder if present and empty target.
    legacy = Path(__file__).resolve().parent / "Transcrpcion"
    if legacy.is_dir() and out_root.resolve() != legacy.resolve():
        # Keep both; new code writes to Transcripciones.
        pass

    items = discover_class_audios(class_number=args.clase)
    if not items:
        where = f"clase {args.clase}" if args.clase else "Clases/"
        print(f"No se encontraron audios para {where}", file=sys.stderr)
        return 1

    print(f"Clases a procesar: {[i.class_name for i in items]}")
    model, model_name, device, compute_type = load_model(
        args.model, args.device, args.compute_type
    )
    print(f"Usando: model={model_name} device={device} compute_type={compute_type}")

    results = []
    for item in items:
        paths = output_paths(out_root, item)
        if already_done(paths, args.force):
            print(f"Omitiendo {item.class_name} (ya existe). Usa --force para rehacer.")
            continue
        results.append(
            transcribe_one(
                model,
                item,
                model_name=model_name,
                language=DEFAULT_LANGUAGE,
                write_subs=args.srt,
                out_root=out_root,
            )
        )

    if not results:
        print("Nada nuevo por procesar.")
        return 0

    total_audio = sum(r["duration"] for r in results)
    total_wall = sum(r["elapsed"] for r in results)
    print("\n=== Resumen ===")
    for r in results:
        print(
            f"- {r['clase']}: {r['segments']} segs, "
            f"{r['duration']/60:.1f} min audio, {r['elapsed']/60:.1f} min wall"
        )
    print(f"Total audio: {total_audio/60:.1f} min | Total wall: {total_wall/60:.1f} min")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
