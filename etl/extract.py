import pandas as pd
from pathlib import Path


def extract_csv(file_path: str) -> pd.DataFrame:
    """
    Extract raw transaction data from CSV.
    No validation or cleaning happens here.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"[EXTRACT ERROR] File not found: {file_path}")

    try:
        df = pd.read_csv(path)
        print(f"[EXTRACT] Loaded {len(df)} records from {file_path}")
        return df

    except Exception as e:
        raise RuntimeError(f"[EXTRACT ERROR] CSV read failed: {e}")
