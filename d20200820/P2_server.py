#Server Side
import threading
from socket import *

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(("",5000))
serverSock.listen()
print("연결대기")

connectionSock, addr = serverSock.accept()
print(str(addr)+"과 연결 성공")

def send(sock):
    sendData = input("Server:")
    sock.send(sendData.encode("utf-8"))

def receive(sock):
    recvData = sock.recv(1024)
    print("Client:",recvData.decode("utf-8"))

while True:
    send(connectionSock)
    receive(connectionSock)

send_thread = threading.Thread(target=send,args="connectionSock")
send_thread.start()
receive_thread = threading.Thread(target=receive,args="connectionSock")
receive_thread.start()
