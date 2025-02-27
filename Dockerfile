FROM python:3.11

# 작업 디렉토리 설정
WORKDIR /app

# 종속성 파일 복사 및 설치
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# 앱 소스 코드 복사
COPY . .

# 환경 변수 설정
ENV PYTHONUNBUFFERED=1

# FastAPI와 Streamlit을 동시에 실행
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port 8000 --reload & streamlit run streamlit_app.py --server.port 8501 --server.address 0.0.0.0"]
