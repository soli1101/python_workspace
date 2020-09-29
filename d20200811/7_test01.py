# Web Crawling
' Web Site를 정기적으로 돌며 정보를 추출하는 기술'
' ==> DB'

# Web Scraping
' Web Site에서 특정 정보를 추출하는 기술'

# Web 
' HTML, CSS, JavaScript '

import requests

res = requests.get("http://google.com")
print(res)

# <Response [200]> = 정상 호출 (HTTP.status)
# <Response [403]> = 권한없음 
# <Response [404]> = 페이지를 찾을 수 없음, url 오류(Uniform Resource Location)
# <Response [500]> = 서버사이드 로직 에러, 개발중, 갱신중 

'''
if res.status_code == requests.codes.ok:
    print(len(res.text))
'''
# 에러가 있으면 에러 메세지를 출력하고 바로 종료
res.raise_for_status() 

with open("google.html","w",encoding="utf-8") as f:
    f.write(res.text)