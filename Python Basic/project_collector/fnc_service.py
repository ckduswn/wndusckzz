import requests
from bs4 import BeautifulSoup
from collect_dao import insert_news
# 아래는 ch05_selenium에서 갖다붙인 거심.
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



def collect_news():
    count = 0 
    url = "https://news.daum.net/home"
    driver = webdriver.Chrome(options=options)
    driver.get("url")
    print(driver.page_source) 
    time.sleep(5)
    
    # 중복 방지 체크 숙제 : 1p(9art) → Total 3p(27art) → collect only one time(27art)
    # logic
    # 1. collecting next art URL and url_list's URL 
    # 2. complete to collection 1 art → save that art URL on url_list

    while True:
    # 9건의 기사 수집
        doc = BeautifulSoup(driver.page_source, "html.parser")
        link_list = doc.select("article.content-article ul.list_newsheadline2 a.item_newsheadline2") 
    # shift + Tab : 앞으로 땡겨
        for link in link_list:
            print(f"{count} ===================================")
            get_news_info(link["href"])
            count+=1
        # 뉴스 새로고침 버튼 클릭
        driver.find_element(By.XPATH,'').click()
        time.sleep(1)
    
def get_news_info(url:str):
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    title = doc.select("h3.tit-view")[0].get_text()
    contents = doc.select("section > p")
    content = ""
    for text in contents:
         content += text.get_text()
    
    writer_list = doc.select("span.txt_info") 
          
    if len(writer_list) < 2:
         writer = ""
    else:
        writer = writer_list[0].get_text()
            
        
    reg_date = doc.select("span.num_date")[0].get_text()
    list_date = reg_date.split(". ")
    # list_date = list(map(lambda x : x.strip(), list_date))
    reg_date = list_date[0] + list_date[1] + list_date[2]   
    print(f"뉴스 제목 : {title}")
    print(f"뉴스 기자 : {writer}")
    print(f"뉴스 본문: {content}")
    print(f"뉴스 날짜 : {reg_date}")  

    data={
        "title" : title,
        "writer" : writer,
        "content" : content,
        "regdate" : reg_date,
    }
    # insert_news(data) # DB에 안 넣을 땐 주석처리
    
collect_news()