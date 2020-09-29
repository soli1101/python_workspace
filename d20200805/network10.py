 # 여러 클라이언트 받기
# 클라이언트 사이드

#기능 불러오기
import socket
import threading

ip = "192.168.0.37"                                             # ip변수 생성
port = 5000                                                     # port변수 생성


# 닉네임 결정
nickname = input("당신의 닉네임을 입력하세영: ")                 # input()를 통해 nickname변수에 대입

# 서버에 연결
clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # socket()를 통해 clientSock변수선언 
clientSock.connect((ip,port))                                    # clientSock변수는 ip와 port(5000번 포트)를 통해 서버와 연결

# 서버에 닉네임 보내기
def receive():                                                   # receive() 지정
    while True:                                                  # 참이라면 반복실행,
        try:                                                     # 기본적인 실행
            msg = clientSock.recv(1024).decode("utf-8")          # msg변수에 bufsize를 설정하여 주고받을 용량을 결정하여 저장 (받을 때 decode)
            if msg =="NICK":                                     # 만약 msg가 NICK이라면,
                clientSock.send(nickname.encode("utf-8"))        #  서버와 연결이 되자마자 "utf-8"형식으로 encode하여 nickname 전송 (보낼때 encode)
            else:                                                # 아니라면,
                print(msg)                                       #  출력
        except:                                                  # 예외발생할 경우
            # 에러 발생시에 연결끊기
            print("에러 발생")                                   # 출력
            clientSock.close()                                   # 예외가 발생한 클라이언트 연결 종료
            break                                                # 반복문 종료

# 서버에 메세지 보내기
def send():                                                      # send() 지정
    while True:                                                  # 참이라면 반복실행,
        msg ="{}: {}".format(nickname, input())                  # input()를 통해 보낼 메세지 입력하여 msg변수에 대입 
        clientSock.send(msg.encode('utf-8'))                     # 서버와 연결이 되자마자 "utf-8"형식으로 encode하여 msg전송 (보낼때 encode)

# 수신과 발신을 동시에 처리하는 쓰레드
receive_thread = threading.Thread(target=receive)                # 계속(지속적으로) 연결하여 메세지를 받을 수 있는 receive_thread변수 생성
receive_thread.start()                                           # receive_thread변수의 쓰레드 시작

send_thread = threading.Thread(target=send)                      # 계속(지속적으로) 연결하여 메세지를 보낼 수 있는 send_thread변수 생성
send_thread.start()                                              # send_thread변수의 쓰레드 시작




