# 데이터를 수집할 수 있는 웹사이트 개발
# 1. 화면 : 특정 정보 입력(streamlit)
# 2. 수집 : 데이터 수집(requests, beautifulsoup)
# 3. 화면 : 출력, 엑셀 다운로드(streamlit, pandas)
# 4. 저장 : 데이터베이스 저장(pymysql + MariaDB)
from fnc_service import collect_news
import streamlit as st

# Streamlit run project_collector/main.py
# Streamlit docs → https://docs.streamlit.io/
# Emoji → https://snskeyboard.com/emoji/


def main():
    
    st.set_page_config(
        page_title="NEWS COLLECTOR",  # 제목
        page_icon="project_collector/img/favicon.png"
    )
    st.title("NEWS :rainbow[COLLECTOR]")
    st.text("Boogie on and on.")
    with st.form(key="form"):
        submitted = st.form_submit_button("collect")

    # 버튼 이벤트 → 수집 버튼을 클릭할 때
    # 위에 submitted 변수 추가. 
    if submitted:
         collect_news()

        # 유효성 체크 → 사용자가 입력한 값이 유효한 값인지 체크
        # 전처리(가공) → 유효한 값으로 변경
        # 1. 정규식을 활용한 유효성 체크
        # 2. 엑셀 파일로 생성 후 다운로드
        # 3. github 정리 → README.md(리.꾸)

if __name__=="__main__": 
    main()