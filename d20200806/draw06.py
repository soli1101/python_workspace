import sys
from random import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import threading

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("draw03_선그리기")
        self.setWindowIcon(QIcon("./img/painter.png"))
        self.setGeometry(400,300,800,800)
        self.show()

    def paintEvent(self, e):
        qp = QPainter()             #qp QPainter 인스턴스 생성
        qp.begin(self)              #페인트 준비 시작

        for k in range(1000):
            red = randint(1,256)
            green = randint(1,256)
            blue = randint(1,256)
            pointsize = randint(1,25)
            x1 = randint(1,800)
            y1 = randint(1,800)
            x2 = randint(1,800)
            y2 = randint(1,800)
        
            qp.setPen(QPen(QColor(red,green,blue),3))  #펜설정(빨강색, 10)
            qp.drawLine(x1,y1,x2,y2)

        qp.end()                    #페인트 끝

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())