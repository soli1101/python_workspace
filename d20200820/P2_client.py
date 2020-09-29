#Client Side
import threading
from socket import *

ip = "192.168.0.31"
port = 5000

clientSock = socket(AF_INET,SOCK_STREAM)
clientSock.connect((ip, port))
print("연결성공")

def send(sock):
    sendData = input("client:")
    sock.send(sendData.encode("utf-8"))

def receive(sock):
    recvData = sock.recv(1024)
    print("server:",recvData.decode("utf-8"))

while True:
    receive(clientSock)
    send(clientSock)

send_thread = threading.Thread(target=send,args="clientSock")
send_thread.start()
receive_thread = threading.Thread(target=receive,args="clientSock")
receive_thread.start()
