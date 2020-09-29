from selenium import webdriver
import pyautogui
import time
import pyperclip


url = "https://www.google.com/"
browser = webdriver.Chrome("e:/dev/python_workspace/chromedriver.exe")
browser.get(url)

# 종로3가 맛집 리스트에 접근하기
pyautogui.click(319,474)
pyperclip.copy("종로3가맛집")
pyautogui.hotkey("ctrl","v")
pyautogui.click(431,560)
time.sleep(2)
pyautogui.click(304,901)

# 맛집 리스크 긁어오기
for i in range(11):
    elem = browser.find_element_by_css_selector(".rlfl__tls.rl_tls")
    lists = elem.find_elements_by_css_selector(".dbg0pd")
    pyautogui.click(359,831)
    for store in lists:
        print(store.find_element_by_css_selector("div.dbg0pd > div").text)
    pyautogui.scroll(-2400)
    time.sleep(1)

# 선생님께 여쭤보기.. 에러발생하는 이유
# --> 완료... 스크롤과 클릭하는 시점의 문제
# time.sleep(1000)