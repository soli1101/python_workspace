print('----Document주석----')
def add(a,b):
    ''' 두 수의 합을 리턴합니다. '''
    c= a+b
    return c

def minus(e,d):
    ''' 두 수의 차를 리턴합니다. '''
    return e-d

x=add(100,200)
y=minus(200,100)
print(x+y) # 400
help(add) # 두 수의 합을 리턴합니다.
help(minus)# 두 수의 차를 리턴합니다.

print('----두개 이상의 값 리턴----')
def add_minus(a,b):           # 두개 이상의 값을 리턴할 수 있다.
    return (a+b), (a-b)   

x, y=add_minus(300,100)
print('x:',x,"y:",y)

i, j = (1,2)        # 언패킹 unpacking: i, j 변수에 튜플값 하나씩 넣어준다
i, j = 1, 2         # 역시 i, j에 튜플값 넣어준 거
i, j = [1,2]        # i, j에 리스트값 넣어준 거 
print(i)
print(j)

# 함수의 리턴 값: 정수, 문자, 실수, 튜플, 리스트 ···

print('----return 연습----')
def hap(a,b):
    return a+b
sumValue = hap(100,200) # 합계를 리턴합니다...: 300
print(sumValue)

def hap2(a,b,c):        # 마지막 c자리는 어떤 type인지를 지정하는 자리
    return a+b+c
sumValue2 = hap2(100,200,300) # 결과값이 안나온다

def hap3(a,*b):         # *b 부분을 튜플로 인식한다
    print("a:",a,"b:",b)
    print((a+int(b[0])+int(b[1])))
    return (a+int(b[0])+int(b[1]))
hap3(100,200,300)

def hap4(a,*b):         # *b는 가변인수 선생님이랑 같이 한 것
    print("a:",a,"b:",b)
    v = a
    for k in b:
        v+=k
    return v

print('-------------------------')
print(hap4(100,200,300))