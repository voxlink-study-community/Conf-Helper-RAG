import streamlit as st
import requests

# FastAPI 서버 URL
API_URL = "http://127.0.0.1:8000/chat/"  # FastAPI 서버가 실행 중인 주소 확인
SEARCH_API_URL = "http://127.0.0.1:8000/search/"

st.title("RAG 기반 환경설정 가이드 챗봇")
st.write("환경설정 관련 질문을 입력하세요.")

# 사용자 입력
query = st.text_input("질문을 입력하세요:")

if st.button("질문하기") and query:
    with st.spinner("답변을 생성 중입니다..."):
        response = requests.post(API_URL, json={"query": query})
        if response.status_code == 200:
            data = response.json()
            st.subheader("답변:")
            st.write(data["answer"])
            
            # 출처 문서 표시
            if data["sources"]:
                st.subheader("참고 문서:")
                for source in data["sources"]:
                    st.write(f"- {source}")
        else:
            st.error("API 요청 실패. 서버 상태를 확인하세요.")

st.subheader("관련 문서 검색")
search_query = st.text_input("검색어를 입력하세요:")

if st.button("검색") and search_query:
    search_response = requests.get(SEARCH_API_URL, params={"query": search_query})
    if search_response.status_code == 200:
        search_data = search_response.json()
        st.write("### 검색 결과")
        for idx, result in enumerate(search_data["results"], 1):
            st.write(f"{idx}. {result}")
    else:
        st.error("검색 API 요청 실패. 서버 상태를 확인하세요.")
