from app.llm.llm_service import LLMService

llm = LLMService()

respuesta = llm.generate(
    "Explica brevemente qué es el pH en una alberca."
)

print(respuesta)