from langchain.tools import tool
from langchain_ollama import ChatOllama

# 1. 도구 정의
@tool
def add_numbers(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@tool("곱셈연산")
def multiply_numbers(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

# -----------------------------------------------------------
# [수정 포인트 1] 도구 단독 실행 결과 출력하기
# -----------------------------------------------------------
print("--- [1] 도구 직접 테스트 ---")
result_add = add_numbers.invoke({"a": 3, "b": 4})
print(f"덧셈 결과: {result_add}")  # 7 출력

result_mul = multiply_numbers.invoke({"a": 3, "b": 4})
print(f"곱셈 결과: {result_mul}")  # 12 출력


# -----------------------------------------------------------
# [수정 포인트 2] 도구 정보 출력 (기존 코드 유지)
# -----------------------------------------------------------
print("\n--- [2] 도구 메타데이터 확인 ---")
print(f"도구 이름: {add_numbers.name}")
print(f"도구 설명: {add_numbers.description}")
print(f"도구 스키마: {add_numbers.args_schema.schema()}")


# -----------------------------------------------------------
# [수정 포인트 3] LLM에 도구 바인딩 및 실행 결과 출력
# -----------------------------------------------------------
print("\n--- [3] LLM 실행 결과 ---")

tools = [add_numbers, multiply_numbers]

llm = ChatOllama(
    base_url="http://localhost:11434",
    model="gemma3:4b",
    temperature=0.3,
)

# LLM에 도구 쥐어주기
llm_with_tools = llm.bind_tools(tools)

# LLM에게 질문 던지기
response = llm_with_tools.invoke("1 + 3 = ?")

# 결과 출력 (AIMessage 객체가 출력됩니다)
print(response)