from fastapi import APIRouter, HTTPException, Query
from  dependencies import rag_service


router = APIRouter()

@router.get("/query")
def query_llm(q: str = Query(..., description="User query text"), top_k: int = 5):
    try:
        result = rag_service.query(q, top_k)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
