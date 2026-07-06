from app.services.diagnosis_service import DiagnosisService
from app.services.treatment_service import TreatmentService
from app.services.calculation_service import CalculationService


class ConsultationService:

    @staticmethod
    def process(data):

        diagnosis_service = DiagnosisService()
        treatment_service = TreatmentService()
        calculation_service = CalculationService()

        diagnostics = diagnosis_service.analyze(data)

        tratamientos = treatment_service.build(diagnostics)

        calculation_service = CalculationService()
        
        tratamientos  = calculation_service.calculate(
            data.volumen,
            tratamientos
        )
        
        return {
            "estado": "ok",
            "datos_recibidos": data.model_dump(),
            "diagnosticos": diagnostics,
            "tratamientos": tratamientos,
            "respuesta_llm": ""
        }