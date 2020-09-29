'''
화면의 특정지점 좌표 이미지로 찾기
'''

import pyautogui

i = pyautogui.locateOnScreen('e:/dev/python_workspace/pyauto02.png')
print(i)

# pyautogui.screenshot("pyauto02.png",region=(92,203,217,224))

pos = pyautogui.center(i)
pyautogui.click(pos)
