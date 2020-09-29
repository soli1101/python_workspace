import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel("집에 가~~~",self)
        
        font1 = label1.font()
        font1.setPointSize(30)
        label1.setFont(font1)
        label1.move(400,200)

        btn = QPushButton("go",self)
        btn.move(210,400)
        btn.resize(600,30)
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.setWindowTitle("안녕하세요 방가방가 >,< 귀욤뽀짝")
        self.setWindowIcon(QIcon("./img/windowicon.png"))
        self.resize(1000,600)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = window()
    sys.exit(app.exec_())