print('----1.변수명 규칙?----')
'''
변수명은 a~z, A~Z, 숫자, _ 가 첫글자로 올 수 있다.
대소문자를 구분한다. 특수문자는 사용할 수 없다.
'''
print()

print('----2. 제곱값을 리턴하는 함수 작성----')
def square(x):
    return x*x
print(square(5))
print()

print('----3. 2를 람다함수로 작성----')
m=[5]
print(list(map(lambda x:x*x,m)))
print()

print('----4. 각 리스트의 값을 3배로 만드는 함수 작성----')
'''
1부터 100까지 값을 가지고 있는 리스트가 있다. 
m = [1,2, ... 100]
각 리스트의 값을 3배로 만드는 함수 triple을 작성하시오 
'''
m = list(range(1,101))
def triple(list):
    for i in range(len(m)):
        m[i]=m[i]*3
    return m
print(triple(m))
print()

print('----5. 람다식으로 4번 작성----')
print(list(map((lambda x:x*3),m)))
print()

print('----6. 다음을 작성----')
'''
10칸 짜리 정수형 리스트 rnd 에 랜덤(100이하)하게 값을 할당하고
최대값 , 최소값을 출력해보자. (내장함수 사용) 
'''
import random
rnd= []
for i in range(10):
    rnd.append([random.randint(1,101)])
    
print(min(rnd),max(rnd))