import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtWidgets, QtNetwork
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

#배경
        bg_img = QPixmap(r"E:/dev/python_workspace/W7(project)/img/bgbg.png")
        self.bg = QLabel("bg",self)
        self.bg.resize(1200,700)
        self.bg.setPixmap(bg_img)

# Player Label
        self.playerList = [QLabel("player{}".format(i)) for i in range(1,5)]
        self.playerList[0].setGeometry(286,560, 80,25)
        self.playerList[1].setGeometry(677,453, 80,25)
        self.playerList[2].setGeometry(568,170, 80,25)
        self.playerList[3].setGeometry(184,205, 80,25)

# 카드이미지
        backImg = QPixmap(r"E:/dev/python_workspace/W7(project)/img/0.png")
        self.backImg_78 = backImg.scaled(78,103)

# Player 4명에게 카드 2장씩 배분하기 
        self.playerCardList = [[QLabel(self) for i in range(2)] for j in range(4)]
        for player in self.playerCardList:      # 카드리스트에서 1개씩 가져와서 
            for card in player:                 # 각 플레이어의 카드에 이미지를 입혀 
                card.setPixmap(self.backImg_78) # 전부다 backImg_78을 입혀
                card.setHidden(False)            # 숨겨놔 
  
# 초코비 뱃지 
        self.heart_img = QPixmap(r"E:/dev/python_workspace/W7(project)/img/coin.png").scaled(28,30)
        self.heartBadgeList =[[QLabel(self) for i in range(3)] for j in range(4)]
        for Label in self.heartBadgeList:       # badge리스트에 있는 Label에
            for heart in Label:                 # 각 Label에  
                heart.setPixmap(self.heart_img) # 하트 이미지를 입혀
                heart.setHidden(False)           # 일단 숨겨놔 
        for j in range(3):  
            self.heartBadgeList[0][j].setGeometry(286+j*26,550,28,30) #맨아래 
            self.heartBadgeList[1][j].setGeometry(677+j*26,479,28,30) #오른쪽
            self.heartBadgeList[2][j].setGeometry(568+j*26,138,28,30) #왼쪽
            self.heartBadgeList[3][j].setGeometry(184+j*26,173,28,30) #위쪽

# 카드이미지 화면에 배치 
        self.playerCardList[0][0].move(378,480) # 자신의 1번카드 맨 아래
        self.playerCardList[0][1].move(488,480) # 자신의 2번카드

        self.playerCardList[3][0].move(185,240)  # player1의 1번카드 왼쪽
        self.playerCardList[3][1].move(185,350)  # player1의 2번카드

        self.playerCardList[2][0].move(478,90)  # player2의 1번카드 맨 위
        self.playerCardList[2][1].move(388,90)  # player2의 2번카드

        self.playerCardList[1][0].move(678,340) # player3의 1번카드 오른쪽
        self.playerCardList[1][1].move(678,230) # player3의 2번카드

# 카드 Deck, 카드 grave
        self.centerCardList = [QLabel(self) for i in range(16)]
        self.grave = [QLabel(self) for i in range(16)]
        for i in range(16):
            self.centerCardList[i].setPixmap(self.backImg_78)   # Deck의 카드를 back 이미지 입힘
            self.centerCardList[i].move(478+i*2,270+i*2)        # Deck의 카드를 조금씩 비껴서 배치
            self.grave[i].move(378+i*2,260+i*2)
            self.grave[i].resize(78,103)

# 공격대상 버튼
        self.selUserBtnList = [QPushButton("{}번".format(i+1), self) for i in range(4)]
        self.selUserBtnList[0].setGeometry(286,560, 80,25)
        self.selUserBtnList[1].setGeometry(677,453, 80,25)
        self.selUserBtnList[2].setGeometry(568,170, 80,25)
        self.selUserBtnList[3].setGeometry(184,205, 80,25)
        for i in range(4):
            self.selUserBtnList[i].setHidden(False)
        
        self.selUserBtnList[0].clicked.connect(lambda: self.send("sys:selectedUser:0"))
        self.selUserBtnList[1].clicked.connect(lambda: self.send("sys:selectedUser:1"))
        self.selUserBtnList[2].clicked.connect(lambda: self.send("sys:selectedUser:2"))

# 1번 카드 선택시 선택할 카드 버튼
        self.selCardList = [QPushButton("{}번".format(i+2), self) for i in range(8)]
        for i in range(7):
            if i < 3: 
                self.selCardList[i].setGeometry(640+i*30,470, 30,40)
            else:
                self.selCardList[i].setGeometry(537+i*30,540, 30,40)
            self.selCardList[i].setHidden(True)

        for j in range(7):
            self.SelectedType(self.selCardList[j], j)

