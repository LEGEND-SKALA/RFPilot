from typing import List, Dict, Any
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os
import pickle

# 모델 로딩 (KoSimCSE-base)
embedding_model = SentenceTransformer("BM-K/KoSimCSE-roberta")

# FAISS 인덱스 전역
DIMENSION = 768  # 모델에 따라 다를 수 있음
index = faiss.IndexFlatL2(DIMENSION)
meta_data_store: List[Dict[str, Any]] = []

# 벡터 저장 경로
INDEX_PATH = "faiss_index.bin"
META_PATH = "faiss_meta.pkl"

def embed_and_index(chunks: List[Dict[str, Any]], doc_title: str):
    global meta_data_store

    for chunk in chunks:
        # section만 있을 수도, subsection 여러 개일 수도 있음
        section_text = chunk.get("content", "")
        title = chunk.get("section_title", "")

        if section_text:
            vector = embedding_model.encode(section_text)
            index.add(np.array([vector]))
            meta_data_store.append({
                "section_title": title,
                "chunk_text": section_text,
                "doc_title": doc_title
            })

        for sub in chunk.get("subsections", []):
            sub_text = sub["content"]
            sub_title = sub["subtitle"]
            vector = embedding_model.encode(sub_text)
            index.add(np.array([vector]))
            meta_data_store.append({
                "section_title": title,
                "subsection_title": sub_title,
                "chunk_text": sub_text,
                "doc_title": doc_title
            })

    save_index()

def save_index():
    faiss.write_index(index, INDEX_PATH)
    with open(META_PATH, "wb") as f:
        pickle.dump(meta_data_store, f)

def load_index():
    global index, meta_data_store
    if os.path.exists(INDEX_PATH):
        index = faiss.read_index(INDEX_PATH)
    if os.path.exists(META_PATH):
        with open(META_PATH, "rb") as f:
            meta_data_store = pickle.load(f)
