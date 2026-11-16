from __future__ import annotations

import json
import re
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from transcribe.export import format_timestamp

DEFAULT_OLLAMA_URL = "http://127.0.0.1:11434"
DEFAULT_CHAPTER_GAP_SEC = 45.0
DEFAULT_MAX_CARDS = 60
DEFAULT_MAX_CHAPTERS = 40
OLLAMA_TIMEOUT_SEC = 120.0


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _title_from_text(text: str, max_words: int = 10) -> str:
    cleaned = re.sub(r"\s+", " ", (text or "").strip())
    if not cleaned:
        return "Sin título"
    words = cleaned.split(" ")
    title = " ".join(words[:max_words])
    if len(words) > max_words:
        title = title.rstrip(".,;:") + "…"
    return title[:120]


def _first_sentences(text: str, max_sentences: int = 2, max_chars: int = 400) -> str:
    cleaned = re.sub(r"\s+", " ", (text or "").strip())
    if not cleaned:
        return ""
    parts = re.split(r"(?<=[.!?])\s+", cleaned)
    out = " ".join(parts[:max_sentences]).strip()
    if len(out) > max_chars:
        out = out[: max_chars - 1].rstrip() + "…"
    return out


def build_heuristic_chapters(
    segments: list[dict[str, Any]],
    *,
    gap_sec: float = DEFAULT_CHAPTER_GAP_SEC,
    max_chapters: int = DEFAULT_MAX_CHAPTERS,
) -> list[dict[str, Any]]:
    """Split transcript into chapters on long pauses between segments."""
    usable: list[dict[str, Any]] = []
    for seg in segments:
        text = str(seg.get("text") or "").strip()
        if not text:
            continue
        try:
            start = float(seg["start"])
            end = float(seg["end"])
        except (KeyError, TypeError, ValueError):
            continue
        usable.append({"start": start, "end": end, "text": text})

    if not usable:
        return []

    chapters: list[dict[str, Any]] = []
    current: dict[str, Any] | None = None

    for seg in usable:
        if current is None:
            current = {
                "title": _title_from_text(seg["text"]),
                "start_sec": seg["start"],
                "end_sec": seg["end"],
                "text": seg["text"],
            }
            continue
        gap = seg["start"] - float(current["end_sec"])
        if gap > gap_sec and len(chapters) + 1 < max_chapters:
            current["summary"] = _first_sentences(current["text"])
            chapters.append(current)
            current = {
                "title": _title_from_text(seg["text"]),
                "start_sec": seg["start"],
                "end_sec": seg["end"],
                "text": seg["text"],
            }
        else:
            current["end_sec"] = seg["end"]
            current["text"] = f"{current['text']} {seg['text']}".strip()

    if current is not None:
        current["summary"] = _first_sentences(current["text"])
        chapters.append(current)

    # Drop internal full text from exported chapter meta (keep summary)
    for ch in chapters:
        ch.pop("text", None)
    return chapters


def build_extractive_qa(
    chapters: list[dict[str, Any]],
    chapter_texts: list[str],
    *,
    max_cards: int = DEFAULT_MAX_CARDS,
) -> list[dict[str, str]]:
    """Simple Q/A pairs from chapter snippets (no LLM)."""
    cards: list[dict[str, str]] = []
    for ch, text in zip(chapters, chapter_texts):
        if len(cards) >= max_cards:
            break
        stamp = format_timestamp(float(ch["start_sec"]))
        snippet = _first_sentences(text, max_sentences=1, max_chars=160)
        back = _first_sentences(text, max_sentences=2, max_chars=500)
        if not back:
            continue
        front = f"¿De qué trata el tramo en [{stamp}]?"
        if snippet:
            front = f"{front}\n({snippet})"
        cards.append(
            {
                "front": front,
                "back": back,
                "start_sec": str(ch["start_sec"]),
            }
        )
    return cards


