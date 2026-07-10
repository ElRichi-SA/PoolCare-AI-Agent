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

Genera la respuesta usando EXACTAMENTE este formato Markdown:

# Diagnóstico

Breve resumen del estado del agua.

# Productos

| Producto | Cantidad |
|----------|----------|
| ... | ... |

# Procedimiento

1.
2.
3.

# Recomendaciones

- ...
- ...
- ...
"""

        return prompt