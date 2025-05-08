from openai import OpenAI
import os
from api.services.embedding import meta_data_store

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_proposal(doc_title: str) -> str:
    # 해당 문서의 청크 중 최대 5개만 요약 대상으로 활용
    chunks = [m for m in meta_data_store if m["doc_title"] == doc_title]
    if not chunks:
        return "요약할 내용이 없습니다."

    content = "\n\n".join(m["chunk_text"] for m in chunks[:5])

    prompt = f"""
    다음은 정부 사업 제안서 일부입니다:
    ---
    {content}
    ---
    아래 항목에 따라 제안서를 요약해 주세요:

    1. 사업 목적 및 배경
    2. 신청 자격 및 대상
    3. 지원 금액 및 기간
    4. 제출 서류 및 신청 방법
    5. 평가 항목 및 배점 기준

    명확하고 간결하게 항목별로 정리하세요. 정보가 없을 경우 '명시되지 않음'이라고 적으세요.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "당신은 정부 제안서를 요약하는 전문가입니다."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=800
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        import traceback
        traceback.print_exc()
        return "요약 생성 실패"