def to_open_cards_library(
    *,
    deck_name: str,
    cards_qa: list[dict[str, str]],
    description: str | None = None,
    tags: list[str] | None = None,
) -> dict[str, Any]:
    now = _utc_now_iso()
    oc_cards: list[dict[str, Any]] = []
    for qa in cards_qa:
        front = str(qa.get("front") or "").strip()
        back = str(qa.get("back") or "").strip()
        if not front or not back:
            continue
        oc_cards.append(
            {
                "id": str(uuid.uuid4()),
                "front": [{"type": "text", "content": front}],
                "back": [{"type": "text", "content": back}],
                "state": "unseen",
                "createdAt": now,
                "updatedAt": now,
            }
        )
    deck_tags = ["Cynta"]
    if tags:
        for t in tags:
            t = str(t).strip()
            if t and t not in deck_tags:
                deck_tags.append(t[:50])
    return {
        "format": "open-cards",
        "version": 1,
        "exportedAt": now,
        "decks": [
            {
                "id": str(uuid.uuid4()),
                "name": (deck_name or "Cynta").strip()[:120] or "Cynta",
                "description": (
                    description
                    or "Generado por Cynta desde la transcripción"
                )[:2000],
                "tags": deck_tags,
                "cards": oc_cards[:1000],
                "createdAt": now,
                "updatedAt": now,
            }
        ],
    }


def write_outline_md(path: Path, chapters: list[dict[str, Any]], *, title: str) -> None:
    lines = [f"# Outline — {title}", ""]
    for i, ch in enumerate(chapters, start=1):
        stamp = format_timestamp(float(ch["start_sec"]))
        lines.append(f"{i}. **[{stamp}]** {ch.get('title') or 'Sin título'}")
        summary = ch.get("summary")
        if summary:
            lines.append(f"   - {summary}")
        lines.append("")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def probe_ollama(base_url: str = DEFAULT_OLLAMA_URL, timeout: float = 3.0) -> dict[str, Any]:
    """Return {ok, url, models[], recommended_model, error?}."""
    url = (base_url or DEFAULT_OLLAMA_URL).rstrip("/")
    try:
        import httpx

        with httpx.Client(timeout=timeout) as client:
            resp = client.get(f"{url}/api/tags")
            resp.raise_for_status()
            data = resp.json()
        models: list[str] = []
        for m in data.get("models") or []:
            name = m.get("name") if isinstance(m, dict) else None
            if name:
                models.append(str(name))
        preferred = None
        for candidate in ("llama3.2", "llama3.1", "llama3", "mistral", "qwen2.5"):
            for name in models:
                if name == candidate or name.startswith(f"{candidate}:"):
                    preferred = name
                    break
            if preferred:
                break
        if preferred is None and models:
            preferred = models[0]
        return {
            "ok": bool(models),
            "url": url,
            "models": models,
            "recommended_model": preferred,
            "error": None if models else "Ollama responde pero no hay modelos",
        }
    except Exception as exc:  # noqa: BLE001
        return {
            "ok": False,
            "url": url,
            "models": [],
            "recommended_model": None,
            "error": str(exc),
        }


def _extract_json_object(text: str) -> dict[str, Any] | None:
    raw = (text or "").strip()
    if not raw:
        return None
    # Strip markdown fences if present
    fence = re.search(r"```(?:json)?\s*([\s\S]*?)```", raw, re.IGNORECASE)
    if fence:
        raw = fence.group(1).strip()
    try:
        data = json.loads(raw)
        return data if isinstance(data, dict) else None
    except json.JSONDecodeError:
        start = raw.find("{")
        end = raw.rfind("}")
        if start >= 0 and end > start:
            try:
                data = json.loads(raw[start : end + 1])
                return data if isinstance(data, dict) else None
            except json.JSONDecodeError:
                return None
    return None


