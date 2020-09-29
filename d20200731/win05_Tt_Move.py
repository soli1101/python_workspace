import threading
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QListView
from PyQt5.QtCore import QCoreApplication,Qt
from PyQt5.QtGui import QIcon,QPixmap
import time

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    # 방향키를 누르면 lb1이 움직이도록 설정하기
    def goLeft(self):
        print(self.lb1.x(),self.lb1.y())
        self.lb1.move(self.lb1.x()-2, self.lb1.y())
    
    def keyPressEvent(self,e):
        print(e.key())
        if e.key() == Qt.Key_Left:
            print("왼쪽으로~")
            self.goLeft()       #함수사용
        elif e.key() == Qt.Key_Right:
            print("오른쪽으로~") #함수X 직접입력
            self.lb1.move(self.lb1.x()+2, self.lb1.y())
        elif e.key() == Qt.Key_Up:
            print("위로!")
            self.lb1.move(self.lb1.x(), self.lb1.y()-2)
        elif e.key() == Qt.Key_Down:
            print("아래로!")
            self.lb1.move(self.lb1.x(), self.lb1.y()+2)
        elif e.key() == Qt.Key_Space:
            t = threading.Thread(target=self.moveTurtle)
            t.start() 
            # 화면을 움직이는 애랑 moveTurtle이랑 별도로 실행
        
    def moveTurtle(self):
        print("스페이스가 눌렸음")
        for i in range(10):
            time.sleep(0.01)
            x= self.lb1.x()
            y= self.lb1.y()
            self.lb1.move(x, y+1)
        
        for i in range(10):
            time.sleep(0.01)
            x= self.lb1.x()
            y= self.lb1.y()
            self.lb1.move(x+8,y-1)
            
    def initUI(self):
        self.setWindowTitle("방향키를 만들어요")
        self.resize(800,600)

        # QPixmap 객체
        p_img = QPixmap("./img/turtle.gif") # 객체 생성

        # label 생성
        self.lb1 = QLabel('나',self)
        self.lb1.setPixmap(p_img)   # pixmap으로 가져온 이미지 
                                    # 입혀주기
        self.lb1.move(50,400)

        self.show()

if __name__=="__main__":
    app=QApplication(sys.argv)
    ex=MyApp()
    sys.exit(app.exec_())
