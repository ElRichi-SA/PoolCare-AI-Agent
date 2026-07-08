class LLMService:

    def generate(self, prompt: str) -> str:

        return (
            "=== RESPUESTA GENERADA POR EL LLM ===\n\n"
            + prompt[:700]
        )