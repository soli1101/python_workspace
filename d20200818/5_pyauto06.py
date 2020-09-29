from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui

url = "https://www.naver.com/"
browser = webdriver.Chrome("e:/dev/python_workspace/chromedriver.exe")

# 브라우저 열고 네이버로 
browser.get(url)

# 현재창을 크게
browser.maximize_window()

# 검색창 찾아서 클릭하고 내용 입력하기 : query
elem = browser.find_element_by_id("query")
elem.click()
elem.send_keys("종로3가 맛집")
elem.send_keys(Keys.ENTER)

# 아래로 스크롤
time.sleep(2)
pyautogui.scroll(-1200)

for i in range(1,21):
    print("------------------page{}".format(i)) # 페이지 번호출력 

    # 맛집 목록 긁어오기
    ulElem = browser.find_element_by_css_selector("#place_main_ct > div > div > div.sc_box.place_list > div.list_area > ul")
    # print(ulElem)
    lists = ulElem.find_elements_by_css_selector(".list_item.type_restaurant")
    # print(lists)
    for store in lists:
        print(store.find_element_by_css_selector("div.tit > span > a > span").text)
    # 다음페이지로 넘기기
    pyautogui.click(764,874)

time.sleep(4)