def enrich_with_ollama(
    chapters: list[dict[str, Any]],
    chapter_texts: list[str],
    *,
    base_url: str,
    model: str,
    max_cards: int = DEFAULT_MAX_CARDS,
) -> tuple[list[dict[str, Any]], list[dict[str, str]], str | None]:
    """Ask Ollama for better titles + Q/A. Returns (chapters, qa, warning)."""
    import httpx

    # Cap payload size: first N chapters, truncated text
    payload_chapters = []
    for i, (ch, text) in enumerate(zip(chapters, chapter_texts)):
        if i >= 12:
            break
        payload_chapters.append(
            {
                "index": i,
                "start_sec": ch["start_sec"],
                "end_sec": ch["end_sec"],
                "title": ch.get("title"),
                "text": text[:1200],
            }
        )

    system = (
        "Sos un asistente de estudio. Respondé SOLO JSON válido, sin markdown. "
        'Esquema: {"chapters":[{"index":0,"title":"...","summary":"..."}],'
        '"cards":[{"chapter_index":0,"front":"...","back":"..."}]}'
    )
    user = (
        "Mejorá títulos/resúmenes de estos capítulos de una clase y generá "
        "3 a 5 flashcards (pregunta/respuesta) por capítulo, en español, "
        f"máximo {max_cards} cards en total.\n\n"
        + json.dumps(payload_chapters, ensure_ascii=False)
    )

    url = base_url.rstrip("/") + "/api/chat"
    try:
        with httpx.Client(timeout=OLLAMA_TIMEOUT_SEC) as client:
            resp = client.post(
                url,
                json={
                    "model": model,
                    "stream": False,
                    "format": "json",
                    "messages": [
                        {"role": "system", "content": system},
                        {"role": "user", "content": user},
                    ],
                },
            )
            resp.raise_for_status()
            body = resp.json()
        content = ""
        msg = body.get("message") if isinstance(body, dict) else None
        if isinstance(msg, dict):
            content = str(msg.get("content") or "")
        parsed = _extract_json_object(content)
        if not parsed:
            return chapters, [], "Ollama no devolvió JSON usable; se usó heurística"

        # Apply titles/summaries
        new_chapters = [dict(ch) for ch in chapters]
        for item in parsed.get("chapters") or []:
            if not isinstance(item, dict):
                continue
            try:
                idx = int(item["index"])
            except (KeyError, TypeError, ValueError):
                continue
            if 0 <= idx < len(new_chapters):
                title = str(item.get("title") or "").strip()
                summary = str(item.get("summary") or "").strip()
                if title:
                    new_chapters[idx]["title"] = title[:120]
                if summary:
                    new_chapters[idx]["summary"] = summary[:500]

        qa: list[dict[str, str]] = []
        for item in parsed.get("cards") or []:
            if len(qa) >= max_cards:
                break
            if not isinstance(item, dict):
                continue
            front = str(item.get("front") or "").strip()
            back = str(item.get("back") or "").strip()
            if not front or not back:
                continue
            start_sec = ""
            try:
                cidx = int(item.get("chapter_index"))
                if 0 <= cidx < len(new_chapters):
                    start_sec = str(new_chapters[cidx]["start_sec"])
            except (TypeError, ValueError):
                pass
            qa.append({"front": front, "back": back, "start_sec": start_sec})

        if not qa:
            return new_chapters, [], "Ollama no devolvió cards; cards heurísticas"
        return new_chapters, qa, None
    except Exception as exc:  # noqa: BLE001
        return chapters, [], f"Ollama falló ({exc}); se usó heurística"


