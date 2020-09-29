from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests
from pathlib import Path

'''베스트셀러 리스트 가져오기'''

url = "http://www.yes24.com/24/category/bestseller?CategoryNumber=001&sumgb=06"
res = requests.get(url)
res.raise_for_status()
# pprint(res.text)
soup = bs(res.text, 'lxml')
# pprint(soup)
divs=soup.find_all('div',attrs={"class","goodsImgW"})
# pprint(divs)

idx=0

for i in divs:
    pprint(i)

    #(1) bookNo 구하기 
    print("-------------------------")
    a_tag=i.find('a')
    bookNo=a_tag['href'].split('/')[-1]
    
    #(2) 책제목과 이미지주소 구하기
    url2="http://www.yes24.com/Product/Goods/{}".format(bookNo)
    # print(url2)
    res2=requests.get(url2)
    # pprint(res2)
    soup2=bs(res2.text,'lxml')
    em=soup2.find('em',attrs={"class","imgBdr"})
    img=em.find('img')

    bookTitle=img['alt'] #==> 책제목
    imgPath=img['src'] #==> 이미지주소
    print(imgPath)

    #(3) 구한 img url을 서버에 요청하기 
    res3=requests.get(imgPath)
    print(res3)
    # res3.raise_for_status()
    # res4.raise_for_status()


    #(4) 파일로 저장하기
    idx+=1
    Path("./img/book_cover").mkdir(parents=True,exist_ok=True)
    with open("./img/book_cover/{}.jpeg".format(bookTitle),'wb') as f:
        f.write(res3.content)
