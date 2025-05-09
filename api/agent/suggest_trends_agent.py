from openai import OpenAI
import os
from api.services.embedding import meta_data_store

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def suggest_trends(doc_title: str) -> list:
    try:
        chunks = [m["chunk_text"] for m in meta_data_store if m["doc_title"] == doc_title]
        combined_text = "\n\n".join(chunks[:5]) if chunks else ""

        prompt = f"""
        다음은 공공 제안서의 일부입니다:
        ---
        {combined_text}
        ---
        이 제안서와 관련하여 기술 또는 서비스 측면에서 고려해야 할 최신 트렌드나 기능 제안을 3가지 추천해 주세요.
        각 제안은 한 문장 이내로 작성하세요.
        """

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "당신은 최신 기술 트렌드를 추천하는 AI 전문가입니다."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip().split("\n")
    except Exception as e:
        import traceback
        traceback.print_exc()
        return ["트렌드 추천 실패"]
