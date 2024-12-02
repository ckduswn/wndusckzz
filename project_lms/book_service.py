# Back-end pattern
# Controller → Service → DAO → Database

# Service단
# - 실제 비즈니스 로직 기능 구현

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
        curs.execute(sql)          # SQL 실행
        rows = curs.fetchall()     # SQL 실행결과 받기
        rows = pd.DataFrame(rows)  # 2차원 DataFrame 형태로 변환
    except Exception as e:
        print(e)
    finally:
        if curs:
            curs.close()
        if conn and conn.open:
            conn.close()
        
    return rows # rows:데이터베이스에서 받아온 값
# 2. 도서 검색
def search_books(keyword:dict):
    pass
# 3. 도서 등록
def insert_book(book:dict):
    pass
# 4. 도서 수정
def update_book(book:dict):
    pass
# 5. 도서 삭제
def delete_book(book_isbn:dict):
    pass