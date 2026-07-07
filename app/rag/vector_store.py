from langchain_community.vectorstores import FAISS


class VectorStoreService:

    def __init__(self, embeddings):
        self.embeddings = embeddings

    def create(self, documents):

        db = FAISS.from_documents(
            documents,
            self.embeddings
        )

        db.save_local("vectorstore")

        return db

    def load(self):

        return FAISS.load_local(
            "vectorstore",
            self.embeddings,
            allow_dangerous_deserialization=True
        )