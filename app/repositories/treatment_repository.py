from app.core.knowledge_service import knowledge


class TreatmentRepository:

    def get_all(self):
        return knowledge.get_treatments()

    def get_products(self):
        return knowledge.get_products()

    def get_procedures(self):
        return knowledge.get_procedures()