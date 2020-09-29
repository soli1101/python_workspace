print('----파이썬의 함수는 모두 일급 함수----')
# 함수를 다른 함수의 인수(argument)로 전달할 수 있다.
# 함수의 반환(return)값으로 함수를 사용할 수 있다.
# 변수에 저장할 수 있다.
# 자바스크립트도 일급함수고 대체적으로 많은 언어가 이런 특징이있다

def add(a,b):
    return a+b
print(add(100,200))         # add 함수 출력해보기
print()

print('----변수에 함수 담기----')
plus = add                  # plus 변수에 add 함수를 담았다
print(plus(500,300))
print()

print('----함수안의 매게변수에 함수 담기 ----')
def appendFunction(f1,c,d): # 매게변수로 함수를 넣을 수 있다
    return f1(c,d)          # 이 함수를 실행하면 f1함수에 c,d 값을 넣은 것을 리턴해
print(appendFunction(add,1000,2000))
print()