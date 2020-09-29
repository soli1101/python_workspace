import pyautogui
import time

pyautogui.moveTo(400,400,0.1)     # 해당위치로 1초마다 가라 절대위치
pyautogui.moveRel(100,100,0.1)    # 상대위치 3초마다 지금 지점에서 해당 거리만큼 움직여라

pyautogui.moveTo(551,420,0.1)
pyautogui.click()                       # 클릭해
pyautogui.click(clicks=2, interval=2)   # 2의 간격을 두고 2번 클릭해
pyautogui.doubleClick()         # 더블클릭하기
time.sleep(1)                   # 1초 잠들기...zzz
pyautogui.moveTo(1132,479)

pyautogui.typewrite("hello")    # hello를 키보드로 입력하기(입력할 수 있는 창이 있어야 확인가능)

