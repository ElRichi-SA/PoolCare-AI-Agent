from pydantic import BaseModel

class Consultation(BaseModel):
    volumen: float
    ph: float
    cloro: float
    alcalinidad: float
    aspecto: str
    temperatura: float | None = None