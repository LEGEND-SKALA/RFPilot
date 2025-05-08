from api.services.embedding import meta_data_store, embedding_model
import numpy as np
import faiss

# 사전 정의된 RFP 평가 기준 (카테고리별 키워드)
rfp_criteria = {
    "기술": "이 프로젝트에 적용될 기술은 무엇이며, 기술 수준은 적절한가?",
    "일정": "사업 수행 일정은 현실적이며 구체적인가?",
    "예산": "예산 계획은 적절하고 세부적으로 작성되었는가?",
    "목표부합성": "사업 목적과 제안 내용이 잘 부합하는가?"
}

def analyze_fit(doc_title: str, top_k: int = 5) -> dict:
    chunks = [m for m in meta_data_store if m["doc_title"] == doc_title]
    if not chunks:
        return {k: 0 for k in rfp_criteria.keys()}

    # 텍스트 및 임베딩 추출
    chunk_texts = [m["chunk_text"] for m in chunks]
    chunk_vecs = embedding_model.embed_documents(chunk_texts)
    chunk_vecs = np.array(chunk_vecs, dtype="float32")

    # FAISS 인덱스 구축
    index = faiss.IndexFlatL2(chunk_vecs.shape[1])
    index.add(chunk_vecs)

    scores = {}
    for category, prompt in rfp_criteria.items():
        query_vec = embedding_model.embed_query(prompt)
        query_vec = np.array([query_vec], dtype="float32")

        D, _ = index.search(query_vec, top_k)
        mean_dist = float(np.mean(D))
        
        # 유사도 계산 (1 - 거리), 단 음수 방지
        similarity = max(0.0, 1.0 - mean_dist)
        scores[category] = round(similarity * 100)

        # 디버깅 로그 (필요 시 주석 처리)
        print(f"[{category}] 평균 거리: {mean_dist:.4f}, 유사도: {similarity:.4f}")

    return scores