class test:
    def __init__(self, balance):
        print("초기화 함수")
        self.balance = balance # instance 변수라고 부른다
    def print(self):
        print("잔액: ", self.balance)

t = test(500)
t.aaa=200   # Class에 aaa 변수가 없어도 그냥 변수를 만들어 준다!!
t.print()
print(t.aaa)