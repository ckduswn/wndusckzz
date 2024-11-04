import requests
from bs4 import BeautifulSoup
from fnc_news import get_news_info

page = 1
while True:
    url = "https://news.daum.net/breakingnews/digital?page=1"
    print(url)
    page+=1
    
    if page == 4:   
        break

