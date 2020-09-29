import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class MyApp(QWidget):
    def __init__(self):
        super().__init__()  # 부모클래스의 __init__ 상속받기
        self.initUI()       # initUI 함수를 생성해

    def print(self):
        print("버튼이 눌림 왜 눌러!^^")

    # UI 담당 함수 : User Interface
    def initUI(self):
        self.setWindowTitle("와...금요일이다...불금불금") 
        self.resize(800,600)
        self.move(300,400)      
       
        # 푸쉬버튼 인스턴스를 추가
        btn1=QPushButton("출력",self)
        btn1.setText("Print")
        btn1.resize(100,50)
        btn1.move(260,360)
        # Event Handler 특정 이벤트를 처리해 주는 기능
        btn1.clicked.connect(self.print) # self.print라는 함수랑 연결해 줘 라는 뜻

        # 푸쉬버튼 인스턴스를 추가
        btn2=QPushButton("exit",self)
        btn2.setText("exit")
        btn2.resize(100,50)
        btn2.move(460,360)
        btn2.clicked.connect(QCoreApplication.instance().quit)
        
        # 화면에 창을 보여지게 설정
        self.show()  

# 실제 실행하기
if __name__=="__main__":   
    app=QApplication(sys.argv)
    ex=MyApp()
    sys.exit(app.exec_())