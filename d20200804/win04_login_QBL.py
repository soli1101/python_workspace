import cx_Oracle
import sys
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# QWidget
# 위젯은 화면에 표시할 수 있는 것을 목적으로 함
# 윈도우나 버튼 모든 위젯 화면에 무언가를 표시하거나 키보드 or 마우스에서
# 사용자의 입력을 받아들이는 것, 버튼, 슬라이드, 뷰, 대화상자 등등
# 사용자와의 상호작용을 나타내는 사각형 영역

# QMainWindow
# 메인 창에서는 최상위 위젯이고 메뉴바, 도구모음, 상태표시줄를 포함하는
# 미리 정의된 레이아웃을 가지고 있다.
# 창의 부모/자식의 상단이며 일반적으로 제목 표시줄과 테두리를 표시

# QDialog
# 특수한 종류의 창으로 보통 일시적
# 알림, 입력, 선택

class MyWidget(QWidget):
        def __init__(self, parent):
            super().__init__()
            self.parent = parent
            print(self.parent)
            self.initUI()

        def initUI(self):
            # QLabel
            self.labelID = QLabel("ID",self)
            self.labelPW = QLabel("PW",self)
            self.labelNM = QLabel("Name",self)
            self.labelGR = QLabel("Grade",self)

            # QLineEdit
            self.leID = QLineEdit("",self)
            self.lePW = QLineEdit("",self)
            self.leNM = QLineEdit("",self)
            self.leGR = QLineEdit("",self)

            # BUTTON
            self.send = QPushButton("send",self)
            self.send.clicked.connect(self.sendDB)

            # Grid Layout
            grid = QGridLayout()
            self.setLayout(grid)

            grid.addWidget(self.labelID,0,0)
            grid.addWidget(self.leID,0,1)

            grid.addWidget(self.labelPW,1,0)
            grid.addWidget(self.lePW,1,1)

            grid.addWidget(self.labelNM,2,0)
            grid.addWidget(self.leNM,2,1)

            grid.addWidget(self.labelGR,3,0)
            grid.addWidget(self.leGR,3,1)

            grid.addWidget(self.send,4,0)
            
        def sendDB(self):
            print("회원가입")
            connection = cx_Oracle.connect("scott","tiger","192.168.0.68:1521/orcl")
            cur = connection.cursor()
            sql = '''
            INSERT into member
            VALUES(:id, :pw, :name, :grade)'''
            cur.execute(sql, id=self.leID.text(), pw=self.lePW.text(), name=self.leNM.text(), grade=self.leGR.text())
            connection.commit() 
            connection.close()
            self.parent.close()

class MyRegisterWindow(QMainWindow):
        def __init__(self, parent):
            super().__init__(parent)
            self.setGeometry(600,500,500,400)
            self.setWindowTitle("회원가입 페이지")
            self.setCentralWidget(MyWidget(self))

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        # Label만들기
        self.labelID = QLabel("ID",self)
        self.labelPW = QLabel("PW",self)

        # QLineEdit
        self.leID = QLineEdit(self)
        self.lePW = QLineEdit(self)

        # 버튼만들기
        self.btnLogin = QPushButton("로그인",self)
        self.btnReg = QPushButton("회원가입",self)
        
        # 창 타이틀 지정
        self.setWindowTitle("찐 로그인 페이지")
        self.resize(300,250)
        
        # Layout : BoxLayout, 수평상자 수직상자(Widget만 적용)
        # 수평상자 레이아웃 객체
        hbox1 = QHBoxLayout() 
        hbox1.addStretch(1)  # 일정정도의 쿠션을 줌(경계랑 얼마나 떨어지는 지)
        hbox1.addWidget(self.labelID) 
        hbox1.addWidget(self.leID)
        hbox1.addStretch(1)  # 오른쪽에 쿠션

        hbox2 = QHBoxLayout() 
        hbox2.addStretch(1)  # 일정정도의 쿠션을 줌(경계랑 얼마나 떨어지는 지)
        hbox2.addWidget(self.labelPW) 
        hbox2.addWidget(self.lePW)
        hbox2.addStretch(1)  # 오른쪽에 쿠션

        hbox3 = QHBoxLayout() 
        hbox3.addStretch(1)  # 일정정도의 쿠션을 줌(경계랑 얼마나 떨어지는 지)
        hbox3.addWidget(self.btnLogin) 
        hbox3.addWidget(self.btnReg)
        hbox3.addStretch(1)  # 오른쪽에 쿠션

        # 수직상자 레이아웃 객체
        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        
        self.setLayout(vbox)

        # PyQt에서 이벤트(Signal) 처리할 때 사용되는 함수를
        # 이벤트 핸들러(Slot)라고 한다.
        # Signal
        self.btnLogin.clicked.connect(self.dbCheck)
        self.btnReg.clicked.connect(self.register)

        # 화면에 보여지게 설정
        self.show()

# Slot
    def dbCheck(self):
        # 1. connection 객체 생성
        connection = cx_Oracle.connect("scott","tiger","192.168.0.68:1521/orcl")
        print(connection)
        
        # 2. cur 객체 생성 
        cur = connection.cursor()
        
        # 3. sql문 객체 생성
        sql = '''
        select id, pw, name, grade
        from member
        where id =:id and pw = :pw ''' # :id : 변수라는 뜻에서 

        # 4. cur 실행문 작성
        cur.execute(sql, id=self.leID.text(), pw=self.lePW.text())
        print(cur)
        # 5. 로직처리 및 출력하기
        for dbid, dbpw, name, grade in cur:
                print(dbid, dbpw)
                if dbid != None:
                        print("Login Suceeded")
                        # 메세지박스
                        rep = QMessageBox.question(self,"Login Suceeded","환영합니다",QMessageBox.Yes)
                else:
                        print("Login Failed")
        # 6. 자원반납하기
        connection.close()

# 회원가입 form 만들기!        
    def register(self):
            self.rg = MyRegisterWindow(self)
            self.rg.move(700,300)
            self.rg.show()

# 현재 파일에서 호출시에만 실행가능하게 설정
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())