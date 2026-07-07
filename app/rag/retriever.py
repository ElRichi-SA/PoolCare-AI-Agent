from app.rag.embeddings import EmbeddingService
from app.rag.vector_store import VectorStoreService


class RetrieverService:

    def __init__(self):

        embeddings = EmbeddingService().get()

        self.db = VectorStoreService(embeddings).load()

    def search(self, question, k=4):

        docs = self.db.similarity_search(
            question,
            k=k
        )

        return docs