# 카드 클릭시 서버에 명령문 전달
        self.playerCardList[0][0].mousePressEvent = self.sendSelected1
        self.playerCardList[0][1].mousePressEvent = self.sendSelected2

# 네트워크 
        self.userName = QLineEdit(self) # 사용자 이름받기
        self.userName.setPlaceholderText("username")
        self.userName.setGeometry(800,350,110,35)

        self.connectButton = QPushButton("Connect",self) # Connect 버튼
        self.connectButton.setGeometry(927,350,110,38)
        self.connectButton.clicked.connect(self.connection)
        self.connectButton.setDefault(True)

        self.startBtn = QPushButton("Start",self)
        self.startBtn.setGeometry(1052,350,110,38)

        self.main_text = QTextEdit(self) # 메인 채팅창
        self.main_text.setReadOnly(True)
        self.main_text.setGeometry(800,400,361,180)
        self.main_text.setTextBackgroundColor= 'blue'

        self.send_box = QLineEdit(self) # 문자 입력창
        self.send_box.setGeometry(800,590,270,40)

        self.send_button = QPushButton('send',self) # 문자 보내기
        self.send_button.setGeometry(1082,590,80,40)
        self.send_button.clicked.connect(self.sendData)

        self.server_ip = "192.168.0.31" # ip, port
        self.port_address = 5000

        self.socket=QtNetwork.QTcpSocket(self)    # socket 생성
        self.socket.readyRead.connect(self.readData)
        self.socket.error.connect(self.displayError)

        dog = QPixmap("E:/dev/python_workspace/W7(project)/img/pp.png").scaled(100,100)
        self.dog = QLabel(self)
        self.dog.setPixmap(dog)
        self.dog.move(1074,498)

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
 먼저 초코비 3개를 모은 사람이 최종 승자가 됩니다.
