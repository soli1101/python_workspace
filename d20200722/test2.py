print('----함수 연습: factorial 계산 함수----')
def factorial(n):               
    value = 1
    for i in range(n,1,-1):
        value=value*i
    print(str(n)+"!=",value)
    return value
x = factorial(3)
y = factorial(5)
print("x:",x,"y:",y,"x+y:",x+y)
print()

print('----연습2: factorial 형식을 보여주는 함수----')

def factorial2(n):  
    ''' 다큐먼트 팩토리얼
    이 함수는 내가 심심해서 만든거야~
    쓸려면 쓰고 말려면 말어~
    '''     
print(factorial2.__doc__)
help(factorial2)

    value = 1           # value 변수에 1을 미리 넣어 놓는다.
    for j in range(n,0,-1): # j는 0~n까지 역순으로 대입한다.
        value=value*j           # value변수에 j번째를 누적 곱
        if j > 1:               # 만약 j가 1보다 크면
            print(j," * ",end="")   # 다음 값을 출력하고
        else:
            print(j," = ",value,end="") #나머지는 이렇게 출력
    return value                # 이 값을 나를 부른애 한테 보내
    
c = factorial2(5)       # 부른애 요있네~! 인수 5 넣어서 변수 c에 담아
print()                 # c를 출력해 보자
