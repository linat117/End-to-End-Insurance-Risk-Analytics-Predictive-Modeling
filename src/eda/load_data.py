# src/eda/load_data.py
import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[2] / "data"

def load_csv(filename: str) -> pd.DataFrame:
    """Load a CSV from the data directory and return a DataFrame."""
    path = DATA_DIR / filename
    return pd.read_csv(path)
