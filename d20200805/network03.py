# Server side #
from socket import *

port = 5000

serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",port))
serverSocket.listen(1)

print("%d번 포트로 접속 대기중"%port)

connectionSock, addr = serverSocket.accept()

print(str(addr),"에서 접속되었습니다.")

while True: # 한 번 듣고 한 번 보내고 할 수 있다
    # 계속 수신한다
    recvData = connectionSock.recv(1024)
    print("클라이언트가 보낸 메세지: ", recvData.decode("utf-8"))
    # 메세지를 보낸다
    sendData = input(">>>")
    connectionSock.send(sendData.encode("utf-8"))
