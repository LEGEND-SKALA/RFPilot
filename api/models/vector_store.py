from langchain_community.chat_models import ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

def load_proposal_vector_db():
    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_db = FAISS.load_local(
        "faiss_store",
        embeddings=embedding,
        allow_dangerous_deserialization=True  #pkl 파일 허용
    )
    return vector_db