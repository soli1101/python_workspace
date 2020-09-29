#client side#
from socket import *
import threading
import time

ip = "192.168.0.68"
port = 5000

clientSocket= socket(AF_INET, SOCK_STREAM)
clientSocket.connect((ip,port))
print("접속완료")

def send(sock):
    sendData = input(">>>보냅니다용!")
    clientSocket.send(sendData.encode("utf-8")) 

def receive(sock):
    recvData = clientSocket.recv(1024)
    print("서버가 보낸 메세지: ", recvData.decode("utf-8"))

# sender = threading.Thread(target=send, args=(clientSocket,))
# receiver = threading.Thread(target=receive, args=(clientSocket,))

# sender.start()
# receiver.start()

# while True:
#     time.sleep(0.1)
#     pass