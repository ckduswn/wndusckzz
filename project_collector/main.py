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

category = "digital" # IT


def main():
    
    st.set_page_config(
        page_title="NEWS COLLECTOR",  # 제목
        page_icon="project_collector/img/favicon.png"
    )
    st.title("NEWS :blue[COLLECTOR]")
    st.text("안녕하십니까")
    
    category = {
        "사회":"society",
        "정치":"politics",
        "경제":"economic",
        "국제":"foreign",
        "문화":"culture",
        "IT":"digital"
    }
    with st.expander(label="news category", expanded=False):
        for key, value in category.items():
            st.text(f"{key}({value})")
    
    with st.form(key="form"):
        # 유효성 체크 → 사용자가 입력한 값이 유효한 값인지 체크
        # 전처리(가공) → 유효한 값으로 변경
        # 1. 정규식을 활용한 유효성 체크
        # 2. 엑셀 파일로 생성 후 다운로드
        # 3. 
        sel_category=st.text_input(label="news category wanna collect")
        st.write(sel_category)
        st.form_submit_button("collect")
    
    
    
    
    
    
    
    
    
    
#    print("Start collector")
#    collect_news(category)
    
if __name__=="__main__": 
    main()