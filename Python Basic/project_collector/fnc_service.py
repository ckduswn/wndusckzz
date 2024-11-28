import requests
from bs4 import BeautifulSoup
from collect_dao import insert_news
# 아래는 ch05_selenium에서 갖다붙인 거심.
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd

# 디폴트 : SELENIUM 코드 종료 → 웹브라우저 종료
# 1. 셀레니움 웹브라우저 설정
options = Options()
# options.add_experimental_option("detach", True) # 웹 브라우저 종료 X, 개발 완료 시 삭제.
options.add_argument("headless") # 셀레니움 백그라운드 동작(개발 완료 시 사용. 지금은 작동하는지 계속 확인해야 하니까 사용하디망.)
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

    url_list=[] # 수집이 완료된 Link(URL) 저장
    flag = False # while문 빠져나오기 위한 변수
    news_list=[] # 
    while True:
    # 9건의 기사 수집
        doc = BeautifulSoup(driver.page_source, "html.parser")
        link_list = doc.select("article.content-article ul.list_newsheadline2 a.item_newsheadline2") 
    # shift + Tab : 앞으로 땡겨
        for link in link_list:
            # 중복수집 체크
            if link in url_list:
                flag=True
                break
            print(f"{count} ===================================")
            news = get_news_info(link["href"]) 
            news_list.append(news) # 수집한 데이터 로컬 저장
            count+=1
            url_list.append(link) # 중복수집 방지를 위한 처리
        if flag: #  if flag == True:를 이렇게 줄이도록 / 0은 False, 그외의 수는 다 True.
            break
        # 뉴스 새로고침 버튼 클릭
        driver.find_element(By.XPATH,'').click()
        time.sleep(1)
        
        # 수집한 데이터 27건 main으로 전달
        # 1. DB 활용
        #   - DB(27건 저장) → SELECT 가져와서 전달
        # 2. 수집시 수집데이터를 따로 저장 후 전달 news_list → [{news1}, {news2},...]
        # "pandas"의 DataFrame(표) Type으로 news_list 변환
        col_name = ["title", "writer", "content", "regdate"]
        df_news=pd.DataFrame(news_list, columns=col_name) # DataFrame(표) 변환
    return df_news, count
    
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
    insert_news(data) # DB에 안 넣을 땐 주석처리 
    return data
collect_news()