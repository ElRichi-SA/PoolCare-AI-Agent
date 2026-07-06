import pandas as pd

from app.core.config import CSV_DIR


class KnowledgeService:

    def get_products(self):
        return self.products
    def get_diagnosis_rules(self):
        return self.diagnosis
    def get_treatments(self):
        return self.treatments
    def get_dosages(self):
        return self.dosages
    def get_procedures(self):
        return self.procedures

    def load(self):

        self.products = pd.read_csv(CSV_DIR / "productos.csv")

        self.diagnosis = pd.read_csv(CSV_DIR / "diagnosticos.csv")

        self.treatments = pd.read_csv(CSV_DIR / "tratamientos.csv")

        self.dosages = pd.read_csv(CSV_DIR / "dosificaciones.csv")

        self.procedures = pd.read_csv(CSV_DIR / "procedimientos.csv")
        
knowledge = KnowledgeService()