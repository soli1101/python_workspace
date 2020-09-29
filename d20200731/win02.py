import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QLineEdit,QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class MyApp(QWidget):
    def __init__(self):
        super().__init__()  # 부모클래스의 __init__ 상속받기
        self.initUI()       # initUI 함수를 생성해

    # print를 누르면 
    def print(self):          # setText() - text()로 사용됨
        id = self.leID.text() # labelEdit에 입력된 text를 가져와
        pw = self.lePW.text()
        print(id, type(id)) 
        print(pw, type(pw))
        if id == 'aaa' and pw == 'bbb':
            print("입성 성공")
        else:
            print("입성 실패...ㅠ.ㅠ 울디마, 다시해")
        self.leID.setText("")
        self.lePW.setText("")

    def close(self):
        # QMessegeBox 클래스
        # 사용자에게 정보를 제공: 질문과 응답을 할 수 있는 대화창
        response = QMessageBox.question(self, "메세지", "정말 나갈라구?",QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        # print('close 실행됨')
        # print(response)
        if response == QMessageBox.Yes: # QMB의 Yes에 고유값이 있으므로 비교연산 가능
            print("나가지마~~~")
            QCoreApplication.instance().quit()


    # UI 담당 함수 : User Interface
    def initUI(self):
        self.setWindowTitle("와...금요일이다...불금불금") 
        self.resize(800,600)
        self.move(300,400)      

        # Label 2개 만들기
        labelID=QLabel("ID",self)
        labelPW=QLabel("PW",self)
        labelID.move(300,180)
        labelPW.move(300,250)
        labelID.resize(120,50)
        labelPW.resize(120,50)
        
        # font 크기 크게
            #└font값을 설정할 변수 생성
        fontID = labelID.font() 
        fontPW = labelPW.font()
        
            #└font 설정 값 주기
        fontID.setPointSize(20)
        fontPW.setPointSize(20) 
        fontID.setBold(True)
        fontPW.setBold(True)   
        
            #└font 설정값을 label과 연동하기
        labelID.setFont(fontID) 
        labelPW.setFont(fontPW) 
        
        # QLineEdit
        self.leID = QLineEdit(self)
        self.lePW = QLineEdit(self)

        self.leID.move(395,180)
        self.lePW.move(395,250)
        self.leID.resize(120,50)
        self.lePW.resize(120,50)

        # 푸쉬버튼 인스턴스를 추가
        btn1=QPushButton("출력",self)
        btn1.setText("Print")
        btn1.resize(100,50)
        btn1.move(260,360)
        # Event Handler 특정 이벤트를 처리해 주는 기능
        btn1.clicked.connect(self.print) # self.print라는 함수랑 연결해 줘 라는 뜻

        # 푸쉬버튼 인스턴스를 추가
        btn2=QPushButton("exit",self)
        btn2.setText("Close")
        btn2.resize(100,50)
        btn2.move(460,360)
        # btn2.clicked.connect(QCoreApplication.instance().quit)
        btn2.clicked.connect(self.close) # close 함수에 연결

        # 화면에 창을 보여지게 설정
        self.show()  

# 실제 실행하기
if __name__=="__main__":   
    app=QApplication(sys.argv)
    ex=MyApp()
    sys.exit(app.exec_())