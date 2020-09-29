import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("draw03_선그리기")
        self.setWindowIcon(QIcon("./img/painter.png"))
        self.setGeometry(400,300,800,600)
        self.show()

    def paintEvent(self, e):
        qp = QPainter()             #qp QPainter 인스턴스 생성
        qp.begin(self)              #페인트 준비 시작
        qp.setPen(QPen(Qt.red,10))  #펜설정(빨강색, 10)
        qp.drawLine(100,100,200,200)#drawLine(x1,y1,x2,y2)
        qp.setPen(QPen(Qt.green,10))
        qp.drawLine(200,100,100,200)
        qp.end()                    #페인트 끝

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())