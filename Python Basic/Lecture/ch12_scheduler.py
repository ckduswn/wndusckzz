# 스케쥴러
# - 일정시간에 반복적으로 동작 해야 하는 작업을 등록
#   ex) 12시간에 한번씩, 매일 자정 한번씩, 5분에 한번씩, 매월 1일 자정에 한번씩
#       -> CRON 표기법

# 스케쥴러 종류
# 1. scheduler
#    -> 매우 쉬움, 기능 약함
# 2. apscheduler
#    -> 매우 쉬움, 기능 강함

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler

# BackgroundScheduler
# - 메인 작업이 있어야만 동작
# - 백그라운드 즉 서브로 동작하기 때문에

# 메인
# While True
# print("test")
# 서브
# - 스케쥴러 실행

# 1. 스케쥴러 생성
# sched = BlockingScheduler
 sched = BackgroundScheduler

# 2. 할 일 생성
def print_hello():
    print*("Hello")
    
# 3. 스케쥴러 할 일 등록
sched.add_job(print_hello, "cron", hour="17",minute="26", id"chosun")

# 4. 스케쥴러 실행
sched.start()

While True:  
    print("test")
