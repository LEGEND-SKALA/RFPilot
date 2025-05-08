from typing import List
from fastapi import APIRouter
from api.schemas.request import ChunkRequest, Chunk
from api.services.chunking import chunk_document_by_section

router = APIRouter(
    prefix="/chunk",
    tags=["chunking"]
)

@router.post("/", response_model=List[Chunk])
def chunk_rfp_doc(req: ChunkRequest):
    return chunk_document_by_section(req.file_path)
