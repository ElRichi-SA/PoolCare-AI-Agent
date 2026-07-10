from app.services.diagnosis_service import DiagnosisService
from app.services.treatment_service import TreatmentService
from app.services.calculation_service import CalculationService

from app.rag.retriever import RetrieverService

from app.llm.prompt_builder import PromptBuilder
from app.llm.llm_service import LLMService

from app.models.response import ConsultationResponse


class ConsultationService:

    @staticmethod
    def process_free(data):

        retriever = RetrieverService()
        prompt_builder = PromptBuilder()
        llm = LLMService()

        documentos = retriever.search(
            data.consulta
        )

        prompt = prompt_builder.build(
            consulta=data.consulta,
            diagnosticos=[],
            tratamientos=[],
            documentos=documentos
        )

        respuesta = llm.generate(prompt)

        return ConsultationResponse(
            diagnosticos=[],
            tratamientos=[],
            respuesta_llm=respuesta
        )

    @staticmethod
    def process_guided(data):

        diagnosis_service = DiagnosisService()
        treatment_service = TreatmentService()
        calculation_service = CalculationService()

        retriever = RetrieverService()
        prompt_builder = PromptBuilder()
        llm = LLMService()

        diagnosticos = diagnosis_service.analyze(data)

        tratamientos = treatment_service.build(
            diagnosticos
        )

        tratamientos = calculation_service.calculate(
            data.volumen,
            tratamientos
        )

        consulta = ", ".join(
            d["diagnostico"]
            for d in diagnosticos
        )

        documentos = retriever.search(
            consulta
        )

        prompt = prompt_builder.build(
            consulta=consulta,
            diagnosticos=diagnosticos,
            tratamientos=tratamientos,
            documentos=documentos
        )

        respuesta = llm.generate(prompt)

        return ConsultationResponse(
            diagnosticos=diagnosticos,
            tratamientos=tratamientos,
            respuesta_llm=respuesta
        )