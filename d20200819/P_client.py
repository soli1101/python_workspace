# client side
import random
from socket import *
import threading

ip = '192.168.0.31'
port = 5000

#닉네임 결정
nickname = input("what's your nickname?")

#연결
clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect((ip,port))

#닉네임 보내기
def receive():
    while True:
        #서버에서 nick을 요청하면, #nickname을 보내
        try:
            msg=clientSock.recv(1024).decode("utf-8")
            if msg == "nick": 
                clientSock.send(nickname.encode("utf-8")) 
            else:
                #그 밖의 메세지는 그냥 출력해
                print(msg)
        except:
            print("에러발생")
            clientSock.close()
            break

#보내기 함수
def send():
    while True:
        msg = "{}: {}".format(nickname,input(""))
        clientSock.send(msg.encode("utf-8"))

#threading
receive_thread = threading.Thread(target=receive)
receive_thread.start()

send_thread = threading.Thread(target=send)
send_thread.start()



inputmsg = input()
clientSock.send(str(inputmsg).encode("utf-8"))

data = clientSock.recv(1024)
print("서버가 보낸 데이터:"+data.decode("utf-8"))

print("연결 성공")


