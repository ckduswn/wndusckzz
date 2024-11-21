# 예외(exception) 처리

# ** 예외
# - 프로그램을 개발하면서 예상치 못한 상황
#   ex) 사용자 입력 오류
# - 예외가 발생하면 프로그램이 종료됨.(크리티컬 상황)
#   -> 에외처리를 하면 예외가 발생해서 동작 가능
# - 예외처리는 의무는 아님!(개발자 맘)
#   -> 파일 시스템과 데이터베이스는 반드시 예외 처리

# cf) 예외상황은 사용자로부터 많이 발생!
#    ex)"-없이 전화번호를 입력하세요."
#         ㄴ사용자1:010-1287-1287
#         ㄴ사용자2:010-1287-ㄴㄴㄴ
#         ㄴ사용자3:111-1111-1111
#         ㄴ개발자:01050011287

# -> 유효성 체크 : 사용자가 입력한 값에 대한 체크
#    1. 확장자 체크
#    2. 파일 이름 체크
#    3. 파일 사이즈 체크

# ** 예외 종류
# 1. 예측 가능한 예외
#    = 발생 여부를 개발자가 사전에 인지 -> 예외 처리
# 2. 예측 불가능한 예외
#    - 카카오톡 서버에 화재로 인해 카카오톡 서비스 중지

# 번외.
# cf) 정부통합전산센터
#     1. 메인(대전)
#     2. 서브(광주)
#     3. 서브(대구)

# ** 개발자 취업
#    1. SI(시스템 통합)
#       - 회사 자체 프로그램 개발 X
#       - 사업을 수주 -> 사업 관련 프로그램 개발
#         하드웨어+소프트웨어
#    2. 솔루션
#       - 회사 자체 프로그램(당근, 한컴,...)
# SI 기업
# 1. "정부통핪전산센터" 사업 발주
#    -> "2024년도 데이터 이전 사업", 1년, 20억
# 2. 다수의 기업들이 사업제안서 참여
#    -> 심사를 통해 회사 선별 
# 3. 선별(중견 기업)
#    -> 대신정보통신(400명)
#            |
#         1하청업체
#            |
#         2하청업체
#            |
#         3하청업체
#
# 4. 정부통합전산센터 사무실 -> 해당 사업 방을 만들고
# -> 대신, 1하청, 2하청, 3하청 : 1년 동안 개발

# 1. 예외 기본 문법
#try:
#    예외가 발생할 수 있는 코드
#except:
#    예외처리
#else:
#    예외가 발생하지 않은 경우 실행되는 코드
#finally:
#    예외 유무와 상관없이 실행되는 코드

# else, finally는 생략 가능
from urllib.request import urlopen, HTTPError
# except HTTPError: -> 예외중 HTTPError 관련 예외만 처리
# except HTTPError: -> 다수의 예외 처리
# except HTTPError:
# except HTTPError:
# except: -> 모든 예외 처리
#try:
#    html urlopen("http://www.naver.com")
#except: HTTPError as e:
#    print(e)  ## 예외처리X, 예외 관련 내용 출력
#else:
#    print("No Error")
#finally:
#    print("자원해제")
    
    
try:
    html urlopen("http://www.naver.com")
except: 
    print("올바른 URL을 입력해주세요.")  ## 예외처리
else:
    print("No Error")
finally:
    print("자원해제")
    