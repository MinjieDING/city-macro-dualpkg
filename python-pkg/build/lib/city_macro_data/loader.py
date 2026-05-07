from __future__ import annotations

import json
from importlib.resources import files

import pandas as pd


def load_data() -> pd.DataFrame:
    data_path = files("city_macro_data.data").joinpath("city_macro.csv")
    return pd.read_csv(data_path)


def get_metadata() -> dict:
    meta_path = files("city_macro_data.data").joinpath("metadata.json")
    return json.loads(meta_path.read_text(encoding="utf-8"))


def data_version() -> str:
    return str(get_metadata()["data_version"])


def validate_data(required_columns: list[str] | None = None) -> bool:
    df = load_data()
    if df.empty:
        raise ValueError("Dataset is empty.")

    cols = required_columns or ["年份", "城市"]
    missing = [c for c in cols if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    return True
