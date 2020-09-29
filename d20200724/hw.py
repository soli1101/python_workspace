print('----hw1: 다음을 람다식으로 수정하시오 ----')
#def test(x):
#       return x+10
print((lambda x: x+10)(10))
print()

print('----hw2: 다음을 공백기준으로 몇글자씩인지 알아내는 코드 ----')
msg0= "Yeah 다시 돌아왔지 내 이름 레인(RAIN) 스웩을 뽐내 WHOO! They call it! 왕의 귀환 후배들 바빠지는 중! 신발끈 꽉 매고 스케줄 All Day 내 매니저 전화기는 조용할 일이 없네 WHOO! "
msg= "Yeah 다시 돌아왔지 내 이름 레인(RAIN) 스웩을 뽐내 WHOO! They call it! 왕의 귀환 후배들 바빠지는 중! 신발끈 꽉 매고 스케줄 All Day 내 매니저 전화기는 조용할 일이 없네 WHOO! ".split()
# 1. for문으로 표현하기
for i in range(len(msg)):
    print("[",i,"]",len(msg[i]),end="")
print()

# 2. set comprehension으로 표현하기
print([len(word) for word in msg])

print('----hw3: 2번 문자열 중 글자가 4자 이상인 단어만 출력----')
# 1. for문으로 표현하기
for i in range(len(msg)):
    if len(msg[i]) >= 4:
        print (msg[i])
print()

# 2. set comprehension으로 표현하기
print([word for word in msg if len(word)>=4])
print()

print('----hw4: 다음을 dictionary comprehension으로 출력----')
do_city = { "경기도":"수원", "강원도":"춘천"}
print({do:city for do,city in do_city.items()})
print()

print('----hw5: 지역변수와 전역변수의 차이점----')
'''지역변수는 정의된 함수 안에서만 사용가능하다.
전역변수는 외부 및 정의된 함수 안 둘 다 사용가능하다.'''
print()

print('----hw6: 다음 코드를 실행한후에 화면에 출력 되는 a의 값은 얼마인가?') 
a  = 100 
def show():
    a = 200
    b = 100
    print(a)  
show()
print(a)  

print('----왜 차이가 날까요?----')
''' 함수안에 있는 print(a)는 지역변수를 먼저 가지고 오고 
함수 밖에 print(a)는 전역변수 a 값을 가져오기 때문이다.'''
print()

print('----hw7:____들어갈 코드는? global a') 
a  = 100 
def show():
    global a
    a = 200
    b = 100

show()
print(a) 
# 200 으로 출력되게 해주려고한다. __________ 들어갈 코드는 ? 
print()

print('----hw8:지역변수의 목록을 확인하려면 어떤 명령을 사용할까?----') 
print('print(locals())')
print()

print('----hw9:다음 코드를 실행했을 때 화면에 출력값? ----')
''' 500 '''
def fx():
    data1  = 500    
    def fx2():
        data1 =  300 
    fx2()
    print(data1)
fx()
print()

print('----hw10:출력 결과를 300 이 나오게 하려면 __________ 에 알맞은 코드는? ----')
print('nonlocal data1')
print()

print('----hw11:일급함수의 특징 3가지 ----')
print('----1.함수를 다른 함수의 인수로 전달할 수 있다 ----')
print('----2.함수의 반환값으로 함수 사용할 수 있다 ----')
print('----3.변수에 저장할 수 있다 ----')
print()

print('----hw12:다음의 출력결과는?----')
def  tax():
    a = 1.1
    def cal(b):
        return a*b
    return cal

getTax = tax()
print(getTax(1000))   # 출력결과는 ?  1100.0

print('----hw13: 클로져 closure ----')
'''
12번에서 cal 함수는 getTax 함수 호출할때 다시 꺼내서 사용되어지는데 
	이런 함수를 _________ 라고 한다. 
'''
print()

print('----hw14: Regular Expression정규 표현식----')
'''
일정한 규칙(패턴)을 가진 문자열을 표현하는 방법  ______________ 이라 한다.
'''
print()

print('----hw15: 사용순서----')
'''
15. 
	사용순서 
		1. re 모듈을 불러온다
		2. compile을 통해 찾을 문자열의 패턴을 입력한다
		3. match, search, findall, finditer을 사용해 문자열 검색
'''
print()

print('----hw16: 전화번호만 출력----')		
'''
16.	# 문자열중 전화번호만 찾아서 출력하고자한다. 
	# 파이썬 코드로 작성하시오.
'''
msg="Hello Python  Oracle  Friday 010-1234-5678  2020년 7월 24일".split()
print(msg)
print([word for word in msg if word.find('010')>=0])

'''
17.
	16번 문제를 정규표현식으로 작성하시오 
'''
import re
p = re.compile('[0-9]+-[0-9]+-[0-9]+')
print(p,type(p))
m = p.findall("Hello Python  Oracle  Friday 010-1234-5678  2020년 7월 24일")
print(m)

