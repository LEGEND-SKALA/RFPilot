from typing import List, Dict
import faiss
from transformers import GPT2LMHeadModel, AutoTokenizer
import torch
from concurrent.futures import ThreadPoolExecutor

import hashlib
import os
import json

import numpy as np
from api.services.embedding import meta_data_store, load_index, embedding_model

# KoGPT 로드
tokenizer = AutoTokenizer.from_pretrained("skt/kogpt2-base-v2")
tokenizer.pad_token = tokenizer.eos_token  # GPT2는 pad_token이 없음

# 모델 로드
model = GPT2LMHeadModel.from_pretrained("skt/kogpt2-base-v2")

# Set device (Apple Silicon M2 optimization)
device = torch.device("cpu")
model.to(device)
model.eval()

# Constants
MAX_TOKENS = 256
PROMPT_OVERHEAD = 100
MAX_INPUT_TOKENS = MAX_TOKENS - PROMPT_OVERHEAD

# 프롬프트 템플릿
PROMPT_TEMPLATE = """
당신은 공공 입찰문서를 요약하는 도우미입니다.

다음은 정부 사업의 공고문입니다. 이 문서를 바탕으로 아래 항목을 요약하여 제안서를 작성하려는 사람에게 간결한 가이드를 제공하세요:

1. 사업 목적 및 배경
2. 신청 자격 및 대상
3. 지원 금액 및 기간
4. 제출 서류 및 신청 방법
5. 평가 항목 및 배점 기준

아래는 문서의 일부입니다:
---
{text}
---
위 정보를 바탕으로 각 항목에 대해 핵심만 요약하여 작성하세요.
모든 항목이 문서에 없다면 '문서에 명시되지 않음'으로 표기하세요.
"""

EVALUATION_PROMPT_TEMPLATE = """
당신은 제안서를 평가하는 평가 항목을 분석하는 도우미입니다.

아래는 정부 공고문입니다. 이 문서에서 평가 기준, 평가 항목, 배점 기준 등을 찾아 핵심 정보를 정리해 주세요. 평가 기준은 표 형태일 수도 있고 본문에 포함되어 있을 수도 있습니다.

---
{text}
---

요약 형식 예시:
- 정성 평가 항목: 창의성, 기대효과, 사업 이해도 등 (배점: 40점)
- 정량 평가 항목: 실적, 인력 등 (배점: 60점)
- 세부 기준: 각 항목별 평가 기준, 평가 방법 요약
"""

# 캐시 폴더
CACHE_DIR = "summary_cache"
os.makedirs(CACHE_DIR, exist_ok=True)

def hash_text(text: str) -> str:
    return hashlib.md5(text.encode("utf-8")).hexdigest()

def load_cached_summary(hash_key: str) -> str:
    path = os.path.join(CACHE_DIR, f"{hash_key}.json")
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f).get("summary", "")
    return ""

def save_cached_summary(hash_key: str, summary: str):
    path = os.path.join(CACHE_DIR, f"{hash_key}.json")
    with open(path, "w") as f:
        json.dump({"summary": summary}, f)

def split_text_by_tokens(text: str, max_tokens: int) -> List[str]:
    tokens = tokenizer.encode(text)
    return [tokenizer.decode(tokens[i:i + max_tokens]) for i in range(0, len(tokens), max_tokens)]

def kogpt_generate(prompt: str, max_new_tokens: int = 512) -> str:
    input_ids = tokenizer.encode(prompt, return_tensors="pt").to(device)
    if input_ids.shape[1] > 1024:
        input_ids = input_ids[:, -1024:]

    with torch.no_grad():
        output = model.generate(
            input_ids,
            max_new_tokens=max_new_tokens,
            temperature=0.7,
            top_p=0.85,
            do_sample=True,
            eos_token_id=tokenizer.eos_token_id,
            pad_token_id=tokenizer.pad_token_id
        )

    decoded_output = tokenizer.decode(output[0], skip_special_tokens=True)
    prompt_text = tokenizer.decode(input_ids[0], skip_special_tokens=True)
    return decoded_output.split(prompt_text, 1)[-1].strip() if prompt_text in decoded_output else decoded_output.strip()

def summarize_with_token_limit(text: str, prompt_template: str) -> List[str]:
    parts = split_text_by_tokens(text, MAX_INPUT_TOKENS)
    summaries = []
    for part in parts:
        prompt = prompt_template.replace("{text}", part)
        hash_key = hash_text(prompt)
        cached = load_cached_summary(hash_key)
        if cached:
            summaries.append(cached)
        else:
            summary = kogpt_generate(prompt)
            save_cached_summary(hash_key, summary)
            summaries.append(summary)
    return summaries

def parse_table_data(table: str) -> str:
    return "\n".join(f"- {line.strip()}" for line in table.strip().split('\n') if line.strip())

def extract_text_from_chunk(chunk: Dict) -> str:
    texts = [f"# {chunk.get('section_title', '')}"]
    for sub in chunk.get("subsections", []):
        subtitle = sub.get("subtitle", "").strip()
        content = sub.get("content", "").strip()
        tables = sub.get("tables", [])
        if subtitle:
            texts.append(f"## {subtitle}")
        if content:
            texts.append(content)
        for table in tables:
            texts.append(parse_table_data(table))
    return "\n".join(texts)

def filter_important_chunks(chunks: List[Dict], max_chunks: int = 5) -> List[Dict]:
    keywords = ["사업", "지원", "신청", "평가", "대상", "목표"]
    scored = []
    for ch in chunks:
        score = sum(k in ch.get("content", "") for k in keywords)
        for sub in ch.get("subsections", []):
            score += sum(k in sub.get("content", "") for k in keywords)
        scored.append((score, ch))
    return [x[1] for x in sorted(scored, key=lambda x: x[0], reverse=True)[:max_chunks]]

def generate_summary(chunks: List[Dict]) -> str:
    important_chunks = filter_important_chunks(chunks)
    extracted_texts = [extract_text_from_chunk(ch) for ch in important_chunks if ch]
    
    # 1차 요약 (각 chunk별 split & summarize)
    all_summaries = []
    for text in extracted_texts:
        summaries = summarize_with_token_limit(text, PROMPT_TEMPLATE)
        all_summaries.extend(summaries)
    
    # 2차 요약 (전체 요약본들을 다시 통합하고 token-safe하게 split하여 처리)
    combined_text = "\n\n".join(all_summaries)
    final_summaries = summarize_with_token_limit(combined_text, PROMPT_TEMPLATE)

    return "\n\n".join(final_summaries)


def extract_evaluation_criteria(doc_title: str) -> str:
    relevant_chunks = [m for m in meta_data_store if m["doc_title"] == doc_title and "평가" in m["chunk_text"]]

    if not relevant_chunks:
        return "문서에서 평가 기준 관련 정보를 찾을 수 없습니다."

    query = "이 문서의 평가 기준과 배점 항목을 찾아줘"
    query_vec = embedding_model.encode([query])

    chunk_texts = [item["chunk_text"] for item in relevant_chunks]
    chunk_vectors = embedding_model.encode(chunk_texts)
    chunk_vectors = np.array(chunk_vectors)

    index_local = faiss.IndexFlatL2(chunk_vectors.shape[1])
    index_local.add(chunk_vectors)

    D, I = index_local.search(np.array(query_vec), 5)
    top_chunks = [chunk_texts[i] for i in I[0]]

    combined_text = "\n\n".join(top_chunks)
    eval_prompt = EVALUATION_PROMPT_TEMPLATE.replace("{text}", combined_text[:1000])
    return kogpt_generate(eval_prompt)