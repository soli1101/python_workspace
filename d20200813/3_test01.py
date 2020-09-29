import requests


url = "http://www.naver.com"

res=requests.get(url)

print(res)
print(res.status_code)
print(res.text)