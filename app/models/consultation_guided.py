from pydantic import BaseModel


class GuidedConsultation(BaseModel):

    volumen: float
    ph: float
    cloro: float
    alcalinidad: float
    aspecto: str
    temperatura: float | None = None