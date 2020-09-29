import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from random import *
import time

class myLotto(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowIcon(QIcon("./img/lotto/q.jpg"))
        self.setWindowTitle("Lotto를 해 봅시당~다라당당당")
       
        # 화면에 표시할 Label 생성
        self.label1 = QLabel("1",self)
        self.label2 = QLabel("2",self)
        self.label3 = QLabel("3",self)
        self.label4 = QLabel("4",self)
        self.label5 = QLabel("5",self)
        self.label6 = QLabel("6",self)
        
        # label에 ? 그림 입혀주기
        self.px = QPixmap('./img/lotto/q.jpg')
        self.label1.setPixmap(self.px)
        self.label2.setPixmap(self.px)
        self.label3.setPixmap(self.px)
        self.label4.setPixmap(self.px)
        self.label5.setPixmap(self.px)
        self.label6.setPixmap(self.px)

        # 새로고침할 버튼생성하기
        self.btn = QPushButton("★대박로또번호★",self)
        self.btn.clicked.connect(self.pause)
        
        # QboxLayout
        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(self.label1)
        hbox1.addStretch(1)
        hbox1.addWidget(self.label2)
        hbox1.addStretch(1)
        hbox1.addWidget(self.label3)
        hbox1.addStretch(1)
        hbox1.addWidget(self.label4)
        hbox1.addStretch(1)
        hbox1.addWidget(self.label5)
        hbox1.addStretch(1)
        hbox1.addWidget(self.label6)
        hbox1.addStretch(1)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(2)
        hbox2.addWidget(self.btn)
        hbox2.addStretch(2)

        vbox = QVBoxLayout()
        vbox.addStretch(2)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        
        self.setLayout(vbox)

        self.show()
    def pause(self):
        
        # ball1~45개 picutre란 이미지에 주소값 담아주기
        self.pictures = []
        for i in range(1,46):
            self.pictures.append("./img/lotto/ball{}.png".format(i))
        
        # 6개의 ball을 추출할 객체 생성하기
        self.px_1 = QPixmap(choice(self.pictures))
        self.px_2 = QPixmap(choice(self.pictures))
        self.px_3 = QPixmap(choice(self.pictures))
        self.px_4 = QPixmap(choice(self.pictures))
        self.px_5 = QPixmap(choice(self.pictures))
        self.px_6 = QPixmap(choice(self.pictures))

        # label에 ball 이미지 입히기
        self.label1.setPixmap(self.px_1)
        self.label2.setPixmap(self.px_2)
        self.label3.setPixmap(self.px_3)
        self.label4.setPixmap(self.px_4)
        self.label5.setPixmap(self.px_5)
        self.label6.setPixmap(self.px_6)
       
        time.sleep(1)            

if __name__=="__main__":
    app = QApplication(sys.argv)
    m = myLotto()
    sys.exit(app.exec_())
