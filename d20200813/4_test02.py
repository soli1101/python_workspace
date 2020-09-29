import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint

url = "https://comic.naver.com/webtoon/list.nhn?titleId=20853"
res=requests.get(url)   #url에서 하이퍼링크를 요청해서 가져와! 정상이면 200표시됨
res.raise_for_status()  #정상적으로 작동하면 실행해
res.close()             #자원반납
# pprint(res.text)        #페이지소스를 완전히 보여줌 \t \n
soup= bs(res.text,'lxml') #res.text를 lxml해석기로 해석해줘 
# print(soup, type(soup)) #\t 이런건 제거하고 보여줌
print(soup.title)         #title인 애를 꺼내줘
print()
print('----하지만 우린 내용이 필요해...----')
print()
print(soup.title.get_text())   
print()
print('----soup객체에서 처음 발견되는 a element 출력----')
print()
print(soup.find("a")) 
print()
print('----a태그의 속성을 가져와----')
print()
print(soup.a.attrs) 
print()
print('----문서내에href라는 속성값을 꺼내옴----')
print()
print(soup.a.attrs['href'])
print()
print('----함수를 이용한 접근----')
print()
print(soup.find("td",attrs={"class","title"})) 
print()
print('----td에서 속성중에 class의 값이 title인 애들을 찾아줘----')
title1 = soup.find("td",attrs={"class","title"})
print()
a = title1.find('a')
print(a)
print()
print('----a에서 text()만 가져와----')
print()
print(a.get_text())


# print(res)
# print(res.status_code)
# print(res.text)