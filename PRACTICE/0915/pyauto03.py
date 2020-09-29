'''
화면의 특정 지점으로 이동하기 
글씨쓰기
'''

import pyautogui
import time

pyautogui.moveTo(400,400,0.1)
pyautogui.moveRel(100,100,0.3)

pyautogui.moveTo(551,420,0.1)
pyautogui.click()
pyautogui.click(clicks=2,interval=2)
pyautogui.doubleClick()
time.sleep(1)
pyautogui.moveTo(1132,479)
pyautogui.typewrite("hello")