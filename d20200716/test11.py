print(1+1)                  #1+1의 연산값 출력
a = 10                      #a에 정수 10을 대입해
print(a)                    #a를 출력해
a = float(a)                #a를 실수형으로 변환후 a에 대입해
print(a)                    #a를 출력해
print(complex(1.3, 1.4j))   #괄호안의 복소수를 출력해

print('-------------------------') #---를 출력해

# x = input("아무거나 입력")   #입력값을 받아서 변수 x에 대입해
# print("aaa","bbb","ccc")    #동시에 여러개를 입력하려면 ,를 구분자로 사용
# print("x의 값은 :", x)       #x의 값은 x변수값 임을 출력해             

# "", '', ''', """ """ 다 문자열을 지정해줌

print(3>5)      #3>5를 논리연산해서 출력해

a = 100         #a에 100 값을 대입해
b = 200         #b에 200 값을 대입해
print(a<b)      #변수 a<b의 논리연산값을 출력해

c=None          #변수 c 값에 None을 대입해
print(c)        #변수 c 값을 출력해

print(100>2 and 300>100) #논리연산자 를 사용해서 둘 다 맞으면 True값을 출력한다
print(100>2 and 300>100 or 100>200) #True를 출력한다

x=True          #x에 True를 대입해
y=False         #y에 False를 대입해

print(x and y)  #x 변수와 y 변수의 값을 and로 논리연산해서 출력해

print('-------------------------')
print(True and True) #괄호안에 논리연산값을 출력해
print(False and True)#괄호안에 논리연산값을 출력해

print(not True)      #괄호안에 논리연산값을 출력해

a = 300              #a에 300을 대입해  
b = 200              #b에 200을 대입해
print(a == b) # a와 b가 '같다'로 비교할 때 ==로 사용한다 = 한개는 대입해
print(a != b) # a와 b가 '같지 않다'

#문제1 국어 영어 수학 점수를 입력받기
#60점 이하가 있다면 False(실패), True(합격)

kor, eng, mat = input("국어 영어 수학 점수를 띄어서 입력하시오 :").split()
kor = int(kor)
eng = int(eng)
mat = int(mat)
print("국어:",kor,"영어:",eng,"수학:",mat)
print("Total:", kor>60 and eng>60 and mat>60)
print("평균:", (kor+eng+mat)/3 >60)