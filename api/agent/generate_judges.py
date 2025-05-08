from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_judges(count: int, company_name: str, service_description: str) -> list:
    try:
        prompt = f"""
        당신은 공공 프로젝트를 심사할 AI 심사위원입니다.
        아래는 제안 기업과 서비스 설명입니다:

        기업명: {company_name}
        서비스 개요: {service_description}

        이 정보를 바탕으로, 제안서를 평가할 {count}명의 심사위원을 역할에 따라 생성해 주세요.
        각 심사위원은 다음 정보를 포함해야 합니다:
        1. 심사위원 이름
        2. 역할 및 전문 분야
        3. 주 평가 항목
        4. 제안서를 읽고 남길 수 있는 예상 피드백 500자(구체적으로)

        아래 형식을 따라 주세요:
        - 심사위원 이름: 역할 (평가 항목) → 피드백: "..."

        예시:
        - 김기술: 기술 전문가 (적용 기술의 적절성) → 예상 피드백: "제안된 기술 스택은 최신 트렌드와 부합하지만, 구현 난이도에 대한 고려가 부족해 보입니다."
        """

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "당신은 제안서 평가를 담당하는 AI입니다."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip().split("\n")
    except Exception as e:
        import traceback
        traceback.print_exc()
        return ["심사위원 생성 실패"]