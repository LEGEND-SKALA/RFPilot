from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
import os

embedding_model = HuggingFaceEmbeddings(model_name="snunlp/KR-SBERT-V40K-klueNLI-augSTS")
VECTOR_DB_PATH = "faiss_store"

def load_proposal_vector_db(doc_title: str):
    db_path = os.path.join(VECTOR_DB_PATH, doc_title)
    if not os.path.exists(db_path):
        raise FileNotFoundError(f"벡터 DB '{doc_title}'가 존재하지 않습니다.")
    return FAISS.load_local(
        folder_path=db_path,
        embeddings=embedding_model,
        allow_dangerous_deserialization=True  # ✅ 이 줄 추가
    )