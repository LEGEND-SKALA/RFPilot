
import os
import fitz  # PyMuPDF
from docx import Document as DocxDocument
from pptx import Presentation
import nltk
from nltk.tokenize import sent_tokenize
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
import api.models.vector_store as vs
from fastapi import UploadFile, File

def extract_text_from_file(file):
    contents = file.read()
    with fitz.open(stream=contents, filetype="pdf") as doc:
        text = "\n".join([page.get_text() for page in doc])
    return text

# === [2] 문장 유사도 분석 ===
def analyze_similarity(file: UploadFile = File(...), top_k: int = 3):
    text = extract_text_from_file(file)
    sentences = sent_tokenize(text)

    # 벡터 DB 로딩
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    scored_sentences = []
    for idx, sentence in enumerate(sentences):
        results = vector_db.similarity_search_with_score(sentence, k=top_k)
        if results:
            top_score = results[0][1]  # 두 번째 요소가 점수
            scored_sentences.append((idx, sentence, top_score))

    # 유사도 평균
    avg_score = sum([score for _, _, score in scored_sentences]) / len(scored_sentences)

    # 상위/하위 문장 (유사도 기준)
    scored_sentences.sort(key=lambda x: x[2])
    lowest = scored_sentences[:3]
    highest = scored_sentences[-3:]

    return {
        "평균 유사도": avg_score,
        "유사도 높은 문장": [{"문장번호": i, "문장": s, "점수": sc} for i, s, sc in reversed(highest)],
        "유사도 낮은 문장": [{"문장번호": i, "문장": s, "점수": sc} for i, s, sc in lowest]
    }
