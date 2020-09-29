import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint
from pathlib import Path

headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}

# 1230 ~ 1237화 까지 받아서 회차별 폴더에 저장해보자!!
for i in range(1230,1237):
    url = "https://comic.naver.com/webtoon/detail.nhn?titleId=20853&no={}&weekday=tue".format(i)
    res=requests.get(url)   #url에서 하이퍼링크를 요청해서 가져와! 정상이면 200표시됨
    res.raise_for_status()  #정상적으로 작동하면 실행해

    soup = bs(res.text,'lxml')
    data = soup.find('div',attrs={"class","wt_viewer"})
    print(data)
    images = data.findAll("img")
    # pprint(images)      --> resultset으로 보여줌
    for img in images:  # --> 1개씩 값을 따로 출력함 
        pprint(img['src'])
        path = img['src']
        # print(path[46:50])  #회차만 따오기
        res2 = requests.get(path, headers=headers)
        # print(res2)
        #별도디렉토리를 만들고 그 장소에 이미지파일을 저장
        Path("./img/"+path[46:50]).mkdir(parents=True,exist_ok=True)
        with open("./img/"+path[46:50]+"/"+path[-12:],'wb') as f:
            f.write(res2.content)