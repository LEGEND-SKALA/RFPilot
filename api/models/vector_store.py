from langchain_community.chat_models import ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings

def load_proposal_vector_db():
    embedding = OpenAIEmbeddings()

    vector_db = FAISS.load_local(
        "faiss_store",
        embeddings=embedding,
        allow_dangerous_deserialization=True  #pkl 파일 허용
    )
    return vector_db