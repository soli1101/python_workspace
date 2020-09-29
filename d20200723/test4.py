# 내장함수
print('★ 내장함수★')
print('----sum----')
print(sum([10,20,30]), sum((10,20)),sum({2,3,}))
print('-------bin------------------')
print(bin(8))       # binary 2진수
print('-------int,float,str--------')
print(int(2.7), float(3), str(5)+'5')
print('-------eval:식으로 바꿔주는 함수')
a = 10
b = eval('a+5')
print(b)
print('-------round------------------')
print(round(5.5))
print()
print('★ module : 함수들의 모음★')
print('-------math module------------')
import math
print(math.ceil(1.2),math.ceil(1.6)) # ()값과 가장 가까운 큰정수
print(math.floor(1.2),math.floor(1.6)) # ()값과 가장 가까운 작은정수
print('-------all, any---------------')
bList = [True,1,False]
print(all(bList)) # True and 1 and False 
print(any(bList)) # True or 1 or False
print()

print('★ 함수안에 함수 사용가능★')
# factorial
# print(factorial)
def do1():
    print("첫번째 함수 실행중")
def do2():
    print("두번째 함수 실행중")
def do3():
    print("세번째 함수 실행중")
    do1()
    do2()
    print("세번째 함수 끝")
do3()
print('----재귀적호출----')

def sayHello(cnt):
    cnt-=1
    print("Hello~~~")
    if cnt > 0:
        sayHello(cnt)
sayHello(5)

print('----factorial----')
# def factorial(n):
#     v = 1
#     for i in range(x,1,-1):
#         v*=i
#     return v

# print(factorial(5)) 
print('----재귀적호출 factorial----')
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)

print(factorial(5)) 

print('----연습5: 피보나치 수열----')
# 1 1 2 3 5 8 13 21 ...
print('----# 1. 내가한 것 ----')
c = [1, 1]
def fibo(x):
    for i in range(x+1):
        v= c[i]+c[i+1] 
        c.append(v)
    return c

print(fibo(4))

print('----# 2. 선생님과 ----')
def fibonacchi(n):
    if n <= 1:
        return n
    return fibonacchi(n-1)+fibonacchi(n-2)

print(10,'번째 피보나치값',fibonacchi(10))