from pydantic import BaseModel, Field


class ConsultationResponse(BaseModel):

    success: bool = True

    diagnosticos: list = Field(default_factory=list)

    tratamientos: list = Field(default_factory=list)

    respuesta_llm: str = ""

    version: str = "0.9.1"