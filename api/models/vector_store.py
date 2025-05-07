from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

def load_proposal_vector_db():
    embedding = OpenAIEmbeddings()
    vector_db = FAISS.load_local("proposal_vector_db", embeddings=embedding)
    return vector_db