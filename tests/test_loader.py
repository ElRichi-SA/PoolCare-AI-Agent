from app.rag.loader import PDFLoader


def test_pdf_loader():

    loader = PDFLoader()

    docs = loader.load()

    assert len(docs) > 0