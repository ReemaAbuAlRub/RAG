from backend.app.core.services.document_service import DocumentService
from backend.app.core.services.rag_service import RagService

document_service = DocumentService()
rag_service = RagService(document_service)


