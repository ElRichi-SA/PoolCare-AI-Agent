from fastapi import APIRouter

from app.models.consultation_free import FreeConsultation
from app.models.consultation_guided import GuidedConsultation
from app.services.consultation_service import ConsultationService

from app.models.response import ConsultationResponse

router = APIRouter(
    prefix=""
)


@router.get(
    "/health",
    tags=["Sistema"]
)
def health():
    return {
        "status": "ok",
        "service": "PoolCare AI"
    }


@router.post(
    "/consultar",
    response_model=ConsultationResponse,
    tags=["Consultas"]
)
def consultar(data: FreeConsultation):

    return ConsultationService.process_free(data)

@router.post(
    "/analizar",
    response_model=ConsultationResponse,
    tags=["Consultas"]
)
def analizar(data: GuidedConsultation):

    return ConsultationService.process_guided(data)

@router.get(
    "/version-info",
    tags=["Sistema"]
)
def version():

    return {
        "application": "PoolCare AI",
        "version":"0.9.1",
        "backend":"FastAPI",
        "llm": "Gemini",
        "rag": True,
        "estado":"Operativo"
    }
    
#@router.get(
#    "/historial",
#    tags=["Consultas"]
#)
#def historial():
#
#   return history_service.get_all()