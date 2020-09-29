print('----중첩함수:nested function----')
def sayHello():
    msg = '니하오'
    def prt():
        print(msg) # 내부 함수는 바깥 함수를 가져다 쓸 수 있다
    prt()
sayHello()
print()

print('----nonlocal중첩함수와 지역변수----')
def f1():
    a=10        # f1의 지역변수: a
    def f2():   # f1 안에 있는 중복함수: f2
        nonlocal a # global로 찾으면 전역변수를 찾기 때문에 
        a=20    # f2의 지역함수: b
    f2()
    print(a)
f1()