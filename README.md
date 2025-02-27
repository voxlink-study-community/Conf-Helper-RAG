# RAG 기반 환경설정 가이드 챗봇

## 📌 프로젝트 개요
이 프로젝트는 **RAG 기반 환경설정 가이드 챗봇**을 구축하여, Airflow 및 리눅스 환경 설정 관련 가이드를 제공하는 챗봇 시스템입니다. 
FastAPI를 백엔드로 사용하고, FAISS를 활용한 벡터 검색 및 OpenAI의 LLM(ChatGPT API)을 사용하여 질문에 대한 답변을 생성합니다.

## 🛠 기술 스택
- **FastAPI** - REST API 백엔드
- **Langchain + FAISS** - 문서 벡터 검색
- **OpenAI ChatGPT API** - LLM 기반 답변 생성
- **Docker Compose** - 배포 및 실행 환경 구성
- **.env 환경 변수 사용** - API Key 관리

---

## 🚀 실행 방법

### 1️⃣ 환경 변수 설정
`.env` 파일을 프로젝트 루트에 생성하고 아래 내용을 추가하세요:
```plaintext
OPENAI_API_KEY=your-api-key-here
```

⚠️ **중요:** `.env` 파일은 `Docker Hub`에 업로드되면 안 되므로 `.dockerignore`에서 유지합니다.

### 2️⃣ 필요 패키지 설치
```bash
pip install -r requirements.txt
```

### 3️⃣ FastAPI 서버 실행
```bash
python main.py
```

### 4️⃣ API 테스트 방법
```bash
# 문서 검색 API 테스트
curl -X GET "http://localhost:8000/search/?query=Python 설치"

# 챗봇 API 테스트
curl -X GET "http://localhost:8000/chat/?query=Python 환경 설정 방법"
```


## 🐳 Docker Compose 실행 방법
Docker 환경에서 실행하려면 아래 명령어를 사용하세요.
```bash
docker-compose up --build
```

서버가 정상적으로 실행되면 아래 URL에서 API를 확인할 수 있습니다:
- API 문서: [http://localhost:8000/docs](http://localhost:8000/docs)
- 문서 검색 API: `http://localhost:8000/search/?query=YOUR_QUERY`
- 챗봇 API: `http://localhost:8000/chat/?query=YOUR_QUERY`

⚠️ **Docker Hub에 올릴 경우 .env 파일을 올리지 않도록 주의하세요!**

## 🛠 주요 기능
- 📄 **문서 기반 검색**: FAISS 벡터 DB를 활용한 관련 문서 검색
- 🤖 **LLM 기반 응답 생성**: OpenAI ChatGPT API와 Langchain을 활용한 대화 생성
- 🏗 **FastAPI 서버**: REST API 기반으로 확장 가능
- 🐳 **Docker 지원**: 컨테이너 기반으로 배포 가능

---

## 📌 추가 사항
- **테스트 코드 작성**: `pytest` 기반 API 테스트 추가 예정
- **Streamlit UI 개발**: 웹 기반 챗봇 인터페이스 추가 예정
- **API 최적화**: Langchain을 통한 토큰 최적화 및 성능 개선 계획

---

## 📢 문의 및 개선
이 프로젝트에 기여하거나 문의사항이 있으면 GitHub Issue를 생성해주세요! 😊

