import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

class MyApp (QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("e:/login.ui",self) #해당 UI 파일을 읽어와서 적용해줘!
        self.show()

if __name__=="__main__":
    app = QApplication(sys.argv)
    m = MyApp()
    sys.exit(app.exec_())