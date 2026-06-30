from pydantic import BaseModel


class ConsultationRequest(BaseModel):
    modo: str
    consulta: str | None = None
    volumen: float | None = None
    ph: float | None = None
    cloro: float | None = None
    alcalinidad: float | None = None