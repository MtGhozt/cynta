from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "Transcripciones"


def main() -> None:
    folders = sorted(
        ROOT.glob("Clase *"),
        key=lambda p: int(re.search(r"\d+", p.name).group()),
    )
    for folder in folders:
        md = folder / "transcripcion.md"
        js = folder / "segmentos.json"
        if not md.exists() or not js.exists():
            print(f"{folder.name}: MISSING")
            continue
        data = json.loads(js.read_text(encoding="utf-8"))
        segs = data["segments"]
        end = segs[-1]["end"] / 60 if segs else 0.0
        pero = sum(1 for s in segs if s.get("text", "").count("Pero...") >= 4)
        print(
            f"{folder.name}: segs={len(segs)} "
            f"cover={end:.1f}min "
            f"audio={data.get('duration_sec', 0)/60:.1f}min "
            f"md_kb={md.stat().st_size/1024:.1f} "
            f"pero_loops={pero}"
        )


if __name__ == "__main__":
    main()
