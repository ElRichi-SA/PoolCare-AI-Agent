import pandas as pd

from app.core.config import CSV_DIR


class KnowledgeService:

    def __init__(self):
        self.products = None
        self.diagnosis = None
        self.treatments = None
        self.dosages = None
        self.procedures = None

    def load(self):

        self.products = pd.read_csv(CSV_DIR / "productos.csv")

        self.diagnosis = pd.read_csv(CSV_DIR / "diagnosticos.csv")

        self.treatments = pd.read_csv(CSV_DIR / "tratamientos.csv")

        self.dosages = pd.read_csv(CSV_DIR / "dosificaciones.csv")

        self.procedures = pd.read_csv(CSV_DIR / "procedimientos.csv")
        
knowledge = KnowledgeService()