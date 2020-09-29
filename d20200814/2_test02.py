# selenium
# 웹 브라우저의 자동화를 가능하게 하는 다양한 도구와 라이브러리 포함하는 모듈
# 브라우저 버젼 확인 : 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 크롬 드라이버 객체를 생성
browser= webdriver.Chrome("e:/dev/python_workspace/chromedriver.exe")

# 브라우저 객체로 네이버 웹페이지 접속
browser.get("http://www.naver.com")

# 검색창 엘리먼트 객체 
element=browser.find_element_by_id("query")
time.sleep(3)
element.click()
element.send_keys("파이썬 카드게임")
element.send_keys(Keys.ENTER)

# 3초후 구글로 이동
time.sleep(3)
browser.get("http://www.google.com")
element =browser.find_element_by_name("q")

# 엘리먼트를 클릭
element.click()

# 검색키워드를 입력
element.send_keys("광복절")
element.send_keys(Keys.ENTER)
time.sleep(3)
element.click()
element.send_keys(Keys.BACKSPACE)
element.send_keys(Keys.BACKSPACE)
element.send_keys(Keys.BACKSPACE)
element.send_keys("빨간날")
element.send_keys(Keys.ENTER)
