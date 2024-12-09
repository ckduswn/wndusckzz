# Back-end pattern
# Controller → Service → DAO → Database

# Service단
# - 실제 비즈니스 로직 기능 구현

# Web programing pattern → MVC, MVT, .. etc
# - MVC : Model + View + Controller

# Web browser(client) → Request(https://naver.com/blog + written text)
# Naver Web Server  → Response(Deliver HTML, contents to Web browser)
# 1. Controller
#   → Get User's Requests
#   → After analyze, deliver to Service단 processing "blog" Buisness logic
# 2. Service
#   → Blog Service
#   → Process requested buisness logic
#   → While processing b.l., If DB is needed → Deliver to DB
# 3. DAO(Data Acess Object)
#   → BlogDAO
#   → DAO processes DB with communicaing DB(CRUD processing)
#   → Deliver the result of executing SQL on DB to Service단
# 4. Service
#   → Deliver the result delivered from DAO to Controller
# 5. Controller
#   → Deliver the result of Service로부터 전달받은 결과와 View(웹 페이지)를 클라이언트에게 전달(Response)


# 선배로서 추천~!
# 1. SQLD 자격증 취득
#   - ORM 개발(SQL 미사용)
#   - SQL 알고 있으면 ORM 더 잘 쓸 수 있음
#   - 복잡한 SQL문은 ORM으로 한계가 있음
#   - AI, 분석 개발(SQL 필수)

# 2. WEB 개발 공부!
#   - 어느 분야로 직업을 정해도 웹개발을 기본적으로 알고 있는 게 도움
#   - Python + WEB + DB = Project
#   - Python Web → Django, Flask, FastAPI
#   * 실제 회사 : Python 웹개발 → Django
#   * FastAPI 추천
#     1. 웹개발(Sprint-JAVA, Node-JS, DJango-Python)
#     2. Django : HARD, FastAPI : EASY

import pandas as pd
from common.connection import commection

# 1. 전체 도서 조회(ALL)
def get_books():
    conn = connection()            # Python ↔ DB
    try:
        curs = conn.cursor()       # cursor : worker
        sql = """
            SELECT * FROM tbl)book;
        """
        curs.execute(sql)               # SQL 실행(도서 전체 데이터 가져옴)
        # DB에서 가져온 전체 데이터 : Dict Type(2차원)
        rows = curs.fetchall()          # SQL 실행결과 받기
        # Dict Type(2차원) → Convert to DataFrame(Table)
        rows = pd.DataFrame(dict_rows)  # 2차원 DataFrame 형태로 변환
    except Exception as e:
        print(e)
    finally:
        if curs:
            curs.close()
        if conn and conn.open:
            conn.close()      
    return rows # rows:데이터베이스에서 받아온 반환값
# 2. 도서 검색
def search_books(keyword:dict):
    conn=connection()
    try:
       curs=conn.cursor()
       sql="""
            select*from tbl_book
            where book_name like %(keyword)s # % 써주면 파이썬 들어간 모든 책 검색해줌
            or book_writer like %(keyword)s
            or book_publisher like %(keyword)s
       """
       curs.execute(sql, {"keyword":"%"+keyword+"%"})
       dict_rows=curs.fetchall()
       rows=pd.DataFrame(dict_rows)
    except Exception as e:
        print(e)
    finally:
        if curs:
            curs.close()
        if conn and conn.open:
            conn.close()   
        return rows

# ※ SQL의 UPDATE문과 DELETE문은 반드시 WHERE절과 함께 사용.**************************************************************************************************
# 3. 도서 등록
def insert_book(book:dict):
    conn=connection()
    try:
       curs=conn.cursor()
       sql="""
           INSERT INTO tbl_book(book_name, book_writer, book_publisher, book_price) 
           VALUES(%(book_name)s,%(book_writer)s, %(book_publisher)s, %(book_price)s); # 실제 데이터
       """
       curs.execute(sql, book)
    except Exception as e:
        print(e)
    finally:
        if curs:
            curs.close()
        if conn and conn.open:
            conn.close()   
    
# 4. 도서 수정
def update_book(book:dict):
    conn=connection()
    try:
       curs=conn.cursor()
       sql="""
        UPDATE tbl_book
        SET book_name=%(book_name)s,
            book_writer=%(book_writer)s,
            book_publisher=%(book_publisher)s,
            book_price=%(book_price)s,
            register_at=%(register_at)s,
            useyn=%(useyn)s
        WHERE book_isbn=%(book_isbn)s; # 얘 없으면 set값이 모든 테이블에 적용되어버림
       """
       curs.execute(sql, book)
    except Exception as e:
        print(e)
    finally:
        if curs:
            curs.close()
        if conn and conn.open:
            conn.close() 


# 5. 도서 삭제
def delete_book(book_isbn:dict):
    pass