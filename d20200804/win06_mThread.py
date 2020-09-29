#CPU Central Process Unit 중앙처리장치
'''
ㅇ x86 => intel => amd
       8068
       80268
       80368
       80468
       pentium

ㅇ multi Task => 작업을 동시에 처리할 수 있다
             1초씩 분산해서 메모리를 할당한다 
    게임 X
    서비스 응대

ㅇ 프로세서 : 메모장, 워드, 카톡 
ㅇ Thread => 하나의 프로세스 내에서 진행되는 하나의 실행 단위를 의미
   multi Thread => 카톡: 채팅, 파일전송 
             하나의 프로세스 내에서 동시에 여러개의 동작을 실행

ㅇ 파이썬에서 multi Thread 구현 방법
    1. thread가 실행할 함수 혹은 method를 작성하는 방식
    2. threading.Thread로 부터 파생된 파생클래스를 작성하여 사용하는 방식
'''
import threading

def run(who):
    for i in range(1, 101):
        print(str(i)+"미터 달리는중",who)

# run("번개")
# run("천둥")

'''
이것을 multi Thread로 처리하려면...
'''

t1 = threading.Thread(target=run,args=("번개",))
t2 = threading.Thread(target=run,args=("천둥",))

'''
start() : Thread를 동작시킨다.
'''
t1.start()
t2.start()

print("---main Thread end---")