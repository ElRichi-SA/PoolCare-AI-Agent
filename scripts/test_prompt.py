from app.llm.prompt_builder import PromptBuilder

builder = PromptBuilder()

prompt = builder.build(
    consulta="Mi piscina tiene agua verde.",
    diagnosticos=["Agua verde"],
    tratamientos=[
        {
            "producto": "Hipoclorito de Sodio 13%",
            "cantidad": 2500,
            "unidad": "ml"
        }
    ],
    documentos=[
        {
            "content": "Después de aplicar el producto mantenga la filtración durante ocho horas."
        }
    ]
)

print(prompt)