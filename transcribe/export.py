from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path
from typing import Any, Iterable

_REPEATED_FILLER_RE = re.compile(
    r"^(?:(?:pero|eh|este|mmm|ah|um|uh)(?:\.\.\.|,|\s)+)+$",
    re.IGNORECASE,
)


def is_hallucinated_segment(text: str) -> bool:
    """Detect obvious ASR repetition loops / filler spam."""
    cleaned = (text or "").strip()
    if not cleaned:
        return True
    if _REPEATED_FILLER_RE.match(cleaned):
        return True
    if cleaned.count("Pero...") >= 4:
        return True
    tokens = re.findall(r"\S+", cleaned)
    if len(tokens) >= 8:
        top_token, top_count = Counter(tokens).most_common(1)[0]
        if top_count / len(tokens) >= 0.55 and len(top_token) <= 12:
            return True
    return False


def filter_segments(segments: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    return [
        seg
        for seg in segments
        if not is_hallucinated_segment(str(seg.get("text") or ""))
    ]


def format_timestamp(seconds: float) -> str:
    total = max(0, int(seconds))
    hours, rem = divmod(total, 3600)
    minutes, secs = divmod(rem, 60)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"


def merge_segments_for_markdown(
    segments: Iterable[dict[str, Any]],
    max_gap: float = 2.0,
    max_chars: int = 900,
) -> list[dict[str, Any]]:
    """Group short ASR segments into readable markdown paragraphs."""
    groups: list[dict[str, Any]] = []
    current: dict[str, Any] | None = None

    for seg in segments:
        text = (seg.get("text") or "").strip()
        if not text:
            continue
        start = float(seg["start"])
        end = float(seg["end"])

        if current is None:
            current = {"start": start, "end": end, "text": text}
            continue

        gap = start - float(current["end"])
        too_long = len(current["text"]) + 1 + len(text) > max_chars
        if gap > max_gap or too_long:
            groups.append(current)
            current = {"start": start, "end": end, "text": text}
        else:
            current["end"] = end
            current["text"] = f"{current['text']} {text}".strip()

    if current is not None:
        groups.append(current)
    return groups


def _prepare_segments(
    segments: list[dict[str, Any]], *, clean: bool
) -> list[dict[str, Any]]:
    return filter_segments(segments) if clean else list(segments)


def merge_timelines(
    part_payloads: list[dict[str, Any]],
    *,
    clase: str | None = None,
    model: str | None = None,
    language: str | None = None,
    curso: str | None = None,
    temas: list[str] | None = None,
) -> dict[str, Any]:
    """Concatenate part segmentos.json payloads into one continuous timeline.

    Each part keeps a local 0-based timeline; offsets are the sum of prior
    part durations (from duration_sec, else max segment end).
    """
    if not part_payloads:
        raise ValueError("merge_timelines requiere al menos una parte")

    first = part_payloads[0]
    merged_segments: list[dict[str, Any]] = []
    parts_meta: list[dict[str, Any]] = []
    offset = 0.0
    source_names: list[str] = []

    for index, payload in enumerate(part_payloads):
        source = str(payload.get("source") or f"part-{index}")
        source_names.append(source)
        raw_duration = payload.get("duration_sec")
        try:
            duration = float(raw_duration) if raw_duration is not None else 0.0
        except (TypeError, ValueError):
            duration = 0.0

        segs = payload.get("segments") or []
        if not isinstance(segs, list):
            segs = []

        if duration <= 0 and segs:
            try:
                duration = max(float(s.get("end") or 0) for s in segs)
            except (TypeError, ValueError):
                duration = 0.0

        for seg in segs:
            text = str(seg.get("text") or "")
            try:
                start = float(seg["start"]) + offset
                end = float(seg["end"]) + offset
            except (KeyError, TypeError, ValueError):
                continue
            merged_segments.append(
                {
                    "start": round(start, 3),
                    "end": round(end, 3),
                    "text": text,
                }
            )

        parts_meta.append(
            {
                "index": index,
                "source": source,
                "offset_sec": round(offset, 3),
                "duration_sec": round(duration, 3) if duration else 0.0,
            }
        )
        offset += duration

    total_duration = round(offset, 3) if offset else None
    source_label = " + ".join(source_names)

    result: dict[str, Any] = {
        "clase": clase if clase is not None else first.get("clase"),
        "curso": curso if curso is not None else first.get("curso"),
        "temas": temas if temas is not None else (first.get("temas") or []),
        "source": source_label,
        "model": model if model is not None else first.get("model"),
        "language": language if language is not None else first.get("language"),
        "duration_sec": total_duration,
        "parts": parts_meta,
        "segments": merged_segments,
    }
    return result


def write_merged_artifacts(
    out_dir: Path,
    merged: dict[str, Any],
    *,
    write_subs: bool = True,
    clean: bool = False,
) -> dict[str, Path]:
    """Write MD/JSON/SRT from a merge_timelines() result into out_dir."""
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path = out_dir / "segmentos.json"
    md_path = out_dir / "transcripcion.md"
    srt_path = out_dir / "subtitulos.srt"
    segments = list(merged.get("segments") or [])
    parts = merged.get("parts") if isinstance(merged.get("parts"), list) else None
    write_json(
        json_path,
        clase=str(merged.get("clase") or "Sin título"),
        source=str(merged.get("source") or ""),
        model=str(merged.get("model") or ""),
        language=str(merged.get("language") or "es"),
        duration=merged.get("duration_sec"),
        segments=segments,
        curso=str(merged["curso"]) if merged.get("curso") else None,
        temas=[str(t) for t in (merged.get("temas") or [])],
        parts=parts,
        clean=clean,
    )
    write_markdown(
        md_path,
        clase=str(merged.get("clase") or "Sin título"),
        source=str(merged.get("source") or ""),
        model=str(merged.get("model") or ""),
        language=str(merged.get("language") or "es"),
        duration=merged.get("duration_sec"),
        segments=segments,
        curso=str(merged["curso"]) if merged.get("curso") else None,
        temas=[str(t) for t in (merged.get("temas") or [])],
        clean=clean,
    )
    paths: dict[str, Path] = {"json": json_path, "md": md_path}
    if write_subs:
        write_srt(srt_path, segments, clean=clean)
        paths["srt"] = srt_path
    return paths


def write_json(
    path: Path,
    *,
    clase: str,
    source: str,
    model: str,
    language: str,
    duration: float | None,
    segments: list[dict[str, Any]],
    curso: str | None = None,
    temas: list[str] | None = None,
    parts: list[dict[str, Any]] | None = None,
    clean: bool = True,
) -> None:
    prepared = _prepare_segments(segments, clean=clean)
    payload: dict[str, Any] = {
        "clase": clase,
        "curso": curso,
        "temas": temas or [],
        "source": source,
        "model": model,
        "language": language,
        "duration_sec": duration,
        "segments": prepared,
    }
    if parts is not None:
        payload["parts"] = parts
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def write_markdown(
    path: Path,
    *,
    clase: str,
    source: str,
    model: str,
    language: str,
    duration: float | None,
    segments: list[dict[str, Any]],
    curso: str | None = None,
    temas: list[str] | None = None,
    clean: bool = True,
) -> None:
    groups = merge_segments_for_markdown(_prepare_segments(segments, clean=clean))

    front = [
        "---",
        f'clase: "{clase}"',
    ]
    if curso:
        front.append(f'curso: "{curso}"')
    if temas:
        temas_literal = ", ".join(f'"{t}"' for t in temas)
        front.append(f"temas: [{temas_literal}]")
    front.extend(
        [
            f"fuente: {source}",
            f"modelo: {model}",
            f"idioma: {language}",
        ]
    )
    if duration is not None:
        front.append(f"duration_sec: {round(duration, 1)}")
    front.extend(["---", ""])

    body: list[str] = []
    for group in groups:
        stamp = format_timestamp(float(group["start"]))
        body.append(f"## [{stamp}]")
        body.append("")
        body.append(str(group["text"]).strip())
        body.append("")

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(front + body).rstrip() + "\n", encoding="utf-8")


