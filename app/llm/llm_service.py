from google import genai

from app.core.config import settings


class LLMService:

    def __init__(self):

        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

    def generate(self, prompt: str) -> str:

        try:

            response = self.client.models.generate_content(
                model=settings.GEMINI_MODEL,
                contents=prompt
            )

            return response.text

        except Exception as e:

            return (
                "No fue posible generar una recomendación "
                f"automática.\n\nDetalle: {e}"
            )