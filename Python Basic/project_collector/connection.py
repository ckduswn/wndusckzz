import pymysql
import pymysql.cursors

# 네트워크  
# - IP : 컴 주소!
#    ㄴ 고정 IP
#    ㄴ 유동 IP
#    ㄴ 루프백 IP : 127.0.0.1
# # Python 프로그램과 Database 연결

def connection():
    try:
        conn = pymysql.connect(
            host="127.0.0.1",
            port="3306",
            user="root",
            password="mariadb",
            database="chosun",
            charset="utf8",
            autocommit=True,
            cursorcalss=pymysql.cursors.DictCursor
        )
        return conn
    except pymysql.Error as e:
        print(f"MariaDB 연결실패 : {e}")