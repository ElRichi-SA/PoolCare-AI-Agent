from fastapi import APIRouter

from app.models.consultation import Consultation
from app.services.consultation_service import ConsultationService

router = APIRouter()


@router.get("/health")
def health():
    return {
        "status": "ok",
        "service": "PoolCare AI"
    }


@router.post("/consultar")
def consultar(data: Consultation):

    return ConsultationService.process(data)

@router.get("/version")
def version():

    return {

        "version":"1.0.0",

        "backend":"FastAPI",

        "estado":"Operativo"

    }
    
@router.get("/historial")
def historial():

    return history_service.get_all()