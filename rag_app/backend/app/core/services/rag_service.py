import numpy as np
import openai
from openai import OpenAI
from backend.app.config import config

class RagService:

    def __init__(self, document_service, normalize_embeddings: bool = True):
        self.document_service = document_service
        self.embeddings = self.document_service.embeddings 
        self.normalize_embeddings = normalize_embeddings
        self.client = OpenAI(api_key=config.api_key)
        print("API KEY: ",config.api_key)
        self.model=config.model

    @staticmethod
    def normalize(self, v: np.ndarray) -> np.ndarray:
        norm = np.linalg.norm(v)
        return v / norm if norm > 0 else v

    def get_prompt(self,context_text:str,query_text:str) -> str:
        prompt = (
                f"Using the context below, answer the following question concisely.\n\n"
                f"Do not answer questions outside the context always respond to them with Out of Context.\n\n"
                f"Context:\n{context_text}\n\n"
                f"Question: {query_text}\n\n"
                f"Answer:"
        )
        return prompt

    def generate_response(self, prompt: str) -> dict:
        if not self.client:
            raise ValueError("OpenAI client not initialized.")
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response

    def query(self, query_text: str, top_k: int = 5) -> dict:
        try:
            query_embedding = self.embeddings.embed_query(query_text)
            query_embedding = np.array(query_embedding, dtype=np.float32)
            
            # if self.normalize_embeddings:
            #     query_embedding = self.normalize(query_embedding)
        
            retrieved_docs = self.document_service.vector_store.search(query_embedding, top_k)

            if not retrieved_docs:
                return {"query": query_text, "retrieved_documents": [], "message": "No documents found."}
            
            context_text = "\n\n".join(retrieved_docs)
            
            prompt=self.get_prompt(context_text,query_text)
            response=self.generate_response(prompt)
            final_answer = response.choices[0].message.content.strip()

        except Exception as e:
            return {"query": query_text, "message": f"Error generating answer: {e}"}
        
        return {"query": query_text, "answer": final_answer}
