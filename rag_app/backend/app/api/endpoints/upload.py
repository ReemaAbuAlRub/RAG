from fastapi import APIRouter, UploadFile, File, HTTPException
from ...dependencies import document_service 
import numpy as np 

router = APIRouter()

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    try:
        result = await document_service.upload_document(file)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
