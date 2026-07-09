from app.repositories.consultation_repository import ConsultationRepository


class HistoryService:

    def __init__(self):

        self.repository = ConsultationRepository()

    def save(
        self,
        data,
        diagnosticos,
        tratamientos,
        respuesta
    ):

        self.repository.save(
            data,
            diagnosticos,
            tratamientos,
            respuesta
        )