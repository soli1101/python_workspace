#client side
from socket import *

ip = "192.168.0.32"
port = 5000

clientSocket= socket(AF_INET, SOCK_STREAM)
clientSocket.connect((ip,port))
print("접속완료")

def send(sock):
    sendData = input(">>>보냅니다용!")
    clientSocket.send(sendData.encode("utf-8")) 

def recive(sock):
    recvData = clientSocket.recv(1024)
    print("서버가 보낸 메세지: ", recvData.decode("utf-8"))

while True:
    send(clientSocket)
    recive(clientSocket)