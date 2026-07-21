import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))

from app.rag.loader import PDFLoader
from app.rag.chunker import DocumentChunker
from app.rag.embeddings import EmbeddingService
from app.rag.vector_store import VectorStoreService


print("Cargando PDFs...")

documents = PDFLoader().load()

print(f"Documentos cargados: {len(documents)}")

chunks = DocumentChunker().split(documents)

print(f"Chunks generados: {len(chunks)}")

embeddings = EmbeddingService().get()

db = VectorStoreService(embeddings)

db.create(chunks)

print("Índice FAISS creado correctamente.")