import pandas as pd
from pathlib import Path

def set_gridcode_to_zero(csv_path: Path) -> None:
    df = pd.read_csv(csv_path)
    if "gridcode" not in df.columns:
        raise ValueError("Column 'gridcode' not found in CSV")
    df["gridcode"] = 0
    df.to_csv(csv_path, index=False)

if __name__ == "__main__":
    csv_file = Path("data/raw/flood/so.csv")
    set_gridcode_to_zero(csv_file)