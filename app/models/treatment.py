from pydantic import BaseModel

class Treatment(BaseModel):
    producto: str
    cantidad: float
    unidad: str
    procedimiento: str