import os
from dotenv import load_dotenv
from pathlib import Path

# 🔹 LangChain / OpenAI 모듈
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


# ===============================
# 1. 환경설정 (.env 로드)
# ===============================
dotenv_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path)

langsmith_key = os.getenv("LANGSMITH_API_KEY")
openai_key = os.getenv("OPENAI_API_KEY")

print("📦 LANGSMITH_API_KEY =", langsmith_key)
print("📦 OPENAI_API_KEY =", openai_key[:8] + "..." if openai_key else "❌ 없음")

if not openai_key:
    print("❌ OPENAI_API_KEY가 설정되지 않았습니다.")
    exit(1)

# LangSmith 추적 활성화
os.environ["LANGCHAIN_TRACING_V2"] = "true"


# ===============================
# 2. 기본 모델 초기화
# ===============================
llm = ChatOpenAI(model="gpt-4o-mini", api_key=openai_key)


# ===============================
# 3. 예제 3.1 — 기본 예제
# ===============================
print("\n🧩 [3.1 기본 예제]")
response = llm.invoke("지구의 자전 주기는?")
print("💬 응답:", response.content)












# ===============================
# 4. 예제 3.2 — 프롬프트 템플릿 적용
# ===============================
print("\n🧩 [3.2 프롬프트 템플릿 적용]")

prompt = ChatPromptTemplate.from_template(
    "You are an expert in astronomy. Answer the question. <Question>: {input}"
)

chain = prompt | llm
response = chain.invoke({"input": "지구의 자전 주기는?"})
print("💬 응답:", response.content)












# ===============================
# 5. 예제 3.3 — 출력 결과 파싱 (문자열 변환)
# ===============================
print("\n🧩 [3.3 출력 결과 파싱]")

prompt = ChatPromptTemplate.from_template(
    "You are an expert in astronomy. Answer the question. <Question>: {input}"
)
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

response = chain.invoke({"input": "지구의 자전 주기는?"})
print("💬 응답:", response)











# ===============================
# 6. 예제 3.4 — 멀티 체인 (한국어 → 영어 → 설명)
# ===============================
print("\n🧩 [3.4 멀티 체인 예제]")

# 첫 번째 체인: 한국어 → 영어 번역
prompt1 = ChatPromptTemplate.from_template("translate {korean_word} to English.")
# 두 번째 체인: 영어 단어 의미 설명
prompt2 = ChatPromptTemplate.from_template(
    "explain {english_word} using Oxford dictionary to me in Korean."
)

# 체인 구성
chain1 = prompt1 | llm | StrOutputParser()
chain2 = ({"english_word": chain1} | prompt2 | llm | StrOutputParser())

response = chain2.invoke({"korean_word": "미래"})
print("💬 응답:", response)











# ===============================
# 7. 종료 메시지
# ===============================
print("\n✅ 모든 LangChain + OpenAI 예제가 정상적으로 실행되었습니다.")
