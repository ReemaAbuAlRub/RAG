from fastapi import UploadFile
from adapters.vector_store import VectorStore
import io
from langchain_openai import OpenAIEmbeddings
from PyPDF2 import PdfReader
import numpy as np 
from config import config

class DocumentService:

    def __init__(self,embedding_dim: int = 1536, normalize_embeddings: bool = True) -> None:
        self.embeddings = OpenAIEmbeddings(openai_api_key= config.api_key)
        self.embedding_dim = embedding_dim
        self.vector_store = VectorStore(self.embedding_dim)
        self.normalize_embeddings = normalize_embeddings
    
    @staticmethod
    def normalize(self,v: np.ndarray) -> np.ndarray:
        norm = np.linalg.norm(v)
        return v / norm if norm > 0 else v

    async def upload_document(self, file: UploadFile) -> dict:
        if file.filename.lower().endswith('.pdf'):
            content = await file.read()
            reader = PdfReader(io.BytesIO(content))
            text = ""
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        else:
            content = await file.read()
            try:
                text = content.decode("utf-8")

            except UnicodeDecodeError:
                return {"status": "error", "message": "Unsupported file encoding."}

        embedding_list = self.embeddings.embed_documents([text])
        embedding_array = np.array(embedding_list, dtype=np.float32)
        embedding = embedding_array[0]

        # if self.normalize_embeddings:
        #     embedding = self.normalize(embedding)

        self.vector_store.add_document(embedding, text)
        return {"status": "success", "message": "Document uploaded and stored."}