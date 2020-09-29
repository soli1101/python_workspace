#함수연습2

mlist=[1000,2000,3000,4000,5000] #만원
for i in range(5):
    mlist[i]=int(mlist[i]*1.1)
print(mlist)
print('----리스트내포----')
# 리스트 내포 표현식 : List comprehension
print([i*1.1 for i in mlist])
# 리스트 내부에 반복문/조건문의 축약 형태 전달 가능
# "사용법:"
# [리턴값 for i in 대상]
# [리턴값 for i in 대상 if 조건]

print('----리스트내포 연습----')
list2=[-5,-2,-1,0,2,-3,-2,10,3]
# 1월 어느날 최고온도
# 영상인 날짜의 온도인 리스트로 작성하려고 한다.
re = []                     
for i in range(len(list2)):
    if list2[i] >= 0:
        re.append(list2[i])
print(re)
print('----LC----')
print([ i for i in list2 if i>=0 ])

print('----#lambda----')
'''
람다함수 (익명함수)
이름이 없는 함수
장점: 코드가 간결하다 
      메모리가 절약된다
'''
def test(x):
    return x+1
print(test(100))
print((lambda x : x+1)(100))

print('----#람다연습----')
def sumdata(a,b):
    return a+b
c=100
d=200
k = sumdata(c,d)
print(k)
print(type(sumdata),id(sumdata))
print('----람다표현----')
pd = sumdata
print(type(sumdata),id(pd))
print('pd:',pd(500,200))
print((lambda a,b : a+b)(100,200))

print('-------------------------')
lmadd = lambda a,b : a+b
print(lmadd(1000,2000))

print('----조건식을 사용한 람다----')

print((lambda a,b : a if a%2==0 else b)(10,20))

