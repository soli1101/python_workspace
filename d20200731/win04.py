import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QListView
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon,QPixmap

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    # 방향키를 누르면 lb1이 움직이도록 설정하기
    def goLeft(self):
        print(self.lb1.x(),self.lb1.y())
        self.lb1.move(self.lb1.x()-2, self.lb1.y())
    def goRight(self):
        print(self.lb1.x(),self.lb1.y())
        self.lb1.move(self.lb1.x()+2, self.lb1.y())
    def goUp(self):
        print(self.lb1.x(),self.lb1.y())
        self.lb1.move(self.lb1.x(), self.lb1.y()-2)
    def goDown(self):
        print(self.lb1.x(),self.lb1.y())
        self.lb1.move(self.lb1.x(), self.lb1.y()+2)

    def keyPressEvent(self,e):
        print(e.key())

    def initUI(self):
        self.setWindowTitle("방향키를 만들어요")
        self.resize(800,600)

        # QPixmap 객체
        p_img = QPixmap("./img/turtle.gif") # 객체 생성

        # label 생성
        self.lb1 = QLabel('나',self)
        self.lb1.setPixmap(p_img)

        self.lb1.move(400,100)
            # font 설정
        fontlb1 = self.lb1.font()
        fontlb1.setPointSize(10)
        self.lb1.setFont(fontlb1) 

        # 방향키 생성
        bleft = QPushButton("◀",self)
        bleft.resize(80,80)
        bleft.move(265,350)
        bleft.clicked.connect(self.goLeft)
        
        bright = QPushButton("▶",self)
        bright.resize(80,80)
        bright.move(480,350)
        bright.clicked.connect(self.goRight)

        bup = QPushButton("▲",self)
        bup.resize(80,80)
        bup.move(373,250)
        bup.clicked.connect(self.goUp)

        bdown = QPushButton("▼",self)
        bdown.resize(80,80)
        bdown.move(373,450)
        bdown.clicked.connect(self.goDown)

        self.show()

if __name__=="__main__":
    app=QApplication(sys.argv)
    ex=MyApp()
    sys.exit(app.exec_())
