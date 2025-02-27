# RAG 기반 환경설정 가이드 챗봇

## 📌 프로젝트 개요

이 프로젝트는 **RAG 기반 환경설정 가이드 챗봇**을 구축하여, Airflow 및 리눅스 환경 설정 관련 가이드를 제공하는 챗봇 시스템입니다.
FastAPI를 백엔드로 사용하고, FAISS를 활용한 벡터 검색 및 OpenAI의 LLM(ChatGPT API)을 사용하여 질문에 대한 답변을 생성합니다. 또한, Streamlit을 활용하여 UI에서 직접 질문을 입력하고 응답을 확인할 수 있습니다.

## 🛠 기술 스택

- **FastAPI** - REST API 백엔드
- **Langchain + FAISS** - 문서 벡터 검색
- **OpenAI ChatGPT API** - LLM 기반 답변 생성
- **Streamlit** - 웹 기반 챗봇 UI
- **API 테스트 방법Docker Compose** - 배포 및 실행 환경 구성
- **.env 환경 변수 사용** - API Key 관리

---

## 🚀 실행 방법

### 1️⃣ 환경 변수 설정

`.env` 파일을 프로젝트 루트에 생성하고 아래 내용을 추가하세요:

```plaintext
OPENAI_API_KEY=your-api-key-here
```

⚠️ **중요:** `.env` 파일은 `Docker Hub`에 업로드되지 않도록 `.gitignore`에서 제외 처리해야 합니다.

### 2️⃣ 필요 패키지 설치

```bash
pip install -r requirements.txt
```

### 3️⃣ FastAPI 및 Streamlit 서버 실행 (개별 실행)

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload &
streamlit run streamlit_app.py --server.port 8501 --server.address 0.0.0.0
```



### 4️⃣ Streamlit UI 실행

```bash
streamlit run streamlit_app.py
```

### 5️⃣ API 테스트 방법

```bash
# 문서 검색 API 테스트
curl -X GET "http://localhost:8000/search/?query=Python 설치"

# 챗봇 API 테스트 (리눅스/macOS)
curl -X POST "http://localhost:8000/chat/" -H "Content-Type: application/json" -d '{"query": "Python 환경 설정 방법"}'

# 챗봇 API 테스트 (Windows PowerShell)
Invoke-RestMethod -Uri "http://localhost:8000/chat/" -Method Post -Headers @{"Content-Type"="application/json"} -Body '{"query": "Python 환경 설정 방법"}'
```
---


## 🖥 Streamlit UI 화면 구성

- **질문 입력 필드**: 사용자가 환경 설정 관련 질문을 입력하는 곳입니다.
- **질문하기 버튼**: 입력된 질문을 FastAPI 서버에 전송하여 답변을 받습니다.
- **답변 출력 영역**: OpenAI API를 통해 생성된 답변이 표시됩니다.
- **참고 문서 표시**: 검색된 관련 문서의 출처를 보여줍니다.
- **검색 기능**: 특정 키워드에 대한 관련 문서를 찾을 수 있습니다.
- **검색 결과 출력**: 검색된 문서 내용을 확인할 수 있습니다.

---

## 🐳 Docker Compose 실행 방법

Docker 환경에서 FastAPI 및 Streamlit을 실행하려면 아래 명령어를 사용하세요.

```bash
docker-compose up --build
```

서버가 정상적으로 실행되면 아래 URL에서 FastAPI 및 Streamlit을 확인할 수 있습니다:

- API 문서: [http://localhost:8000/docs](http://localhost:8000/docs)
- 문서 검색 API: `http://localhost:8000/search/?query=YOUR_QUERY`
- 챗봇 API: `http://localhost:8000/chat/?query=YOUR_QUERY`

Streamlit UI는 `http://localhost:8501`에서 실행됩니다.

⚠️ **Docker Hub에 올릴 경우 .env 파일을 올리지 않도록 주의하세요!**

---

## 🛠 주요 기능

- 📄 **문서 기반 검색**: FAISS 벡터 DB를 활용한 관련 문서 검색
- 🤖 **LLM 기반 응답 생성**: OpenAI ChatGPT API와 Langchain을 활용한 대화 생성
- 🏗 **FastAPI 서버**: REST API 기반으로 확장 가능
- 🖥 **Streamlit UI 지원**: 웹 기반 챗봇 인터페이스 제공
- 🐳 **Docker 지원**: 컨테이너 기반으로 배포 가능

---

## 📌 추가 사항

- **테스트 코드 작성**: `pytest` 기반 API 테스트 추가 예정
- **Streamlit UI 개선**: 사용자 경험 향상을 위한 UI 개선 예정
- **API 최적화**: Langchain을 통한 토큰 최적화 및 성능 개선 계획

---

## 📢 문의 및 개선

이 프로젝트에 기여하거나 문의사항이 있으면 GitHub Issue를 생성해주세요! 😊

