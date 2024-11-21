import requests
from bs4 import BeautifulSoup
from collect_dao import insert_news

def collect_news():
    count = 1 
    url = "https://news.daum.net/"
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    link_list = doc.select("ul.list_newsbasic a.item_newsbasic") 
# shift + Tab : 앞으로 땡겨
    for link in link_list:
        print(f"{count} ===================================")
        get_news_info(link["href"])
        count+=1

    
def get_news_info():
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
    insert_news(data)