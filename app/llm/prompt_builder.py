class PromptBuilder:

    def build(
        self,
        consulta,
        diagnosticos,
        tratamientos,
        documentos
    ):

        contexto = ""

        for doc in documentos:
            contexto += doc["content"]
            contexto += "\n\n"

        texto = f"""
Eres un consultor profesional especializado en mantenimiento de piscinas.

Consulta del cliente:

{consulta}

Diagnósticos detectados:

{diagnosticos}

Tratamientos calculados:

{tratamientos}

Información técnica obtenida del manual:

{contexto}

Genera una respuesta profesional.

No inventes tratamientos.

No cambies las cantidades calculadas.

Explica el procedimiento paso a paso.
"""

        return texto