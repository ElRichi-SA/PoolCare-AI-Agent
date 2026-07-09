from app.services.diagnosis_service import DiagnosisService
from app.services.treatment_service import TreatmentService
from app.services.calculation_service import CalculationService

from app.rag.retriever import RetrieverService

from app.llm.prompt_builder import PromptBuilder
from app.llm.llm_service import LLMService

class ConsultationService:

    @staticmethod
    def process(data):

        diagnosis_service = DiagnosisService()
        treatment_service = TreatmentService()
        calculation_service = CalculationService()

        retriever = RetrieverService()
        prompt_builder = PromptBuilder()
        llm = LLMService()

        # =====================================
        # 1. Diagnóstico
        # =====================================

        diagnosticos = diagnosis_service.analyze(data)

        # =====================================
        # 2. Tratamientos
        # =====================================

        tratamientos = treatment_service.build(
            diagnosticos
        )

        # =====================================
        # 3. Dosificación
        # =====================================

        tratamientos = calculation_service.calculate(
            data.volumen,
            tratamientos
        )

        # =====================================
        # 4. Consulta para el RAG
        # =====================================

        query = " ".join(
            f"{d.get('diagnostico', '')} {d.get('codigo_tratamiento', '')}"
            for d in diagnosticos
        )

        # =====================================
        # 5. Recuperación de documentos
        # =====================================

        documentos = retriever.search(query)

        # =====================================
        # 6. Construcción del Prompt
        # =====================================

        prompt = prompt_builder.build(
            consulta=query,
            diagnosticos=diagnosticos,
            tratamientos=tratamientos,
            documentos=documentos
        )

        # =====================================
        # 7. Generación con LLM
        # =====================================

        respuesta = llm.generate(prompt)
        
        # =====================================
        # 8. Respuesta
        # =====================================

        return {
            "diagnosticos": diagnosticos,
            "tratamientos": tratamientos,
            "respuesta": respuesta
        }