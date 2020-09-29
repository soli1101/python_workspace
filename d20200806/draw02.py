import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("draw02_점찍기")
        self.setWindowIcon(QIcon("./img/painter.png"))
        self.setGeometry(400,300,800,600)
        self.show()

    def paintEvent(self, e):
        qp = QPainter()             #qp QPainter 인스턴스 생성
        qp.begin(self)              #페인트 준비 시작
        qp.setPen(QPen(Qt.blue,8))  #펜설정(펜객체(파랑색,8px))
        qp.drawPoint(self.width()/2, self.height()/2)   #펜위치(화면너비의 절반, 화면높이의 절반)
        qp.end()                    #페인트 끝

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())