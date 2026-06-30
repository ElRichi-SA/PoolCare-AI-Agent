from fastapi import APIRouter

from app.models.consultation import ConsultationRequest
from app.services.consultation_service import ConsultationService

router = APIRouter()


@router.get("/health")
def health():
    return {
        "status": "ok",
        "service": "PoolCare AI"
    }


@router.post("/consultar")
def consultar(data: ConsultationRequest):

    return ConsultationService.process(data)