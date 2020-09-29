import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()       # initUI라는 함수를 호출해

    def initUI(self):
        btn = QPushButton('나가기',self)
        btn.move(100,100)
        btn.resize(20,30)
        btn.clicked.connect(QCoreApplication.instance().quit)
        
        self.setWindowTitle("내가 만든 윈도우창")
        self.move(10,10)     # 처음 창이 시작되는 위치
        self.setWindowIcon(QIcon("./img/instagram.png"))
        self.resize(800,600) # 창크기 
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
