import models.vector_store as vs
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.docstore.document import Document

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
def fill_missing_parts(incomplete_text: str, reference_texts: list[str]) -> str:
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

    chain = LLMChain(llm=llm, prompt=prompt_template)
    references_combined = "\n\n".join(reference_texts)
    output = chain.run({"incomplete": incomplete_text, "references": references_combined})
    return output
