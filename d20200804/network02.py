#client side
import random
from socket import *

word = ["안녕","곱하기","왜그래","만나요","즐겁니","사랑해","이쁘다","좋아해","행복해","즐거워"]
random.choice(word)

# 1. Socket 생성
clientSock = socket(AF_INET, SOCK_STREAM) 

# 2. 서버랑 연결해줘..
  ## 서버에 연결
clientSock.connect(('192.168.0.32',5000)) 
  ## 서버에게 메세지 전송
clientSock.send(random.choice(word).encode("utf-8")) 

# 3. data라는 메모리를 할당해서 clientSock의 
#    recv(전송받을 packet최대량) 받은 값을 넣어 
data = clientSock.recv(1024)   
#    data에 들어 있는 값을 utf-8형식으로 decoding 해서 출력해    
print("서버가 보낸 데이터: "+data.decode("utf-8"))

print("연결 성공!!!")