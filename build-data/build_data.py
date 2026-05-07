from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA_SRC = ROOT / "data-src" / "city_macro.xlsx"
DIST_DIR = ROOT / "dist-data"
DIST_CSV = DIST_DIR / "city_macro.csv"
DIST_META = DIST_DIR / "metadata.json"


def build() -> None:
    if not DATA_SRC.exists():
        raise FileNotFoundError(
            f"Missing source Excel: {DATA_SRC}. Put your file in data-src/ and rename to city_macro.xlsx."
        )

    df = pd.read_excel(DATA_SRC)
    DIST_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(DIST_CSV, index=False, encoding="utf-8-sig")

    metadata = {
        "data_version": datetime.now().strftime("%Y.%m"),
        "build_time_utc": datetime.now(timezone.utc).isoformat(),
        "source_file": DATA_SRC.name,
        "row_count": int(df.shape[0]),
        "column_count": int(df.shape[1]),
        "columns": list(df.columns),
    }
    DIST_META.write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Built data -> {DIST_CSV}")
    print(f"Built metadata -> {DIST_META}")


if __name__ == "__main__":
    build()
