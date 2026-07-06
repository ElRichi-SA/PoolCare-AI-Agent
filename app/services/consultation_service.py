from app.services.diagnosis_service import DiagnosisService


class ConsultationService:

    @staticmethod
    def process(data):

        diagnosis_service = DiagnosisService()

        diagnostics = diagnosis_service.analyze(data)

        return {
            "estado": "ok",
            "datos_recibidos": data.model_dump(),
            "diagnosticos": diagnostics,
            "tratamientos": [],
            "respuesta_llm": ""
        }