import os
import time
import log

class ATM:
    def __init__(self):
        print("초기화 함수 호출")
        self.balance=0
        self.name="홍길동"
    
    def deposit(self,money):
        self.balance += money
        print(money, "원 입금합니다.")
        print("현재 잔액 : ",self.balance)
        # log 함수 불러와서 저장하는 기능!!
        log.savelog("./bank.log",money,self.balance,False)
        
    def withdraw(self,money):      
        # db에 연결해서 현재 진짜 잔액이 존재하는지
        # 권한은 있는지 감사기록을 남긴다.
        if money <= self.balance:
            self.balance -= money
            print(money,"원 출금합니다.")
        # 현재 작업디렉토리에 bank.log라는 파일을 생성해서
        # 지금시간, 출금액, 현재잔액을 저장하는 파일을 만들자
            log.savelog("./bank.log",money,self.balance,True)
        else:
            print("잔액이 부족합니다>.<")
        print("현재 잔액:",self.balance)
auto = ATM()
print()
print('----------입금-----------')
auto.deposit(1000)
print()
print('----------출금-----------')
auto.withdraw(400)
