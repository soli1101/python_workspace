from socket import *

# 1. socket 생성
serverSock = socket(AF_INET, SOCK_STREAM)

# 2. bind : 접속하기! 5000번 포트의 모든 것에 연결해
serverSock.bind(('',5000)) # 5000번 포트를 사용할거야
print("사용자의 접속을 대기합니다.")

# 3. 연결을 기다림 (수신중 ...)(1)은 1개 받는다는 표시
serverSock.listen(1)     
#    사용자의 연결이 올 때 까지 대기한다.
connectionSock, addr = serverSock.accept() 
#    성공됐다는 메세지와 함께 addr를 문자열로 바꿔서 출력한다
print(str(addr)+"연결 성공!!")

# 4. data라는 방을열고 recv로 client에서 받은 내용을 담는다.
data = connectionSock.recv(1024)
#    msg에 client에게 받은 메세지를 decoding해서 넣는다
msg = data.decode("utf-8")
print(msg)

# 5. client로 부터 받은 메세지를 그대로 전송한다.
connectionSock.send(msg.encode("utf-8"))
print("서버 메세지 전송 완료")