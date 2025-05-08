from fastapi import APIRouter
from api.services.embedding import meta_data_store
from api.services.analysis import generate_summary

router = APIRouter(prefix="/analyze", tags=["analysis"])

@router.get("/summary/{doc_title}")
def get_summary_and_scores(doc_title: str):
    # 업로드 시 저장된 청크 기반 메타데이터 필터링
    chunks = []
    for meta in meta_data_store:
        if meta["doc_title"] == doc_title:
            content = meta.get("chunk_text", "")
            
            # subsection들을 붙여서 하나의 큰 텍스트로 확장
            for sub in meta.get("subsections", []):
                subtitle = sub.get("subtitle", "")
                subcontent = sub.get("content", "")
                if subtitle or subcontent:
                    content += f"\n\n{subtitle}\n{subcontent}"

            # 빈 내용은 제외
            if content.strip():
                chunks.append({
                    "section_title": meta.get("section_title", ""),
                    "content": content,
                    "subsections": []  # 이미 붙였기 때문에 안 써도 됨
                })

    if not chunks:
        return {"error": "해당 문서가 존재하지 않거나 아직 분석되지 않았습니다."}

    summary = generate_summary(chunks)

    return {
        "summary": summary
    }
