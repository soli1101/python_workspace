print('dict : 키 : 값의 쌍으로 이루어짐, 순서 X')
print('-------------------------')
mydic = dict(k1=1,k2='abc',k3=3.4)
print(mydic)
print('-------------------------')
dic = {"파이썬":"뱀","자바":"커피",'오라클':'델파이'}
print(dic, len(dic))
print('-------------------------')
print(dic['자바'])  # dictionary 안에 키 값을 넣으면 value값을 꺼내줌
print('-------------------------')
dic['스미스']="백그라운드프로세스"  # 새로운 키value값 추가
print(dic)
dic['neo']="키아누리브스"
dic['스미스']="bg"              # 있는 값을 할당하면 덮어씀
print('-------덮어쓰기---------')
print(dic)
print('-------------------------')
dic['neo']="잘생김"             # 중복 X 덮어쓴다
print(dic)
print('----------지우기-----------')
dic.clear()
print(dic)
print()
print('-------연습1 -------')
# 1. 1부터 100까지 정수를 랜덤하게 생성
# 2. 사용자로부터 숫자 한개를 입력
# 3. 두 수가 일치하면 일치합니다. 메세지 출력
# 4. 일치하지 않으면 사용자가 입력한 값보다 작은값인지 큰값인지 
#    출력하게 하고 다시 입력 받도록 한다.

import random
num = random.randint(1,100)
print("컴퓨터 랜덤숫자:",num)

while True:
    guess = int(input("숫자 한개를 입력하세요: "))
    print(num, guess)
    if num == guess :
        print("일치합니다.")
        break
    else:
        if num >= guess:
            print("더 큰수를 입력해봐")
        else:
            print("더 작은수를 입력해봐")
print()