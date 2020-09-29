import sys
from PyQt5.QtWidgets import *

#  윈도우를 생성하는 클래스 : QMainWindow, QWidget, QDialog
#  메인윈도우를 생성하기 위한 클래스 : QMainWindow, QDialog
#  QMainWindow : QHBoxLayout, QVBoxLayout 같은 layout 사용 X


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.show

if __name__ == "__main__":
    # QApplication 클래스의 인스턴스를 생성
    app = QApplication(sys.argv)    # app을 생성한 뒤
    print(app,sys.argv)             # app을 출력함 # sys.argv는 파일이 있는 경로 

    btn=QPushButton("Quit")
    btn.show()
    btn.clicked.connect(quit())
                                    
    app.exec_()           # 이벤트 루프 : 무한 루프돌리기
