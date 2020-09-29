import pyautogui
# 이미지로 클릭하기

# pyautogui.screenshot("blog2.png", region=(49,274,52,24))
i = pyautogui.locateOnScreen("e:/dev/python_workspace/img/blog.png")
print(i)

#Q버튼 중간쯤 클릭
pos = pyautogui.center(i)
pyautogui.click(pos)
