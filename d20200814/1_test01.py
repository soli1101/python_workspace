from bs4 import BeautifulSoup as bs
from pprint import pprint
from pathlib import Path
import requests

url="https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EB%82%A0%EC%94%A8"
res=requests.get(url)
res.raise_for_status()
# pprint(res.text)
soup=bs(res.text,'lxml')
# pprint(soup)

dds = soup.find_all("dd",attrs={"class","lv1"})
# pprint(dds)

# 정의 목록 만들기
# <d1> 정의목록 (Definition List)
#     <dt> 용어 제목 </dt> (Definition Term)
#     <dd> 용어 설명 </dd> (Definition Description)
# </dt>

# 온도 가져오기
temp = soup.find('p',attrs={"class","info_temperature"})
# print(temp)
pprint(temp.get_text())
print('------------------------------')

# 강수량 가져오기
rainfall = soup.find("span",attrs={"class","rainfall"})
# pprint(rainfall)
num2 = rainfall.find("span",attrs={"class","num"})
# pprint(num2)
print(num2.get_text())
print('------------------------------')

for d in dds:
    # print(d)
    num=d.find("span",attrs={"class","num"})
    print(num.get_text())   # get_Text()말고 text도 같은결과출력
    temp
    print('--------------------------')