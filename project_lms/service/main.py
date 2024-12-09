# 도서관 관리 프로그램
# - 도서만 관리 프로그램
# - 기능
#   1) 도서 등록 Create
#   2) 도서 수정 Update
#   3) 도서 삭제 Delete
#   4) 도서 조회 Read
#   5) 도서 검색 Read
# - CRUD 개발 학습 → 모든 시스템 또는 프로그램 CRUD 개발
# - 프론트엔드 : Streamlit
# - 백엔드 : Python + SQL
# - DB : Mariadb

# streamlit run project_lms/main.py
import streamlit as st
import pandas as pd
from service import book_service


#################
## 1. 초기 설정 ##
#################

# st. session_state["page"] → 현재 사용 중인 페이지, 상태 정보 저장소. 여기에 Page라는 변수를 만들어 main이라는 값을 저장하겠다.
# 1. Main Page
# 2. Insert(등록) Page
# 3. Update(수정) Page
if "page" not in st.session_state:
    st.sesssion_state["page"] = "main"
    
# 다른 페이지로 이동하는 함수
def navigate_to(page):
    st.session_state["page"] = page
    st.rerun()

# design    
st.markdown("""

    <style>
        .block-container {
            padding-top: 2rem;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
            max-width: 55rem !important;
        }
        hr {
            margin: 0;
            padding: 0;
        }
        .stButton>button {
            width: 5rem;
            padding: 0;
            margin: 0;
            text-align: center;
            font-size: 16px;
            cursor: pointer;
        }

        .stColumns {
            gap: 0px; /* 열 간의 기본 간격을 없애기 */
        }
    </style>

""", unsafe_allow_html=True)

#################
## 2. HEADER  ##
#################
st.title("도서관리시스템")
st. markdown("<hr>", unsafe_allow_html=True)

if st.button("HOME"):
    navigate_to("main")
    
if st.button("등록"):
    navigate_to("insert")
st. markdown("<hr>", unsafe_allow_html=True)

#################
##  3. PAGE    ##
#################
def main_page():
    # [ 전체 도서 데이터 조회]
    rows=book_service.get_books() 
    # [ 도서 검색 ]
    with st.form("search_form"):
        keyword=st.text_input("도서검색")
        submitted=st.form_submit_button("검색")
        if submitted:
            rows=book_service.search_books(keyword)
            st.write(f'"{keyword}"로 검색한 결과는 총 {len(rows)}건 입니다.')
    event = st.dataframe(rows,
                       on_select="rerun",
                       selection_mode="simgle-row", # 하나만 선택 가능. Multi-col : 다중선택
                       use_container_width=True,    # 가로 길이 폭. True : 가장 큰 폭.
                       hide_index=True)             # 인덱스 숨김.
    if len(event.selection["row"]):
        # 수정, 삭제에선 사용자가 선택한 값이 필요!
        # → 사용자가 선택한 idx의 행(row)값을 가져오기.
        selected_idx=event.selection["row"][0]
        book_isbn=rows.iloc[selected_idx]["book_isbn"]
        book_name=rows.iloc[selected_idx]["book_name"]
        book_writer=rows.iloc[selected_idx]["book_writer"]
        book_publisher=rows.iloc[selected_idx]["book_publisher"]
        book_price=rows.iloc[selected_idx]["book_price"]
        register_at=rows.iloc[selected_idx]["register_at"]
        useyn=rows.iloc[selected_idx]["useyn"]
        
        data={
            "book_isbn":book_isbn,
            "book_name":book_name,
            "book_writer":book_writer,
            "book_publisher":book_publisher,
            "book_price":book_price,
            "register_at":register_at,
            "useyn":useyn
        }
        # data를 update 페이지에서도 활용하기 위해 공용저장소에 저장
        st.session_state["data"]=data
        if st.button("수정"):
            navigate_to("update")
        if st.button("삭제"):
            pass
            
        
def insert_page():
    with st.form("insert_form"):
        book_name=st.text_input("book_name")
        book_writer=st.text_input("book_writer")
        book_publisher=st.text_input("book_publisher")
        book_price=st.text_input("book_price")
        submitted=st.form_fubmit_button("등록")
        
        book={
            "book_name":book_name,
            "book_writer":book_writer,
            "book_publisher":book_publisher,
            "book_price":book_price}

        if submitted:
            book_service.insert_book(book)
            navigate_to("main")
        
def update_page():
    row=st.session_state["data"]
    
    st.write("도서 수정")
    with st.form("update_form"):
        book_isbn=st.text_input("book_isbn", value=row["book_isbn"],disabled=True)
        book_name=st.text_input("도서명", value=row["book_name"])
        book_writer=st.text_input("저자", value=row["book_writer"])
        book_publisher=st.text_input("출판사", value=row["book_publisher"])
        book_price=st.text_input("가격", value=row["book_price"])
        register_at=st.text_input("등록일자", value=row["register_at"])
        useyn=st.text_input("사용유무", value=row["useyn"])
        submitted=st.form_submit_button("수정")
        if submitted:
            book={
                "book_isbn":book_isbn,
                "book_name":book_name,
                "book_writer":book_writer,
                "book_publisher":book_publisher,
                "book_price":book_price,
                "register_at":register_at,
                "useyn":useyn,
            }
            book_service.update_book(book)

######################
##   4. PAGE CTRL   ##
######################
    if st.session_state["page"] == "main":
        main_page()
    elif st.session_state["page"] == "insert":
        insert_page()
    elif st.session_state["page"] == "update":
        update_page()