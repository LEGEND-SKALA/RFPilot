from langchain.agents import initialize_agent, Tool
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
import os


def summarize_proposal(file):
    temp_path = "temp_eval.txt"
    with open(temp_path, "wb") as f:
        f.write(file.file.read())

    # load from local FAISS DB
    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.load_local("proposal_vector_db", embeddings=embedding)
    retriever = db.as_retriever()

    # 심사 기준 프롬프트 템플릿
    eval_criteria = [
        "1. 제안 목적과 목표의 명확성",
        "2. 실행 가능성과 현실성",
        "3. 차별성과 혁신성"
    ]

    llm = ChatOpenAI(temperature=0)

    agents_summary = {}
    for idx, criterion in enumerate(eval_criteria, start=1):
        prompt = PromptTemplate(
            input_variables=["context"],
            template=f"""
            다음 제안서를 기반으로 심사 기준 [{criterion}] 에 따라 평가 요약을 작성하세요:
            ---
            {{context}}
            """
        )
        chain = LLMChain(llm=llm, prompt=prompt)
        docs = retriever.get_relevant_documents(criterion)
        context = "\n".join([doc.page_content for doc in docs])
        agents_summary[f"criterion_{idx}"] = chain.run(context)

    # 전체 요약
    full_docs = retriever.get_relevant_documents("전체 요약")
    full_context = "\n".join([doc.page_content for doc in full_docs])
    full_prompt = PromptTemplate(
        input_variables=["context"],
        template="""
        다음 제안서를 전반적으로 요약해 주세요:
        ---
        {context}
        """
    )
    full_chain = LLMChain(llm=llm, prompt=full_prompt)
    agents_summary["overall_summary"] = full_chain.run(full_context)

    os.remove(temp_path)
    return agents_summary