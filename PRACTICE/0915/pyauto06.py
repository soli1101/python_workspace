from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
from pathlib import Path

url="https://www.naver.com"
browser=webdriver.Chrome("e:/dev/python_workspace/chromedriver.exe")

browser.get(url)

browser.maximize_window()

elem=browser.find_element_by_id("query")
elem.click()
elem.send_keys("종로3가맛집")
elem.send_keys(Keys.ENTER)

time.sleep(2)
pyautogui.scroll(-1200)

Path("./rtrlist").mkdir(parents=True,exist_ok=True)
rtrlist=list()
with open("./rtrlist/stores.txt",'a')as f: 
    for i in range(1,21):
        print("--------page{}".format(i))
        ulElem=browser.find_element_by_css_selector('#place_main_ct > div > div > div.sc_box.place_list>div.list_area>ul')
        lists=ulElem.find_elements_by_css_selector(".list_item.type_restaurant")
        for store in lists:
            # print(store.find_element_by_css_selector("div.tit>span>a>span").text)
            f.write(store.find_element_by_css_selector("div.tit>span>a>span").text,sep=",")
        pyautogui.click(766 , 874)






time.sleep(3)