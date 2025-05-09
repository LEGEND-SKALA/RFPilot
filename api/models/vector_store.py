from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
import os

embedding_model = HuggingFaceEmbeddings(model_name="snunlp/KR-SBERT-V40K-klueNLI-augSTS")
VECTOR_DB_PATH = "faiss_store"
def load_proposal_vector_db():
    # embedding = OpenAIEmbeddings()
    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_db = FAISS.load_local(
        "faiss_store",
        embeddings=embedding,
        allow_dangerous_deserialization=True  #pkl 파일 허용
    )
    return vector_db
