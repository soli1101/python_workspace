import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtWidgets, QtWidgets, QtNetwork
from PyQt5 import *
from card import Card

myTurn = False

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Love Letter♡")
        self.resize(1200,700)
        self.move(0,0)
        self.setWindowIcon(QIcon("E:/dev/python_workspace/W7(project)/img/pp2.png"))

# 배경 
        bg_img = QPixmap("E:/dev/python_workspace/W7(project)/img/bgbg.png")
        self.bg = QLabel("bg",self)
        self.bg.resize(1200,700)
        self.bg.setPixmap(bg_img)
        
# player Label 만들기
        self.playerList = [QLabel("player{}".format(i+1),self) for i in range(4)]
        [label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) for label in self.playerList] #Q--> A : List 내포로 선언
        self.playerList[0].setGeometry(286, 582, 80, 25)
        self.playerList[1].setGeometry(677, 453, 80, 25)
        self.playerList[2].setGeometry(568, 170, 80, 25)
        self.playerList[3].setGeometry(184, 205, 80, 25)

# 공격대상 버튼
        self.playerBtnList = [QPushButton("Player{}".format(i+1), self) for i in range(4)]
        self.playerBtnList[0].setGeometry(286, 560, 80, 25)
        self.playerBtnList[1].setGeometry(677, 453, 80, 25)
        self.playerBtnList[2].setGeometry(568, 170, 80, 25)
        self.playerBtnList[3].setGeometry(184, 205, 80, 25)

        for i,btn in enumerate(self.playerBtnList): # 공격대상 선택하면 서버로 보내주기 위한 for문 
            btn.setHidden(True)             # 버튼은 감추고
            self.playerBtnEvent(btn,i)      # 이벤트를 실행한다. btn과 player번호를 인수로 받는다
        
