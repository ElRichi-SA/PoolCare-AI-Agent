from pathlib import Path
from langchain_community.document_loaders import PyPDFDirectoryLoader

PDF_PATH = Path("data/pdf/fichas_tecnicas")


class PDFLoader:

    def load(self):
        loader = PyPDFDirectoryLoader(PDF_PATH)
        return loader.load()