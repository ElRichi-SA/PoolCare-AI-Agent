from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]
CSV_DIR = BASE_DIR / "data" / "csv"


class CSVRepository:

    @staticmethod
    def cargar(nombre_archivo: str):

        ruta = CSV_DIR / nombre_archivo

        return pd.read_csv(ruta)