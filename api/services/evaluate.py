import openai

def load_judge_prompts(filepath="judge.txt", delimiter="심사위원"):
    """judge.txt에서 심사 프롬프트를 로드하여 리스트로 반환"""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    return [p.strip() for p in content.split(delimiter) if p.strip()]

def evaluate_text_by_judges(input_text):
    """주어진 심사 프롬프트들을 기반으로 텍스트를 평가"""
    evaluations = []
    judge_prompts=load_judge_prompts
    for i, prompt in enumerate(judge_prompts, 1):
        full_prompt = f"""
        당신은 전문적인 심사위원입니다. 아래의 기준에 따라 텍스트를 평가하고 점수(1~10)와 간단한 평가 이유를 출력하세요.

        [심사 기준]
        {prompt}

        [평가할 텍스트]
        {input_text}

        [출력 형식]
        점수: x/10
        평가: 평가 사유
        """
        print(f"\n=== 🧑‍⚖️ 심사위원 {i} 평가 ===")

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "당신은 공정하고 전문적인 평가자입니다."},
                {"role": "user", "content": full_prompt}
            ]
        )

        message = response['choices'][0]['message']['content'].strip()
        evaluations.append((i, message))
        print(message)

    return evaluations
