#함수연습1
def do_test(*k):
    cum = 0
    for i in k:
        cum+=i
    print("cum:",cum)
    return cum
# 리턴값이 있는 함수는
# 리턴값을들 어떤 변수에 담아서 써야함
x=do_test(100,200,300)   
print(x)

def do_test1(**kwargs):
    for key, value in kwargs.items():
        print('key:',key,"value:",value)
do_test1(name="홍길동",age=20)