from app.rag.retriever import RetrieverService

retriever = RetrieverService()

docs = retriever.search(
    "¿Cómo eliminar agua verde?"
)

for i, doc in enumerate(docs, start=1):

    print("=" * 80)
    print(f"Resultado {i}")
    print("=" * 80)

    print(doc.page_content[:600])

    print("\nMetadata:")

    print(doc.metadata)