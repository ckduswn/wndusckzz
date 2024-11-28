# 데이터를 수집할 수 있는 웹사이트 개발
# 1. 화면 : 특정 정보 입력(streamlit)
# 2. 수집 : 데이터 수집(requests, beautifulsoup)
# 3. 화면 : 출력, 엑셀 다운로드(streamlit, pandas)
# 4. 저장 : 데이터베이스 저장(pymysql + MariaDB)

# 데이터를 수집하는 이유?
#  → 데이터 분석 or 인공지능 학습
#  → CSV or JSON 수집
# CSV  예 : 1, 최체리, 10, 여
# JSON 예 :
# {
#     "번호":1,
#     "이름":"최체리",
#     "나이":10,
#     "성별":여
# }

from fnc_service import collect_news
import streamlit as st
from datetime import datetime

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
    if st.button("수집"):
        df_news, count = collect_news()
        st.write(f"뉴스 {count}건 수집 완료!")
        st.write(df_news)
        flag=True
        # df_news : DataFrame → CSV type
        news_csv=df_news.to_csv(index=False, encoding="utf8")
    if flag:
        now=datetime.now().strftime("%Y%m%d%H%M%S")
        st.download_button(
            Label="다운로드",
            data=news_csv,
            file_name=f"실시간뉴스_{now}.csv",
            mime="text/csv",
            key="download_csv"
        )
        
        # 유효성 체크 → 사용자가 입력한 값이 유효한 값인지 체크
        # 전처리(가공) → 유효한 값으로 변경
        # 1. 정규식을 활용한 유효성 체크
        # 2. 엑셀 파일로 생성 후 다운로드
        # 3. github 정리 → README.md(리.꾸)

if __name__=="__main__": 
    main()