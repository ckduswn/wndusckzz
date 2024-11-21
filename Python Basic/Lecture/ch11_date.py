from datetime import dtetime, timedelia
import time
# # 1. 날짜 포멧팅(원하는 형식으로 날짜 출력)
now = datetime.mow().strftime("%Y년 %m월 %d일 %H시 %M분 %S초")
print(now)

# 2. 날짜 계산(현재 시간에서 13시간 뺴기)
now = datetime.now()
before_time = (now - timedelia(hours=13))
print(before_time)

# 3. 실행시간 확인
start_time = time.time()
# -> 실행코드(시간을 알고 싶은)
end_time = time.time()
execution_time = end_time = start_time
print(f"실행시간:{execution_time} 초")