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
            contexto += doc.page_content
            contexto += "\n\n"

        prompt = f"""
Consulta:
{consulta}

Diagnósticos:
{diagnosticos}

Tratamientos:
{tratamientos}

Información técnica:

{contexto}

Con base únicamente en la información anterior, genera una recomendación profesional para el mantenimiento de la alberca.
"""

        return prompt