from app.rag.retriever import RetrieverService


def test_rag_search():

    retriever = RetrieverService()

    docs = retriever.search(
        "¿Cómo eliminar agua verde?"
    )

    assert len(docs) > 0