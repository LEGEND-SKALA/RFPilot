import api.models.vector_store as vs
<<<<<<< HEAD
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.llms.openai import OpenAI  # 일반적인 텍스트 응답용
from langchain_core.runnables import RunnableSequence
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
=======
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
>>>>>>> 021f1ebc458ed13ed652fcf7e0d6ce9d2bfafbe1
from nltk.tokenize import sent_tokenize
import nltk

vector_db = vs.load_proposal_vector_db()

nltk.download("punkt")

# 1. 문장 단위 분리
def split_text_into_sentences(text: str) -> list[str]:
    return sent_tokenize(text)

# 2. 벡터 DB에서 가장 유사한 문서 추출
def query_vector_db(sentence: str, top_k: int = 3) -> list[str]:
    results = vector_db.similarity_search(sentence, k=top_k)
    return [res.page_content for res in results]

# 3. LLM을 이용한 적합도 판단
def judge_relevance(sentence: str, reference: str) -> str:
    prompt_template = PromptTemplate(
        input_variables=["sentence", "reference"],
        template="""
        다음은 사용자 입력 문장입니다:
        "{sentence}"

        다음은 참고 문서입니다:
        "{reference}"

        위 문장이 참고 문서 내용과 주제 및 맥락상 적합한 문장인지 판단해 주세요.
        결과는 "적합" 또는 "부적합"으로만 응답하고, 판단 근거는 생략하세요.
        """
    )
    llm = OpenAI(temperature=0)
    chain = RunnableSequence([prompt_template, llm, StrOutputParser()])
    return chain.run({"sentence": sentence, "reference": reference}).strip()

# 4. 전체 평가 흐름
def evaluate_script(script_text: str):
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    sentences = split_text_into_sentences(script_text)
    suitable = []
    unsuitable = []

    for sentence in sentences:
        top_refs = query_vector_db(vector_db, sentence, top_k=3)
        if not top_refs:
            unsuitable.append(sentence)
            continue

        judgment = judge_relevance(sentence, top_refs[0])
        if "적합" in judgment:
            suitable.append(sentence)
        else:
            unsuitable.append(sentence)

    return {
        "correct_sentences": suitable,
        "incorrect_sentences": unsuitable
    }
