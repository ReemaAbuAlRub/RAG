import faiss
import numpy as np

class VectorStore:
    def __init__(self, embedding_dim: int):
        self.index = faiss.IndexFlatL2(embedding_dim)
        self.documents = []

    def chunk_document(self, doc_text: str):
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        return text_splitter.split_document(doc_text)

    def add_document(self, embedding: np.ndarray, doc_text: str):
        if embedding.ndim == 1:
            embedding = embedding.reshape(1, -1)
        embedding = embedding.astype(np.float32)
        self.index.add(embedding)
        self.documents.append(doc_text)


    def search(self, query_embedding: np.ndarray, top_k: int = 5) -> list:
        if query_embedding.ndim == 1:
            query_embedding = query_embedding.reshape(1, -1)

        query_embedding = query_embedding.astype(np.float32)
        _, indices = self.index.search(query_embedding, top_k)
        results = []
        
        for i in indices[0]:
            if 0 <= i < len(self.documents):
                results.append(self.documents[i])
            else:
                print(f"Index {i} is out of range for documents list.")
        
        return results