def generate_study(
    segmentos_path: Path,
    out_dir: Path,
    *,
    title: str | None = None,
    ollama_url: str = DEFAULT_OLLAMA_URL,
    model: str | None = None,
    use_ollama: bool = True,
    gap_sec: float = DEFAULT_CHAPTER_GAP_SEC,
) -> dict[str, Any]:
    """Build outline + Open Cards artifacts next to the job transcript."""
    raw = json.loads(segmentos_path.read_text(encoding="utf-8"))
    segments = raw.get("segments") or []
    if not isinstance(segments, list) or not segments:
        raise ValueError("segmentos.json sin segmentos")

    deck_title = (title or str(raw.get("clase") or "Clase")).strip() or "Clase"
    curso = raw.get("curso")
    tags = [str(curso)] if curso else []

    # Build chapters with internal texts first
    usable_segs = [
        {
            "start": float(s["start"]),
            "end": float(s["end"]),
            "text": str(s.get("text") or "").strip(),
        }
        for s in segments
        if str(s.get("text") or "").strip()
        and "start" in s
        and "end" in s
    ]

    # Intermediate chapters keeping text
    interim: list[dict[str, Any]] = []
    current: dict[str, Any] | None = None
    for seg in usable_segs:
        if current is None:
            current = {
                "title": _title_from_text(seg["text"]),
                "start_sec": seg["start"],
                "end_sec": seg["end"],
                "text": seg["text"],
            }
            continue
        gap = seg["start"] - float(current["end_sec"])
        if gap > gap_sec and len(interim) + 1 < DEFAULT_MAX_CHAPTERS:
            interim.append(current)
            current = {
                "title": _title_from_text(seg["text"]),
                "start_sec": seg["start"],
                "end_sec": seg["end"],
                "text": seg["text"],
            }
        else:
            current["end_sec"] = seg["end"]
            current["text"] = f"{current['text']} {seg['text']}".strip()
    if current is not None:
        interim.append(current)

    chapter_texts = [c["text"] for c in interim]
    chapters = [
        {
            "title": c["title"],
            "start_sec": round(float(c["start_sec"]), 3),
            "end_sec": round(float(c["end_sec"]), 3),
            "summary": _first_sentences(c["text"]),
        }
        for c in interim
    ]

    mode = "heuristic"
    ollama_meta: dict[str, Any] = {"used": False, "model": None, "warning": None}
    cards_qa = build_extractive_qa(chapters, chapter_texts)

    if use_ollama:
        probe = probe_ollama(ollama_url)
        chosen = model or probe.get("recommended_model")
        if probe.get("ok") and chosen:
            enriched_ch, enriched_qa, warning = enrich_with_ollama(
                chapters,
                chapter_texts,
                base_url=ollama_url,
                model=str(chosen),
            )
            chapters = enriched_ch
            if enriched_qa:
                cards_qa = enriched_qa
                mode = "ollama"
                ollama_meta = {
                    "used": True,
                    "model": chosen,
                    "warning": warning,
                }
            else:
                cards_qa = build_extractive_qa(chapters, chapter_texts)
                ollama_meta = {
                    "used": False,
                    "model": chosen,
                    "warning": warning or "Sin cards de Ollama; cards heurísticas",
                }
        else:
            ollama_meta = {
                "used": False,
                "model": chosen,
                "warning": probe.get("error")
                or "Ollama no disponible — outline/cards heurísticos",
            }

    out_dir.mkdir(parents=True, exist_ok=True)
    outline = {
        "mode": mode,
        "clase": deck_title,
        "chapters": chapters,
        "ollama": ollama_meta,
    }
    outline_path = out_dir / "outline.json"
    outline_path.write_text(
        json.dumps(outline, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    write_outline_md(out_dir / "outline.md", chapters, title=deck_title)

    library = to_open_cards_library(
        deck_name=deck_title,
        cards_qa=cards_qa,
        description=f"Generado por Cynta ({mode}) desde la transcripción",
        tags=tags,
    )
    # Attach study meta without breaking Open Cards schema consumers:
    # keep file pure open-cards; meta lives in outline.json
    oc_path = out_dir / "open-cards.json"
    oc_path.write_text(
        json.dumps(library, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    deck = library["decks"][0]
    return {
        "mode": mode,
        "outline": outline,
        "deck": {
            "name": deck.get("name"),
            "cards_count": len(deck.get("cards") or []),
            "tags": deck.get("tags") or [],
        },
        "ollama": ollama_meta,
        "paths": {
            "outline": str(outline_path),
            "outline_md": str(out_dir / "outline.md"),
            "opencards": str(oc_path),
        },
    }
