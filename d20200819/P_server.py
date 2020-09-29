# server side
import threading
from socket import *

#connection
serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('',5000))
serverSock.listen()
print("연결 대기")

#여러 사용자 접속 허용
clients = []
nicknames = []

def broadcast(msg):
    for client in clients:
        client.send(msg)

def handler(client):
    while True:
        try:
            msg = client.recv(1024)
            broadcast(msg)
            print(msg.decode("utf-8"))
        except:
            i=clients.index(client)  #index: list에서 몇번째 인지 가져와
            clients.remove(client)
            client.close()
            nickname=nicknames[i]   #[]이게 왜 쓰인거지?
            broadcast("{}님 떠남".format(nickname).encode("utf-8"))
            nicknames.remove(nickname)
            break


#클라이언트들의 nickname 받아서 저장하기
def receive():
    while True:
        #연결대기
        connectionSock, addr = serverSock.accept()
        print(str(addr) + "연결 성공")

        #nick요청하고 받아서 nicknames에 append 시키기
        connectionSock.send("nick".encode("utf-8"))
        nickname = connectionSock.recv(1024).decode("utf-8")
        print(nickname)
        nicknames.append(nickname)
        clients.append(connectionSock)
        print(clients)

        #접속자소개하기
        broadcast("{}님이 접속하셨습니다.".format(nickname).encode("utf-8"))
        connectionSock.send("서버에 접속되었습니다. 환영합니다".encode("utf-8"))

        #동시에 채팅가능하게 하기
        handler_thread = threading.Thread(target=handler,args=(connectionSock,))
        handler_thread.start()

receive()
