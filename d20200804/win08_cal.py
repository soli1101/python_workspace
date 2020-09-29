import cx_Oracle
import sys
import math
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")

        # QLineEdit
        self.le = QLineEdit("",self)

        # QPushButton
        self.b7 = QPushButton("7",self)
        self.b8 = QPushButton("8",self)
        self.b9 = QPushButton("9",self)
        self.bp = QPushButton("+",self)

        self.b4 = QPushButton("4",self)
        self.b5 = QPushButton("5",self)
        self.b6 = QPushButton("6",self)
        self.bm = QPushButton("-",self)

        self.b1 = QPushButton("1",self)
        self.b2 = QPushButton("2",self)
        self.b3 = QPushButton("3",self)
        self.bmp = QPushButton("*",self)

        self.b0 = QPushButton("0",self)
        self.b00 = QPushButton("00",self)
        self.beq = QPushButton("=",self)
        self.bdv = QPushButton("/",self)

        # Signal 모음
        self.b7.clicked.connect(lambda : self.func("7"))
        self.b8.clicked.connect(lambda : self.func("8"))
        self.b9.clicked.connect(lambda : self.func("9"))
        self.bp.clicked.connect(lambda : self.func("+"))

        self.b4.clicked.connect(lambda : self.func("4"))
        self.b5.clicked.connect(lambda : self.func("5"))
        self.b6.clicked.connect(lambda : self.func("6"))
        self.bm.clicked.connect(lambda : self.func("-"))

        self.b1.clicked.connect(lambda : self.func("1"))
        self.b2.clicked.connect(lambda : self.func("2"))
        self.b3.clicked.connect(lambda : self.func("3"))
        self.bmp.clicked.connect(lambda : self.func("*"))
        
        self.b0.clicked.connect(lambda : self.func("0"))
        self.b00.clicked.connect(lambda : self.func("00"))
        self.bdv.clicked.connect(lambda : self.func("/"))
        ## = 은 실제 연산을 시켜주는 함수 cal과 연결시킨다
        self.beq.clicked.connect(self.cal)

        # QGridLayout
        grid = QGridLayout()
        self.setLayout(grid)

        '''grid를 for문으로 돌려서 만드는 방법'''
        # gridList = []                
        # cnt = 0
        # for i in range(1,3):
        #     for j in range(0,4):
        #         grid.addWidget(gridList[cnt],i,j)
        #         cnt +=1

        grid.addWidget(self.le,0,0,1,4)
        
        grid.addWidget(self.b7,1,0)
        grid.addWidget(self.b8,1,1)
        grid.addWidget(self.b9,1,2)
        grid.addWidget(self.bp,1,3)

        grid.addWidget(self.b4,2,0)
        grid.addWidget(self.b5,2,1)
        grid.addWidget(self.b6,2,2)
        grid.addWidget(self.bm,2,3)

        grid.addWidget(self.b1,3,0)
        grid.addWidget(self.b2,3,1)
        grid.addWidget(self.b3,3,2)
        grid.addWidget(self.bmp,3,3)

        grid.addWidget(self.b0,4,0)
        grid.addWidget(self.b00,4,1)
        grid.addWidget(self.beq,4,2)
        grid.addWidget(self.bdv,4,3)

        self.show()

    # 많이 사용하는 내장 이벤트
    # -----------------------#
    # def keyPressEvent(self,e):   # 계속 누르고 있으면 동작한다
    #     print("키보드가 눌릴 때")   
    # def keyReleaseEvent(self,e):
    #     print("키보드를 땔 때")   # 오직 땔 때만 동작한다
    # def mouseMoveEvent(self,e):
    #     print("마우스를 움직일 때 호출")
    # def mouseDoubleClickEvent(self,e):
    #     print("마우스를 더블클릭 했을 때")
    # def resizeEvent(self,e):
    #     print("위젯의 크기를 변경할 때 호출")
    # def mousePressEvent(self,e):
    #     print(e)
    # -----------------------#
    
    # 해당 버튼을 클릭하면 line창에 뜨게 하는 함수
    def func(self,txt):
        self.le.setText(self.le.text()+txt)

    # 실제 계산으로 바꿔주는 함수
    # eval 식을 정말 연산식으로 처리해 주는 함수     
    def cal(self): 
        self.le.setText(str(eval(self.le.text())))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Calculator()
    sys.exit(app.exec_())