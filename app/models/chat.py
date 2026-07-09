class ChatRequest(BaseModel):

    session_id: str

    consulta: str

    volumen: float | None = None

    ph: float | None = None

    cloro: float | None = None

    alcalinidad: float | None = None