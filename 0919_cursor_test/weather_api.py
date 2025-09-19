import os
from dotenv import load_dotenv
from openai import OpenAI

# .env 로드
load_dotenv()

# OpenAI 클라이언트 생성 (API 키 직접 주입)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 사용자가 물어본 질문
messages = [
    {"role": "user", "content": "서울의 현재 날씨는 어떤가요?"}
]

# AI에게 알려줄 도구(Function) 정의
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "e.g. San Francisco, CA"
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"]
                    }
                },
                "required": ["location"]
            }
        }
    }
]

# ChatCompletion API 호출
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
    tools=tools,
    tool_choice="auto"  # 모델이 필요 시 함수를 선택해서 호출
)

# 응답 출력 (전체 객체)
print("=== Raw Response ===")
print(response)

# 모델이 함수 호출을 요청했는지 확인
if response.choices[0].message.tool_calls:
    print("\n=== Tool Call Detected ===")
    print(response.choices[0].message.tool_calls)
else:
    print("\n=== Model Answer ===")
    print(response.choices[0].message.content)
