from socket import *

ip = "192.168.0.32"
port = 5000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((ip, port)) # 튜플로 입력해 줘야 한다.
print("접속 완료")
while True:
    sendData = input(">>>보냅니다용!")
    clientSocket.send(sendData.encode("utf-8")) 

    recvData = clientSocket.recv(1024)
    print("서버가 보낸 메세지: ", recvData.decode("utf-8"))