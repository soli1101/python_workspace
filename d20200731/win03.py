import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class MyApp(QWidget):
    def __init__(self):
        super().__init__() 
        self.initUI()       
    
    def gugudan(self):
        dan = int(self.danInput.text())
        for i in range(1,10):
            print(dan,"x",i,"=",dan*i)
        self.danInput.setText("")

    def initUI(self):
        self.setWindowTitle("win03.py")
        self.resize(800,600)

        # QLineEdit : 구구단 입력받을 입력창 생성
        self.danInput = QLineEdit(self)
        self.danInput.move(295,180)
        self.danInput.resize(120,50)
              
        # 구구단 실행할 버튼 생성
        btn=QPushButton("gugudan",self)
        btn.resize(100,100)
        btn.move(210,400)
        btn.clicked.connect(self.gugudan)

        self.show()

# 실제 실행하기
if __name__=="__main__":   
    app=QApplication(sys.argv)
    ex=MyApp()
    sys.exit(app.exec_())
