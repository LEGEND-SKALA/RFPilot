import api.models.vector_store as vs
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.llms.openai import OpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from langchain.prompts import PromptTemplate
from langchain.docstore.document import Document
from fastapi import UploadFile

vector_db = vs.load_proposal_vector_db()

# 1. 미완성 문서 불러오기
def load_input_text(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

# 2. Vector DB 로드 및 유사 문서 검색
def search_similar_docs(query: str, top_k: int = 3):
    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    docs = vector_db.similarity_search(query, k=top_k)
    return docs

# 3. LLM을 이용해 문서 보완
from fastapi import UploadFile
<<<<<<< HEAD
from langchain import OpenAI, PromptTemplate
=======
from langchain import OpenAI, LLMChain, PromptTemplate
>>>>>>> 021f1ebc458ed13ed652fcf7e0d6ce9d2bfafbe1
from langchain.vectorstores.base import VectorStoreRetriever  # vector_db 타입 힌트
from typing import List

# vector_db는 외부에서 미리 로딩된 전역 객체라고 가정
# 예: vector_db = FAISS.load_local("db_index", embeddings)

def fill_missing_parts(file: UploadFile, vector_db: VectorStoreRetriever) -> str:
    # 1. 파일에서 미완성 문서 내용 추출
    content = file.file.read()
    try:
        incomplete_text = content.decode('utf-8')
    except UnicodeDecodeError:
        incomplete_text = content.decode('cp949', errors='ignore')

    # 2. 벡터 DB에서 관련 문서 검색
    relevant_docs = vector_db.similarity_search(incomplete_text, k=3)  # k는 상위 몇 개 문서
    reference_texts: List[str] = [doc.page_content for doc in relevant_docs]

    # 3. LLM용 프롬프트 구성
    llm = OpenAI(temperature=0.7)

    prompt_template = PromptTemplate(
        input_variables=["incomplete", "references"],
        template="""
        다음은 미완성 문서입니다:
        --------------------
        {incomplete}

        아래는 참고 가능한 문서들입니다:
        --------------------
        {references}

        참고 문서를 바탕으로 미완성 문서를 자연스럽게 보완하세요.
        """
    )

<<<<<<< HEAD
    chain = chain = RunnableSequence([prompt_template, llm, StrOutputParser()])
=======
    chain = LLMChain(llm=llm, prompt=prompt_template)
>>>>>>> 021f1ebc458ed13ed652fcf7e0d6ce9d2bfafbe1
    references_combined = "\n\n".join(reference_texts)
    output = chain.run({"incomplete": incomplete_text, "references": references_combined})
    return output
