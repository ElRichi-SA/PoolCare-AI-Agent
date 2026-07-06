from pathlib import Path
import pandas as pd
from app.core.knowledge_service import knowledge

class DiagnosisRepository:

    def __init__(self):
        self.csv_path = Path("data/csv/diagnosticos.csv")

    def get_rules(self):
        return pd.read_csv(self.csv_path)
    
class DiagnosisRepository:

    def get_all_rules(self):
        return knowledge.get_diagnosis_rules()