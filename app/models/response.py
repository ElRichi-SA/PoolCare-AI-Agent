from pydantic import BaseModel

class ConsultationResponse(BaseModel):

    diagnosticos: list

    tratamientos: list

    respuesta_llm: str = ""