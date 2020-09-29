import sys
from PyQt5.QtWidgets import *

def quit():
    print("quit() 호출됨")       # sys의 exit를 실행. 0=정상종료
    sys.exit(0)                 # 다른값은 비정상종료(좀 더 빠름 오류로 인식)

app = QApplication(sys.argv)    # app을 생성한 뒤
print(app,sys.argv)             # app을 출력함 # sys.argv는 파일이 있는 경로 

btn=QPushButton("Quit")
btn.show()
btn.clicked.connect(quit)
                                
app.exec_()                     # 이벤트 무한 루프