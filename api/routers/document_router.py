from fastapi import APIRouter, UploadFile, File
from api.services.chunking import extract_chunks_from_pdf_upload
from api.services.embedding import embed_and_index

router = APIRouter(prefix="/process-document", tags=["document"])

@router.post("/upload")
async def process_uploaded_pdf(file: UploadFile = File(...)):
    # 1. 문서에서 청크 추출
    chunks = extract_chunks_from_pdf_upload(file)

    # 2. 파일명에서 문서 이름 추출 (확장자 제거)
    doc_title = file.filename.rsplit(".", 1)[0]

    # 3. 벡터 임베딩 및 저장
    embed_and_index(chunks, doc_title)

    # 4. 일부 결과만 반환 (임시 디버깅용)
    return {
        "doc_title": doc_title,
        "num_chunks": len(chunks),
        "chunks": chunks[:3]
    }
