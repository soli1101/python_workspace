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
        qp.drawEllipse(QPointF(220.0,220.0),100,200)
          #drawEllipse(QPointF(x,y),가로너비,세로너비)
        
        qp.setPen(QPen(Qt.blue,10))  #펜설정(빨강색, 10)
        qp.drawEllipse(QPointF(580.0,220.0),200,100)

        qp.end()                    #페인트 끝

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())