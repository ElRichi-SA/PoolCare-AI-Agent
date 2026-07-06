from app.core.knowledge_service import knowledge


class CalculationRepository:

    def get_dosages(self):
        return knowledge.get_dosages()