from pathlib import Path

def get_project_root() -> Path:
    """
    Find project root by looking for a marker folder (e.g., 'data')
    """
    current = Path().resolve()

    for parent in [current] + list(current.parents):
        if (parent / "data").exists() and (parent / "notebooks").exists():
            return parent

    raise RuntimeError("Project root not found")

PROJECT_ROOT = get_project_root()

DATA_DIR = PROJECT_ROOT / "data"
PROCESSED_DIR = DATA_DIR / "processed"
RAW_DIR = DATA_DIR / "raw"
RESULT_DIR = DATA_DIR / "result"