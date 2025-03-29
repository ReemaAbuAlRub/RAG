from fastapi import FastAPI
from  api.endpoints import upload, query
import uvicorn

app = FastAPI(title="RAG Application API")

app.include_router(upload.router, prefix="/api", tags=["upload"])
app.include_router(query.router, prefix="/api", tags=["query"])

if __name__ == "__main__":
    
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)