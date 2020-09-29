print('----Closer 클로져----')
# 함수를 호출할 때 다시 꺼내서 사용하는 함수 

def plus_ten():
    a = 10            # a 변수는 원래 한번 호출되면 사라져야 하는데 
    def add(b):       # 사라지지 않고 메모리로 남는다
        return a+b    # 안쪽에 있는 함수는 바깥의 변수에 접근 가능
    return add

cal = plus_ten()      # cal변수에 plus_ten 함수 담아줌 
print(cal(1)) 
print()

print('----return에 람다식 쓰기----')
def plus_ten2():
    a=2
    return lambda b : a+b # 익명함수 매게변수는 b 이고 결과값으로
                          # a+b를 리턴해
cal2 = plus_ten2()        # plus_ten2함수를 cal2에 담어
print(cal2(100),cal2(200))