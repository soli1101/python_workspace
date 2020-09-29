print('----#hw1: 세계최초의 암호화 ----')
# setEncryption(문자열) 함수 생성
# 1. 사용자로부터 단어를 입력받는다
# 2. 글자를 불러와서 아스키코드 값으로 바꾸고 
# 3. 그것에 3을 더해서 출력한다.
# 4. 끝에 3자는 다시 a,b,c가 될 수 있도록
# 5. 3번째 뒤에 글자를 출력한다.
# 6. getDecode(~~~암호값) 함수 생성

data = input("암호화 할 메세지를 입력하세요!: ")
def setEncryption(msg):
    w=[]
    for i in range(len(msg)):
        b = ord(msg[i])+3
        if b == 123:    # x->a y->b z->c
            b = 97
        elif b == 124:
            b = 98
        elif b == 125:
            b = 99
        elif b == 91:   # X->A Y->B Z->C
            b = 65
        elif b == 92:
            b = 66
        elif b == 93:
            b = 67
        v = chr(b)
        print(v,end="")
        w.append(v)
    return w
m=setEncryption(data)
print()
print(m)
print('-------------------------')
def getDecode(code):
    a = []
    for j in range(len(code)):
        c = ord(code[j])-3
        if c == 94:     # a->x  b->y  c->z
            c = 120
        elif c == 95:
            c = 121
        elif c == 96:
            c = 122
        elif c == 62:   # A->X  B->Y  C->Z
            c = 88
        elif c == 63:
            c = 89
        elif c == 64:
            c = 90
        y = chr(c)
        print(y,end="")
        a.append(y)
    return a
p=getDecode(m)
print()
print(p)

print()
print('----#hw2: 6행 5열 행열 만들고 총점 및 평균 구하기 ----')
score = []      # score라는 빈 리스트 만들어 준다
score.append([80,80,80,0,0])    # 리스트에 행열 값 입력한다
score.append([60,50,80,0,0])
score.append([50,90,90,0,0])
score.append([40,50,60,0,0])
score.append([90,90,95,0,0])
score.append([85,95,100,0,0])

for j in range(6):
    for i in range(1):
        sum=score[j][0]+score[j][1]+score[j][2]
        print(j,"번 학생의 총점:",sum, '평균:',sum//3)

print()
print('----#hw3: 야구 게임 만들기----')
import random

n=random.randrange(100,1000)    # 컴퓨터가 3자리 랜덤 숫자 생성
print('컴퓨터 랜덤숫자: ',n)

ni=int(input("3자리 숫자를 입력하세요~!")) # 사용자로부터 3자리 숫자 입력받기
print("입력:", ni)
print(n[0])
 


    


