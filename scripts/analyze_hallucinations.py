"""Quick diagnostics for repetitive ASR hallucinations."""
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from transcribe.export import is_hallucinated_segment  # noqa: E402


def main() -> int:
    path = Path(
        sys.argv[1]
        if len(sys.argv) > 1
        else ROOT / "Transcripciones" / "Clase 1" / "segmentos.json"
    )
    data = json.loads(path.read_text(encoding="utf-8"))
    segs = data["segments"]
    bad = [(i, s) for i, s in enumerate(segs) if is_hallucinated_segment(s.get("text", ""))]
    print(f"file={path}")
    print(f"total={len(segs)} hallucinated={len(bad)}")
    if bad:
        i, s = bad[0]
        print(f"first_bad_idx={i} start={s['start']:.1f} text={s['text'][:80]!r}")
    # token spam summary
    counts: Counter[str] = Counter()
    for _, s in bad:
        toks = re.findall(r"\S+", s.get("text", ""))
        counts.update(toks[:3])
    print("top_bad_tokens=", counts.most_common(5))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