def write_srt(
    path: Path,
    segments: list[dict[str, Any]],
    *,
    clean: bool = True,
) -> None:
    blocks: list[str] = []
    index = 1
    for seg in _prepare_segments(segments, clean=clean):
        text = (seg.get("text") or "").strip()
        if not text:
            continue
        start = _srt_ts(float(seg["start"]))
        end = _srt_ts(float(seg["end"]))
        blocks.append(f"{index}\n{start} --> {end}\n{text}\n")
        index += 1
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(blocks).rstrip() + "\n", encoding="utf-8")


def rewrite_job_artifacts(
    json_path: Path,
    md_path: Path,
    srt_path: Path,
    segments: list[dict[str, Any]],
) -> dict[str, Any]:
    """Rewrite JSON/MD/SRT keeping existing meta; preserve user-edited text (clean=False)."""
    meta: dict[str, Any] = {}
    if json_path.is_file():
        try:
            meta = json.loads(json_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            meta = {}

    clase = str(meta.get("clase") or "Sin título")
    source = str(meta.get("source") or "")
    model = str(meta.get("model") or "")
    language = str(meta.get("language") or "es")
    duration = meta.get("duration_sec")
    if duration is not None:
        try:
            duration = float(duration)
        except (TypeError, ValueError):
            duration = None
    curso = meta.get("curso")
    if curso is not None:
        curso = str(curso) or None
    temas = meta.get("temas")
    if not isinstance(temas, list):
        temas = []
    parts = meta.get("parts")
    if not isinstance(parts, list):
        parts = None

    normalized = [
        {
            "start": float(seg["start"]),
            "end": float(seg["end"]),
            "text": str(seg.get("text") or ""),
        }
        for seg in segments
    ]

    write_json(
        json_path,
        clase=clase,
        source=source,
        model=model,
        language=language,
        duration=duration,
        segments=normalized,
        curso=curso,
        temas=[str(t) for t in temas],
        parts=parts,
        clean=False,
    )
    write_markdown(
        md_path,
        clase=clase,
        source=source,
        model=model,
        language=language,
        duration=duration,
        segments=normalized,
        curso=curso,
        temas=[str(t) for t in temas],
        clean=False,
    )
    write_srt(srt_path, normalized, clean=False)
    out: dict[str, Any] = {
        "clase": clase,
        "source": source,
        "model": model,
        "language": language,
        "duration_sec": duration,
        "curso": curso,
        "temas": [str(t) for t in temas],
        "segments": normalized,
    }
    if parts is not None:
        out["parts"] = parts
    return out


def _srt_ts(seconds: float) -> str:
    millis = int(round(max(0.0, seconds) * 1000))
    hours, rem = divmod(millis, 3_600_000)
    minutes, rem = divmod(rem, 60_000)
    secs, ms = divmod(rem, 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{ms:03d}"
