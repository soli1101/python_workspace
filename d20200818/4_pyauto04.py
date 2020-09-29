#gb_70 : 로그인 버튼의 ID
#로그인 이메일 id: indentifierID

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
import pyperclip

# url = "https://www.naver.com/"
# browser = webdriver.Chrome("e:/dev/python_workspace/chromedriver.exe")
# browser.get(url)

# elem = browser.find_element_by_class_name("link_login")
# elem.click()

# elem = browser.find_element_by_id("id")
# elem.send_keys('munjayerrr')

# elem = browser.find_element_by_id("pw")
# elem.send_keys('munjayerrr')

# browser.find_element_by_class_name("btn_global").click()
# time.sleep(2)

# pyautogui.alert("로그인 완료후 버튼을 클릭하세요")
# browser.maximize_window() # 현재창을 크게 하자

pyautogui.click(616,478)
pyautogui.click(774,529)
pyautogui.click(511,312) # 받는사람
time.sleep(2)
pyperclip.copy("soli110@naver.com")
pyautogui.hotkey("ctrl","v")


pyautogui.click(509,384) # 제목
time.sleep(2)
pyperclip.copy("행운의 편지")
pyautogui.hotkey("ctrl","v")

pyautogui.click(390,520) # 내용
time.sleep(2)
pyperclip.copy("만나면 좋은 친구 우우 임비시 문화방소소소소송")
pyautogui.hotkey("ctrl","v")

time.sleep(2)
pyautogui.click(386,261) # 발송

