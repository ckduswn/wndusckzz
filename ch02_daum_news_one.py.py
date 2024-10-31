import requests
from bs4 import BeautifulSoup
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
title = doc.select("h3.tit-view")[0].get_text()
contents = doc.select("section > p")
content = ""
for text in contents:
    content += text.get_text()
writer = doc.select("span.txt_info")[0].get_text()
reg_date = doc.select("span.num_date")[0].get_text()
 # 2024. 10. 28. 16:40
# 1. [0:5] [6:8] etc 연월일 뽑기 : 지양
# 2. "." 구분자 기준으로 split 이용..단독 strip() : 지양, 반복이니까 
list_date = reg_date.split(". ")
# reg_date = list_date[0] + list_date[1].strip() + list_date[2].strip()
# print(reg_date)
# 3. 리스트 컴프리핸션
# ["년", " 월", " 일", " 시간"]
# list_date = [x.strip() for x in list_date]
# 4. lambda식
#  - map, reduce, filter
# list_date = list(map(lambda x : x.strip(), list_date))
reg_date = list_date[0] + list_date[1] + list_date[2]   

exit()
print(f"뉴스 제목 : {title}")
print(f"뉴스 기자 : {writer}")
print(f"뉴스 날짜 : {reg_date}")  # > 20241028
print(f"뉴스 본문: {content}")

print("="*50)
print(f"뉴스 제목 : {title}")
print("="*50)

