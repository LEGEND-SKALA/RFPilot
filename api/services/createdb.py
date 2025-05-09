from langchain.vectorstores import FAISS
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
import os, shutil

def create_proposal_vector_db(file):
    temp_path = "temp_proposal.txt"
    with open(temp_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    loader = TextLoader(temp_path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = splitter.split_documents(documents)

    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.from_documents(texts, embedding)

    db.save_local("proposal_vector_db")
    os.remove(temp_path)