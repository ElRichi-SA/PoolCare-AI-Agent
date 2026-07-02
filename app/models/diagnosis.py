from pydantic import BaseModel

class Diagnosis(BaseModel):
    parametro: str
    diagnostico: str
    severidad: str
    codigo_tratamiento: str
    mensaje: str