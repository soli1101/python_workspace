import cx_Oracle
import sys
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

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

            # ID 입력란의 Layout
            hbox1 = QHBoxLayout()
            hbox1.addStretch(1)
            hbox1.addWidget(self.labelID)
            hbox1.addStretch(1)
            hbox1.addWidget(self.leID)
            hbox1.addStretch(1)

            # PW 입력란의 Layout
            hbox2 = QHBoxLayout()
            hbox2.addStretch(1)
            hbox2.addWidget(self.labelPW)
            hbox2.addStretch(1)
            hbox2.addWidget(self.lePW)
            hbox2.addStretch(1)
            
            # Name 입력란의 Layout
            hbox3 = QHBoxLayout()
            hbox3.addStretch(1)
            hbox3.addWidget(self.labelNM)
            hbox3.addStretch(1)
            hbox3.addWidget(self.leNM)
            hbox3.addStretch(1)
            
            # Grade 입력란의 Layout
            hbox4 = QHBoxLayout()
            hbox4.addStretch(1)
            hbox4.addWidget(self.labelGR)
            hbox4.addStretch(1)
            hbox4.addWidget(self.leGR)
            hbox4.addStretch(1)
            
            # Send 버튼의 Layout
            hbox5 = QHBoxLayout()
            hbox5.addStretch(1)
            hbox5.addWidget(self.send)
            hbox5.addStretch(1)

            # 모든 행의 Vertical Layout
            vbox = QVBoxLayout()
            vbox.addStretch(1)
            vbox.addLayout(hbox1)
            vbox.addStretch(1)
            vbox.addLayout(hbox2)
            vbox.addStretch(1)
            vbox.addLayout(hbox3)
            vbox.addStretch(1)
            vbox.addLayout(hbox4)
            vbox.addStretch(1)
            vbox.addLayout(hbox5)
            vbox.addStretch(1)

            # Layout 설정하기
            self.setLayout(vbox)

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