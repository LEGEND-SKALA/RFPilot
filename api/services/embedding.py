from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# LangChain 호환 Embedding 객체
embedding_model = HuggingFaceEmbeddings(model_name="snunlp/KR-SBERT-V40K-klueNLI-augSTS")

# 벡터 DB 저장 경로
vector_db_path = "faiss_store"

# 메타데이터 저장소
meta_data_store = []

#벡터디비에 저장 
def embed_chunks(text_list: list[str], doc_title: str):
    db = FAISS.from_texts(text_list, embedding=embedding_model)
    db.save_local(f"{vector_db_path}/{doc_title}")

    for i, text in enumerate(text_list):
        meta_data_store.append({
            "doc_title": doc_title,
            "chunk_text": text,
            "index": i
        })