import time

class ATM:
    def __init__(self):
        print("초기화 함수 호출")
        self.__balance=0         #_를 주면 외부에서는 접근X 내부O
        self.name="홍길동"
    
    # setter, getter
    def get__balance(self):
        # 감사기록
        print("잔액: ", self.__balance)

    def set__balance(self, balance):
        # 감사기록
        self.__balance = balance
    
    def deposit(self,money):
        self.__balance += money
        print(money, "원 입금합니다.")
        print("현재 잔액 : ",self.__balance)
        
    def withdraw(self,money):      
        if money <= self.__balance:
            self.__balance -= money
            print(money,"원 출금합니다.")
        else:
            print("잔액이 부족합니다>.<")
        print("현재 잔액:",self.__balance)
auto = ATM()
print()
print('----------입금-----------')
auto.deposit(1000)

# __balance라는 새로운! 변수를 만들어서 넣어 준 것임!!
# 내부 balance와 이름이 우연히 같을 뿐
# 실제로 내부변수에 적용 X
auto.__balance = 999999999999  

auto.set__balance(88888888)

print()                        
print('----------출금-----------') 
print(auto.__balance)
auto.withdraw(400)
