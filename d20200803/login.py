import cx_Oracle
import sys
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyWidget(QWidget):
        def __init__(self):
                super().__init__()

class MyRegisterWindow(QMainWindow):
        def__init__(self,parent):
        super().__init__(parent)
        self.setCentralWidget(MyWidget())
        # self.unitUI


class Register(QMainWindow):
        def __init__(self, parent):
                super().__init__(parent)
                self.setGeometry(600,500,500,400)
                self.setWindowTitle("회원가입 페이지")
                self.Register_UI()
                self.show()

        def Register_UI(self):
                # QLabel
                self.labelID = QLabel("ID",self)
                self.labelID.move(100,100)

                self.labelPW = QLabel("PW",self)
                self.labelPW.move(100,140)
                
                self.labelNM = QLabel("Name",self)
                self.labelNM.move(100,180)

                self.labelGR = QLabel("Grade",self)
                self.labelGR.move(100,220)

                # QLineEdit
                self.leID = QLineEdit("",self)
                self.leID.move(150,100)
                
                self.lePW = QLineEdit("",self)
                self.lePW.move(150,140)

                self.leNM = QLineEdit("",self)
                self.leNM.move(150,180)
                
                self.leGR = QLineEdit("",self)
                self.leGR.move(150,220)

                # BUTTON
                self.send = QPushButton("send",self)
                self.send.move(200,290)
                self.send.clicked.connect(self.sendDB)

        def sendDB(self):
                print("회원가입")
                 # 1. connection 객체 생성
                connection = cx_Oracle.connect("scott","tiger","192.168.0.68:1521/orcl")
      
                # 2. cur 객체 생성 
                cur = connection.cursor()
        
                # 3. sql문 객체 생성
                sql = '''
                INSERT into member
                VALUES(:id, :pw, :name, :grade)'''

                # 4. cur 실행문 작성    
                cur.execute(sql, id=self.leID.text(), pw=self.lePW.text(), name=self.leNM.text(), grade=self.leGR.text())
                connection.commit() 
                
                # 5. 로직처리 및 출력하기
                # 6. 자원반납하기
                connection.close()
                # 입력이 다 끝나고 send 누르면 창 닫기
                self.hide()

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
            self.rg = Register(self)
            self.rg.move(700,300)
            self.rg.show()

# 현재 파일에서 호출시에만 실행가능하게 설정
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())