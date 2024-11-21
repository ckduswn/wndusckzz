# 데이터 베이스 선택
USE chosun;
# 대문자 : SQL 문법

# 테이블 삭제
# - CASCADE(연쇄반응) + DROP = 연쇄삭제
#      ㄴ 관련 있는 거 모두 삭제
DROP TABLE IF EXISTS tbl_news CASCADE;

# 테이블 생성
# STRING(문자열)    → CHAR, VARCHAR(variable character)
# - CHAR(10)      → | a | b | c |   |   | → 안 써도 빈 칸까지 표현. 메모리 낭비.
# - VARCHAR(10)   → | a | b | c |
# → VARCHAR(200) - 200이 무어냐. 해당 컬럼 입력값의 최대 길이(Byte)
# 영문(2Byte), 한글(3Byte)
# 고정길이 문자열 → CHAR
# 가변길이 문자열 → VARCHAR
# DATETIME → 날짜(년, 월, 일, 시, 분 다 들 어 가 야 Damn)
# AUTO_INCREMENT → 자동으로 count(+1) 값 입력, 사용 시 중복값 발생X
# (PK) → 테이블의 모든 값을 유일하게 식별

CREATE TABLE tbl_news(
	id           INT AUTO_INCREMENT PRIMARY KEY,
	title        VARCHAR(200),
	writer       VARCHAR(50),
	content      VARCHAR(10000),
	regdate      VARCHAR(50)
);

# 테이블 조회 
SELECT*FROM tbl_news;