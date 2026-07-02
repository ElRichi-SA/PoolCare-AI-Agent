from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DATA_DIR = BASE_DIR / "data"

CSV_DIR = DATA_DIR / "csv"

PDF_DIR = DATA_DIR / "pdf"

JSON_DIR = DATA_DIR / "json"