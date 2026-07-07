from app.llm.prompt_builder import PromptBuilder


def test_prompt():

    builder = PromptBuilder()

    prompt = builder.build(
        consulta="El agua está verde",
        diagnosticos=["Agua verde"],
        tratamientos=[
            {
                "producto": "Hipoclorito",
                "cantidad": 2500,
                "unidad": "ml"
            }
        ],
        documentos=[
            {
                "content": "Aplicar hipoclorito lentamente..."
            }
        ]
    )

    assert "Agua verde" in prompt