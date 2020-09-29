import sys

from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import time

class MyWindow2(QMainWindow):
    def __init__(self, parent): # 
        super().__init__(parent)
        self.setGeometry(400,300,200,232)
        # image 객체 생성하기 
        merong_img = QPixmap('./img/merong2.png')
        # label 만들어서 image입히기
        self.lb1 = QLabel("merong",self)
        self.lb1.setPixmap(merong_img)
        self.lb1.setGeometry(0,0,200,232)
        self.show()

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "나의 윈도우"
        self.setGeometry(200,200,500,400)
        
        self.btn1 = QPushButton("비법자소서보기",self)
        self.btn1.move(200,200)
        self.btn1.setToolTip("<h3>날 눌러봐!!</h3>")
        self.btn1.clicked.connect(self.newWindow)
        
        self.show()

    def newWindow(self):
        for i in range(2):
            time.sleep(0.2) # 지연 
            self.nw = MyWindow2(self)
            self.nw.q = QLabel("이건 몰랐지?",self)
            self.nw.move(10+i*30,10+i*20)
            self.nw.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    sys.exit(app.exec_())