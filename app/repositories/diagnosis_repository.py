from pathlib import Path
import pandas as pd


class DiagnosisRepository:

    def __init__(self):
        self.csv_path = Path("data/csv/diagnosticos.csv")

    def get_rules(self):
        return pd.read_csv(self.csv_path)