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
        self.setWindowTitle("draw07_텍스트그리기")
        self.setWindowIcon(QIcon("./img/painter.png"))
        self.setGeometry(400,300,650,400)
        self.show()

        
    def paintEvent(self, e):
        qp = QPainter()             #qp QPainter 인스턴스 생성
        qp.begin(self)              #페인트 준비 시작

        qp.setPen(QColor(0,0,0))
        qp.setFont(QFont("나눔고딕", 50)) #setFont(QFont("폰트명",크기))
        qp.drawText(100,100,"미라미라 쾅쾅쾅") #drawText(x1,y1,"글내용")
        
        self.drawOther(qp)          #함수로 빼서 만들어 주기

        qp.end()                    #페인트 끝

    def drawOther(self,qp):         
        pen = QPen(Qt.black, 3, Qt.SolidLine) # pen 객체 생성
        qp.setPen(pen)                        # pen 설정
        qp.drawLine(50,50,100,50)             

        pen.setStyle(Qt.DashLine)   # pen스타일설정
        qp.setPen(pen)              # 다시 pen 설정 변경 적용
        qp.drawLine(200,50,300,150)

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())