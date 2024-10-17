# 주차 타워(앨레베이터)
# -5층으로 제한
# -1층마다 차량 1대만 입고
# - 차량번호는 숫자 4자리 ex)5001

# 기능
# 1. 차량 입고
# 2. 차량 출고
# 3. 차량 조회
# 4. 종료

# 1. 공통 설정
max_car = 5 # 최대 주차 차량 수
cnt_car = 0 # 현재 주차되어 있는 차량 수(count)
 
# 2. 주차 타워 생성 -> list[] -> "" 빈칸
# tower = ["", "", "", "", ""]  # 방법1. 하드코딩(절대 지양)

# 방법2. for문 활용
# tower = []
# for i in range(max_car):
#     tower.append("")
    
# 방법3. 리스트 컴프리헨슨
# 모든 for문을 이거로 변경은 불가. 심플한 거만 ㄱㄴㄸ.
tower = ["" for i in range(max_car)]

# 3. 메뉴 출력
print("="*50)
print("== 주차 타워 시스템 ver 1.0==")
print("="*50)
print("= 1. 차량 입고")
print("= 2. 차량 출고")
print("= 3. 차량 조회")
print("= 4. 종료")
print("="*50)

# 4. 메뉴 선택
# 사용자는 1~4번까지 입력
# 사용자가 입력한 값은 select_num 변수에 저장
# 사용자가 1~4 이외의 값을 넣으면 경고메세지 출력 후 다시 입력 받기

while True:
    select_num = int(input(">> 번호:"))
    if 4 >= select_num >= 1:
        break
    else:
        print("올바른 값을 입력하세요.")
        
      
# 5. 메뉴 서비스
# select_num이 1, 2, 3, 4, 인 경우
if  select_num == 1:
    # 도메인 지식 -> 비즈니스 로직
    # 1. 주차공간 유무 확인
    #    y : 다음스텝 / n : "만차띠예"
    if max_car > cnt_car:    # max_car : 5로 고정. 
        # 2. 차량번호 입력
        #    + 유효성 체크(숫자만, 4자리수만) -> 정규식(re) 공부해올 것!
        num_car = input(">> 차량번호: ")
        # 3. 주차타워 입고(tower[]에 저장)
        #    + 주차타워 빈 공간 서치
        for i in range(max_car):
            if tower[i] == "":
                tower[i] = num_car
                cnt_car += 1
                break
        #    + 빈 공간에 값 저장
        # 4. 현재 주차된 차량 수 최신화 => cnt_car + 1
    
    else:
        print("만차띠예!")
        
       
    elif select_num == 2: # 출고는 숙제
    # 1. 출고 차량 번호 입력 ex) 5789
    # 2. 입력한 번호로 주차타워 검색
    #    y : 다음스텝 / x : "주차되지 않은 차량번호입니다."
    # 3. 차량 출고 -> tower[] -> ""
    # 4. 현재 주차수 - 1
    
    elif select_num == 3:
    pass
# range(시작, 끝, 인터벌) -> range(0, 5, 1)   = 0, 1, 2, 3, 4 
#                        -> range(4, -1, -1) = 4, 3, 2, 1, 0    
    for i in range(max_car-1, -1, -1):
            print(f"{i+1}층: {tower[i]}")
elif select_num == 4:
        print("프로그램을 종료합니다.")
        exit() 

