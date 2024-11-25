# SELENIUM
# - 설치 : pip install selenium
# - 웹 크롤링(정적, 동적 모두 가능) + 자동화
#       ㄴ SELENIUM이 제어할 수 있는 웹 브라우저 사용
# ㄴ 과거에 웹브라우저 테스트 도구!

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# 디폴트 : SELENIUM 코드 종료 → 웹브라우저 종료
# 1. 셀레니움 웹브라우저 설정
options = Options()
options.add_experimental_option("detach", True) # 웹 브라우저 종료 X, 개발 완료 시 삭제.
# options.add_argument("headless") # 셀레니움 백그라운드 동작(개발 완료 시 사용. 지금은 작동하는지 계속 확인해야 하니까 사용하디망.)


# ※ 셀레니움이 로봇이 아닌 척 하는 방법(로봇인 거 걸리면 페이지가 수집 거부하는 경우 있음.)
options.add_argument("disable-blink-features=AutomationContralled")
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])


# ※ 셀레니움 4버전 이하에서는 ChromeDriver를 설치해서 사용!
#    4버전부터는 설치할 필요 없음!
#    service = Service(ChromeDriverManager().install())

# 2. 셀레니움 웹브라우저 생성
driver = webdriver.Chrome(options=options)

# 3. 셀레니움 웹브라우저 사용
driver.get("https://www.naver.com")
print(driver.page_source) # → 네이버 메인페이지 소스코드. 인터넷 느린 곳에서 뜨다 만 화면에 실행하면 뜨다 만 만큼만 가져옴. 이를 방지하고자 import time과 아래 코드를 사용.
time.sleep(5) # 페이지 로딩 다 될 때까지 5초 기달뤼걸아.

search = driver.find_element(By.ID,"query")
search.send_keys("정우성")
search.send_keys(Keys.ENTER)

# 현재 페이지 정보 가져오기(request는 첫 화면에서 보이는 한정된 개수만 수집. 정적이다. selenium은 동적이라 새로고침시 나오는 기사들까지 수집.)
# 현재 웹브라우저 페이지의 소스코드 GET
print(driver.page_source) # 정우성 검색 네이버 페이지 소스코드. 어느 페이지에서 실행하냐에 따라 가져오는 페이지 소스가 다르다. selenium의 동적 기능.
# + BeautifulSoup