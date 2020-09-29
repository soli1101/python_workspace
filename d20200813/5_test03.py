import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint

url = "https://comic.naver.com/webtoon/list.nhn?titleId=20853"
res=requests.get(url)   #url에서 하이퍼링크를 요청해서 가져와! 정상이면 200표시됨
res.raise_for_status()  #정상적으로 작동하면 실행해
res.close()             #자원반납
soup = bs(res.text,'lxml')

 #함수를 이용한 접근
print('----()의 조건에 해당하는 걸 다 찾아줘----') 
tdList= soup.find_all("td",attrs={"class","title"})
print(tdList,type(tdList))
print(tdList[0].find('a').get_text())
for i in tdList:
    print(i.find('a').get_text())