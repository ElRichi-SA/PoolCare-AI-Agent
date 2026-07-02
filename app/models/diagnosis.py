from pydantic import BaseModel

class Diagnosis(BaseModel):

    parametro: str

    diagnostico: str

    severidad: str

    producto: int

    procedimiento: int

    mensaje: str