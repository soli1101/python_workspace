print('----변수의 범위----')
print('----└전역변수----')
print('----└지역변수----')

a = 10              # 전역 변수 global 변수
def prt():
    global a        # 전역변수 a 쓸거임
    a=20            # 전역변수 a에 20을 담아
    b=100     
    print(a)        # 흔히는 지역변수를 먼저 사용
    print(locals()) # 함수내 지역변수가 뭐가 잇는지 목록으로 확인가능
    # print(b)
prt()
print()
print('----전역변수 영역----')
print(locals)
print(a)