\n""",self)
        self.gamerule.move(800,100)
        self.gamerule.setStyleSheet("padding: 0px; margin:0px; font-family: 맑은 고딕; border-radius:10;")
        self.show()

#------- 함수 정의 --------#
    
#readData: sys의 메세지 받아서 처리하는 함수
    def readData(self):
        global myTurn
        message = self.socket.readLine().data().decode("utf-8")
        print(message)
        #sys에서 온 메세지 처리 
        if message == "NICK":   #sys로 부터 NICK이라는 메세지가 왔다면,
            self.socket.write(self.userName.text().encode("utf-8"))#userName값을 보내
            self.userName.setReadOnly(True)                        #userName은 읽기전용으로 바꿔
        
        # sys : print : 11(남은카드) : [무덤카드타입] : [1,2](자기카드타입) : 1 : 1 : 1 :
        #  0  :   1   :     2       :       3       :         4          : 5 : 6 : 7 : 8 
        elif message.split(":")[0] == "sys": #sys에서 온 메세지이면, :로 잘라와
            msg = message.split(":")         
            if msg[1] == "print":            #print이면 
                self.sysPrint(msg[2:-1])     #sysPrint에 있는 명령들을 실행해 

            elif msg[1] == "turn":           #자기 턴이면 카드 1,2번 다 보여줘
                # self.playerCardList[0][0].setPixmap(QPixmap(r"E:\dev\python_workspace\W7(project)\img\{}.jpg".format(msg[2])).scaled(100,139,Qt.KeepAspectRatio, Qt.FastTransformation))
                # self.playerCardList[0][1].setHidden(False) 
                # self.playerCardList[0][1].setPixmap(QPixmap(r"E:\dev\python_workspace\W7(project)\img\{}.jpg".format(msg[3])).scaled(100,139,Qt.KeepAspectRatio, Qt.FastTransformation))
                myTurn = True

            elif msg[1] == "reSelectCard":
                myTurn = True
            
            elif msg[1] == "selectUser":
                selectedUser = self.selectUserOpponent(msg[2])
                print(selectedUser)
                self.send("sys:selectedUser:{}".format(selectedUser))
            
            elif msg[1] == "selectType":
                pass


            elif msg[1] == "notice":
                pass
            elif msg[1] == "D_notice":
                pass

            print("시스템 메세지 입니다")

        else:
            self.main_text.append(message)  # 그냥 메세지 이면 그냥 채팅창에 출력해 

#sysPrint: sys의 메세지 받아서 카드GUI에 구현하기
    # sys : print : 11(남은카드) : [무덤카드타입] : [1,2](자기카드타입) : 1 : 1 : 1 :
    #  0  :   1   :     2       :       3       :         4          : 5 : 6 : 7 : 8 
    #끊어서가져오면:     0       :       1       :         2          : 3 : 4 : 5  
    def sysPrint(self,list):

        # Deck에 있는 카드 모두 보여주기
        for i in range(int(list[0])):
            self.centerCardList[i].setHidden(False) 
        
        # Deck에 있는 카드 숨기기
        for i in range(int(list[0]),len(self.centerCardList)):
            self.centerCardList[i].setHidden(True)
        
        # 무덤 카드 보여주기  
        for i in range(len(eval(list[1]))):
            if i == 0 :                                  # 처음에는
                self.grave[i].setPixmap(self.backImg_78) # 뒷면 이미지를 보여줘
            else:
                self.grave[i].setHidden(False)           # 그 밖에는 앞면을 보여줘
                self.grave[i].setPixmap(QPixmap(r"E:/dev/python_workspace/W7(project)/img/"+str(eval(list[1])[i])+".png").scaled(78,103))
                
            
        # 무덤 카드 숨기기  --> 무덤에 쌓인애들 말고 나머지 애들은 안보이게 숨겨놓기
        for i in range(len(eval(list[1])), len(self.grave)):
            self.grave[i].setHidden(True)

        # player 카드 숨기기
        for i in range(len(eval(list[2])), 2):
            self.playerCardList[0][i].setHidden(True)     # player1의 카드를 숨겨줘

        # player의 카드 보여주기
        for i, cardtype in enumerate(eval(list[2])):
            self.playerCardList[0][i].setPixmap(QPixmap(r"E:\dev\python_workspace\W7(project)\img\{}.png".format(cardtype)))
            self.playerCardList[0][i].setHidden(False)    # 보여줘
            if cardtype == 1:
                self.playerCardList[0][i].setToolTip("상대를 선택하고 카드를 추측하여 맞으면 상대가 탈락한다")
            elif cardtype == 2:
                self.playerCardList[0][i].setToolTip("상대를 선택하고 가진 카드 확인한다")
            elif cardtype == 3:
                self.playerCardList[0][i].setToolTip("상대를 선택하고 자신의 카드와 비교하여 낮은 숫자를 가진 사람이 탈락")
            elif cardtype == 4:
                self.playerCardList[0][i].setToolTip("다음 자신의 턴이 올 때까지 다른 카드의 공격을 받지 않는다")
            elif cardtype == 5:
                self.playerCardList[0][i].setToolTip("상대를 선택하고 카드를 버리고 다시 뽑는다")
            elif cardtype == 6:
                self.playerCardList[0][i].setToolTip("상대를 선택하고 카드를 교환한다")
            elif cardtype == 7:
                self.playerCardList[0][i].setToolTip("5번 또는 6번 카드를 가지고 있으면 반드시 버려진다")
            elif cardtype == 8:
                self.playerCardList[0][i].setToolTip("버리면 무조건 패배(버릴 수 없음)")
    
        # 
        for i in range(len(list)-3):
            for card in self.playerCardList[i+1]:
                if self.playerCardList[i+1].index(card) < int(list[i+3]):
                    card.setHidden(False)
                else:
                    card.setHidden(True)

#sendSelected : 선택된 카드 보내기
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

#sendData : 명령문 보내기
    def sendData(self,e):
        message = "{} : {}".format(self.userName.text(), self.send_box.text())
        self.send(message)
        self.send_box.clear()
        self.send_box.setFocus()

#send : 일반 메세지 보내기
    def send(self, message):
        self.socket.write(message.encode("utf-8"))

#SelectedType : 1번 카드제출했을 때 player가 선택한 카드 
    def SelectedType(self, btn, j):
        btn.clicked.connect(lambda: self.send("sys:selectedType:{}".format(j)))

#displayError 
    def displayError(self,e):
        QMessageBox.information(self, "Connection", "서버가 연결을 해제했습니다.")

#closeEvent : 연결종료하기 
    def closeEvent(self,e):
        self.socket.disconnectFromHost()

#connection : 네트워크연결
    def connection(self,e):
        self.socket.connectToHost(self.server_ip, self.port_address)
        if self.socket.waitForConnected(1000):
            self.send("login %s" % self.userName.text())
            self.connectButton.setEnabled(True)
            self.send_button.setDefault(True)
            self.send_box.setFocus()
            print("연결성공")

# #카드 모서리 함수
    # def Round(self,e):
        
        


        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())