# 1번 카드 선택시 선택할 카드 버튼
        self.selTypeBtnList = [QPushButton("{}번".format(i+2), self) for i in range(7)]
        for i,btn in enumerate(self.selTypeBtnList):
            if i<(len(self.selTypeBtnList)//2)+1: 
                btn.setGeometry(660+i*30,540, 30,40)
            else:
                btn.setGeometry(645+(i-len(self.selTypeBtnList)//2)*30,590, 30,40)
            btn.setHidden(True)
            self.typeBtnEvent(btn,i) # 선택된 카드를 서버로 보내기 위한 함수로 이동시킴

# 초코비 뱃지 
        self.heart_img = QPixmap("E:/dev/python_workspace/W7(project)/img/coin.png").scaled(28,30)
        self.heartBadgeList =[[QLabel(self) for i in range(3)] for j in range(4)]
        for Label in self.heartBadgeList:       # badge리스트에 있는 Label에
            for heart in Label:                 # 각 Label에  
                heart.setPixmap(self.heart_img) # 하트 이미지를 입혀
                heart.setHidden(True)           # 일단 숨겨놔 
        for j in range(3):  
            self.heartBadgeList[0][j].setGeometry(286+j*26,550,28,30) #맨아래 
            self.heartBadgeList[1][j].setGeometry(677+j*26,479,28,30) #오른쪽
            self.heartBadgeList[2][j].setGeometry(184+j*26,173,28,30) #위쪽
            self.heartBadgeList[3][j].setGeometry(568+j*26,138,28,30) #왼쪽

# card List 생성 및 배치 
        self.backImg = QPixmap("E:/dev/python_workspace/W7(project)/img/0.jpg").scaled(78,103,Qt.KeepAspectRatio, Qt.FastTransformation)
        self.playerCardList = [[QLabel(self) for i in range(2)] for j in range(4)]
        for player in self.playerCardList:
            for card in player:
                card.setPixmap(self.backImg)
                card.setHidden(True)
        
        self.playerCardList[0][0].move(378,480) # 자신의 1번카드 맨 아래
        self.playerCardList[0][1].move(488,480) # 자신의 2번카드
        self.playerCardList[1][0].move(678,340) # player3의 1번카드 오른쪽
        self.playerCardList[1][1].move(678,230) # player3의 2번카드
        self.playerCardList[2][0].move(478,90)  # player2의 1번카드 맨 위
        self.playerCardList[2][1].move(388,90)  # player2의 2번카드
        self.playerCardList[3][0].move(185,240)  # player1의 1번카드 왼쪽
        self.playerCardList[3][1].move(185,350)  # player1의 2번카드

        self.playerCardList[0][0].mousePressEvent = self.sendSelected1
        self.playerCardList[0][1].mousePressEvent = self.sendSelected2
        
# center Card
        self.centerCardList = [QLabel(self) for i in range(16)]
        self.grave = [QLabel(self) for i in range(16)]
        for i in range(16):
            self.centerCardList[i].setPixmap(self.backImg)
            self.centerCardList[i].move(478+i*2,270+i*2)
            self.grave[i].move(378+i*2,270+i*2)
            self.grave[i].resize(78,103)

# 네트워크
        # username
        self.userName = QLineEdit(self)
        self.userName.setPlaceholderText("username")
        self.userName.setGeometry(927,350,110,38)

        # 연결버튼
        self.connectButton = QPushButton("연결",self)
        self.connectButton.setGeometry(1052,350,110,38)
        self.connectButton.clicked.connect(self.connection)
        self.connectButton.setDefault(True)

        #start button
        self.startBtn = QPushButton("게임시작",self)
        self.startBtn.setGeometry(800,350,110,38)
        self.startBtn.setHidden(True)
        self.startBtn.clicked.connect(self.startGame)
        
        # 채팅창
        self.main_text = QTextEdit(self) # 메인 텍스트
        self.main_text.setReadOnly(True)
        self.main_text.setGeometry(800,400,361,180)

        self.send_box = QLineEdit(self) # 문자 입력창
        self.send_box.setGeometry(800,590,270,40)

        self.send_button = QPushButton('보내기',self)  # 문자 보내기
        self.send_button.setGeometry(1082,590,80,40)
        self.send_button.clicked.connect(self.sendData)

        dog = QPixmap("E:/dev/python_workspace/W7(project)/img/pp.png").scaled(100,100)
        self.dog = QLabel(self)
        self.dog.setPixmap(dog)
        self.dog.move(1074,498)

        # 네트워크 연결하기 
        self.server_ip = '192.168.0.31'
        self.port_address = 5000

        self.socket = QtNetwork.QTcpSocket(self)
        self.socket.readyRead.connect(self.readData)
        self.socket.error.connect(self.displayError)
        
        # Game Rule
        self.gamerule = QLabel("""
                              ※ 게임 방법 ※\n
 [1] 자신의 턴에 카드 2장이 주어집니다. 
 [2] 카드 한 장을 선택합니다.
 [3] 카드의 기능은 공격가능 대상에게만 사용할 수 있습니다.
 [4] 카드를 사용하면 자동으로 차례가 넘어갑니다.
 [5] 마지막 까지 카드를 들고 있는 사람이 승자가 됩니다.  
    *2인 이상 일 경우: 카드를 비교해서 숫자가 높은사람이 승!\t\n

                              ※ 게임 목표 ※\n
 1게임은 총 3판으로 구성되고,
 1판이 끝날 때 마다 승자는 초코비를 받게 됩니다. 
 먼저 초코비 3개를 모은 사람이 최종 승자가 됩니다.""",self)
        self.gamerule.move(800,100)
        self.gamerule.setStyleSheet("padding: 0px; margin:0px; font-family: 맑은 고딕; border-radius:10;")

        self.show()

#----------함수-----------#

    def startGame(self):                # start 함수
        self.startBtn.setHidden(True)   # 실행되면 보여진다 
        self.send("sys:start")          # 서버에 sys:start라는 메세지 보낸다

    def playerBtnEvent(self, btn, i):   # 공격대상 선택 버튼 이벤트: 클릭 되는 버튼을 걸러주는 체 역할!
        btn.clicked.connect(lambda : self.playerBtnEvent2(btn,i)) # ★클릭★하면 2로 보냄

    def playerBtnEvent2(self, btn, i):  # 공격대상 선택 버튼 이벤트2 
        self.send("sys:selectedPlayer:{}".format(i)) # 서버에 선택대상 보냄, 보내고 나면
        for bt in self.playerBtnList:   # player버튼리스트에서 버튼을 가져와서
            bt.setHidden(True)          # 버튼을 숨긴다

    def typeBtnEvent(self, btn, i):     # 공격대상의 카드 타입 : 역시 클릭 된 카드를 걸러내는 체 역할을 한다
        btn.clicked.connect(lambda: self.typeBtnEvent2(btn,i)) # 클릭하면 2로 보냄

    def typeBtnEvent2(self, btn, i):    # 공격대상의 카드 타입 보내기 이벤트 
        self.send("sys:selectedType:{}".format(i+2)) # 서버에 선택된 카드 보냄 
        for bt in self.selTypeBtnList:  # 보낸뒤에 다시 카드를 
            bt.setHidden(True)          # 숨김

#sysPrint: 서버의 메세지 받아서 카드GUI에 구현하기
    # sys : print : 11(남은카드) : [무덤카드타입] : [1,2](자기카드타입) : 1 : 1 : 1 :
    #  0  :   1   :     2       :       3       :         4          : 5 : 6 : 7 : 8 
    #끊어서가져오면:     0       :       1       :         2          : 3 : 4 : 5  
    def sysPrint(self,list):
        
        # center 카드 
        for i,card in enumerate(self.centerCardList):
            if i < int(list[0]):
                card.setHidden(False)
            else:
                card.setHidden(True)
        
        # grave 카드
        for i,card in enumerate(self.grave):
            if i < len(eval(list[1])):  # 무덤카드리스트에 담긴 카드보다 순번이 작으면 : 결국, 무덤카드에 1개 미만일 때 (처음에만)
                card.setHidden(False)   # 카드를 보여준다
                card.setPixmap(QPixmap("E:/dev/python_workspace/W7(project)/img/{}.jpg".format(eval(list[1])[i])).scaled(78,103,Qt.KeepAspectRatio, Qt.FastTransformation))
            else:
                card.setHidden(True)    # 카드를 제출하기 시작하면 무덤카드를 전부 보여준다.
        
        # player 카드 
        for i,card in enumerate(self.playerCardList[0]):
            if i < len(eval(list[2])):  # len(eval(list[2])) --> 카드의 갯수  // eval(list[2]) --> 카드의 타입
                card.setPixmap(QPixmap("E:/dev/python_workspace/W7(project)/img/{}.jpg".format(eval(list[2])[i])).scaled(100,139,Qt.KeepAspectRatio, Qt.FastTransformation))
                card.setHidden(False)   # 카드를 보여줘
                # 카드마다 보여줄 tooltip리스트 
                toolTipL = ["","상대를 선택하고 카드를 추측하여 맞으면 상대가 탈락한다","상대를 선택하고 가진 카드 확인한다","상대를 선택하고 자신의 카드와 비교하여 낮은 숫자를 가진 사람이 탈락","다음 자신의 턴이 올 때까지 다른 카드의 공격을 받지 않는다","상대를 선택하고 카드를 버리고 다시 뽑는다","상대를 선택하고 카드를 교환한다","5번 또는 6번 카드를 가지고 있으면 반드시 버려진다","버리면 무조건 패배(버릴 수 없음)"]
                card.setToolTip(toolTipL[eval(list[2])[i]]) 
            else :
                card.setHidden(True)    # 이외의 경우에는 카드를 보여줘
        
        # 나머지 player의 카드를 출력하는 코드
        #"sys:print:11:[0,1]:[3,5]:1:1:1:/"   -> split("/") -> split(":")
        #["sys","print","11","[0,1]","[3,5]","1","1","1",""]
        #["11","[0,1]","[3,5]","1","1","1"]
        #["11","[0,1,3]","[5]","1","1","1"]
        #["11","[0,1,3]","[5]","[2]","1","1"]
        #["11","[0,1,3]","[5]","1","1","1"]

        for i in range(len(list)-3):                # player 숫자를 가져와서 그것 만큼 돌리는 것 
            for j,card in enumerate(self.playerCardList[i+1]):   # playerCardList[i+1]된 이유는 자기자신을 제외하고 나머지 플레이어 1~3까지의 카드를 보여주기 위해서 
                if len(list[i+3]) == 1:             # 서버에서 받는 메세지에서 해당 player의 카드가 갯수로 온건지 아니면 타입으로 온 건지 파악하기 위해서 만약 1이면, 갯수로 온것 
                    if j < int(list[i+3]):   # player1,2,3의 index번호가 
                        card.setPixmap(QPixmap("E:/dev/python_workspace/W7(project)/img/0.jpg").scaled(78,103,Qt.KeepAspectRatio, Qt.FastTransformation))
                        card.setHidden(False)       # 카드의 뒷면을 보여줘
                    else:
                        card.setHidden(True)        # 나머지는 숨겨
                else: # 2,3 번 카드 일 때 다른 사람의 카드를 보여주기 위한..
                    self.playerCardList[i+1][0].setPixmap(QPixmap("E:/dev/python_workspace/W7(project)/img/{}.jpg".format(eval(list[i+3])[0])).scaled(78,103,Qt.KeepAspectRatio, Qt.FastTransformation))

#readData: 서버의 메세지 받아서 처리하는 함수
    def readData(self):
        global myTurn
        message = self.socket.readLine().data().decode("utf-8").split("/")
        print(message)

        #sys에서 온 메세지 처리 
        for submessage in message:
            if submessage == "":
                continue
            elif submessage == "NICK":    #sys로 부터 NICK이라는 메세지가 왔다면,
                self.socket.write(self.userName.text().encode("utf-8")) #userName값을 보내
                self.userName.setReadOnly(True)                         #userName은 읽기전용으로 바꿔
        
        # sys : print : 11(남은카드) : [무덤카드타입] : [1,2](자기카드타입) : 1 : 1 : 1 :
        #  0  :   1   :     2       :       3       :         4          : 5 : 6 : 7 : 8     
            elif submessage.split(":")[0] == "sys":    # sys에서 온 메세지이면, :로 잘라와
                msg = submessage.split(":")
                if msg[1] == "print":           # msg 1이 print이면
                    self.sysPrint(msg[2:-1])    # sysprint 함수로 이동해서 처리해 
                elif msg[1] == "turn":          # turn 이면
                    myTurn = True               # myTurn을 활성화시켜
                elif msg[1] == "reSelectCard":  # reSelectedCard이면
                    QMessageBox.information(self, "reselect", "카드를 다시 선택하세요!") 
                    myTurn = True               # myTurn을 활성화시켜
                elif msg[1] == "selectPlayer":  # selectPlayer 이면
                    for idx in eval(msg[2]):    # 남은카드의 숫자만큼을 가져와서 A.-->eval(msg[2]) : 공격이 가능한 player의 인덱스 번호들이 리스트 안에 담겨서 옴   이게 리스트인가?
                        self.playerBtnList[idx].setHidden(False) # player버튼을 보여줘
                elif msg[1] == "selectType":    # selectType 이면
                    for btn in self.selTypeBtnList: # 카드선택리스트를 보여줘
                        btn.setHidden(False)
                elif msg[1] == "nick":          # player라벨의 nick 바꾸기
                    for i in range(len(self.playerList)):   # 플레이어의 인원수 만큼
                        if i < len(eval(msg[2])):           # 남은카드의 수가 순번보다 작으면: 결국, 첫번째 이면:
                            self.playerList[i].setText(eval(msg[2])[i]) # A:setText 서버로부터 전송받은 닉네임 리스트를 받아서 그걸 playlist의 각항목에 입힘
                            self.playerBtnList[i].setText(eval(msg[2])[i])  # 버튼도 같은 식으로 바꿈
                        else:                   # 아니면
                            self.playerList[i].setHidden(True)      # playerList를 숨겨
                            self.playerBtnList[i].setHidden(True)   # playerBtnList를 숨겨
                elif msg[1] == "youAreFirst":   # 첫번째사람에게만 start버튼 보여주기
                    self.startBtn.setHidden(False)  

                elif msg[1] == "favorability":  # 승리자에게 초코비 주기!
                    for idx, cnt in enumerate(eval(msg[2])): # 예) [1,2,3,1] 이런식으로 메세지가 오면 index번호랑 cnt(내용물)를 가져와 
                        for i,badge in enumerate(self.heartBadgeList[idx]): # idx번호에 해당하는 값 리스트의 i와 badge를 가져와
                            if i < cnt :                # 만약 cnt(내용물)이 badge의 idx 번호보다 작다면
                                badge.setHidden(False)  # 뱃지를 보여주고 아니면 숨겨  Q--> 이걸 왜 만들어 놨지? 물어보기
                            else:                       
                                badge.setHidden(True)

                elif msg[1] == "winner":
                    mb = QMessageBox()
                    mb.setText("축하합니다!!!\n{}".format(msg[2]))
                    mb.setWindowTitle("winner message")
                    mb.setIconPixmap(QPixmap("E:/dev/python_workspace/W7(project)/img/jg.jpg"))
                    mb.exec_()
            else:
                self.main_text.append(submessage)       
    
    def sendSelected1(self,e):
        global myTurn
        if myTurn:
            self.send("sys:selectedCard:1")
            myTurn = False

    def sendSelected2(self,e):
        global myTurn
        if myTurn:
            self.send("sys:selectedCard:2")
            myTurn = False

    def send(self, message):
        self.socket.write(message.encode("utf-8"))

    def sendData(self, e):
        message = "{} : {}".format(self.userName.text(),self.send_box.text())
        if message.find("/") != -1:
            QMessageBox.information(self, "fail", "입력 불가능한 단어가 포함되어 있습니다.\n")
        else:
            self.send(message)
            self.send_box.clear()
            self.send_box.setFocus()

    def closeEvent(self, e):
        self.socket.disconnectFromHost()
    
    def connection(self, e):
        if self.userName.text() == "sys":
            QMessageBox.information(self, "fail", "사용 불가능한 닉네임 입니다.\n")
        else:
            self.socket.connectToHost(self.server_ip, self.port_address)
            if self.socket.waitForConnected(1000):
                self.connectButton.setEnabled(False)
                self.send_button.setDefault(True)
                self.send_box.setFocus()
                print("연결성공")
        
# 디스플레이 에러 메세지
    def displayError(self, e):
        QMessageBox.information(self, "Connection", "서버가 연결을 해제했습니다.")

if __name__=="__main__":
    app = QApplication(sys.argv)
    ex=MyApp()
    sys.exit(app.exec_())