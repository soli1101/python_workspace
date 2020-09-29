import sys
from random import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("draw04_사각형그리기")
        self.setWindowIcon(QIcon("./img/painter.png"))
        self.setGeometry(400,300,800,600)
        self.show()

    def paintEvent(self, e):
        qp = QPainter()             #qp QPainter 인스턴스 생성
        qp.begin(self)              #페인트 준비 시작
        
        qp.setBrush(QColor(200,80,70))

        qp.setPen(QPen(QColor(100,100,100),5)) #펜설정(회색, 5)
        qp.drawRect(30,30,100,150)  #drawRect(x1,y1,너비,높이)
        
        qp.setPen(QPen(Qt.red,10))  #펜설정(빨강, 10)
        qp.drawLine(250,30,700,30)

        qp.setBrush(QColor(100,100,70))
        qp.setPen(QPen(Qt.blue,5))  #drawRect(x1,y1,너비,높이)
        qp.drawRect(250,100,80,80)
        
        qp.setBrush(QColor(100,255,70))
        qp.setPen(QPen(Qt.blue,5))
        qp.drawRect(440,100,80,80)
        
        qp.setBrush(QColor(200,20,70))
        qp.setPen(QPen(Qt.blue,5))
        qp.drawRect(620,100,80,80)
        
        qp.setPen(QPen(Qt.green,10)) #펜설정(초록, 10)
        qp.drawLine(250,260,700,260)
        
        qp.end()                    #페인트 끝

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())