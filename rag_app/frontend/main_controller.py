from api_client import upload_document, query_llm

def handle_upload(file) -> dict:
    return upload_document(file)

def handle_query(query_text: str, top_k: int) -> dict:
    return query_llm(query_text, top_k)
