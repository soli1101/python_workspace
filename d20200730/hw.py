print()
print('----hw1. 클래스, 객체, 인스턴스?----')
print('1.클래스: 객체를 생성하기 위한 청사진이다')
print('2.객체: 객체란 사물이고 클래스를 통해 생성된다')
print('3.인스턴스: 클래스를 통해서 메모리에 할당 된 실체이다.')

print()
print('----hw2. 아무것도 없는 Cat 클래스를 정의하세요 ')
'''
3.  다음 코드로 야옹야옹 이라는 메세지를 출력하도록 Cat 클래스를 수정하세요 
     nabi = Cat()
     야옹야옹  
4.  nabi.play("공")
     공을 가지고 놀고 있다냐옹 
5.   생성자 추가 
     nabi2 = Cat("나비", 2)
6.  print(nabi2)
    이름 : 나비 , 나이 : 2 
7.  nabi2.info()
    이름 : 나비 , 나이 : 2 
8.  nabi2.eat("생선")
     나비가 생선을 먹고 있어요 
9.  del  nabi2 
     고양이 죽는다 야옹 
'''
class Cat:
    def __init__(self,name,age):
        print("야옹야옹")
        self.name=name
        self.age=age
    def __str__(self):
        return '이름:'+self.name+' 나이:'+str(self.age)
    def info(self):
        print('이름:'+self.name+' 나이:'+str(self.age))
    def play(self,what):
        print(what,"을 가지고 놀고 있다냐옹")
    def eat(self,what):
        print("나비가 "+what+"을 먹고있어요")
    def __del__(self):
        print("고양이 죽는다 야옹")
nabi2=Cat("나비",2)
print(nabi2)
nabi2.info()
nabi2.eat("생선")
del nabi2

print()
print('----hw10. Customer 인스턴스를 생성할수 있도록 클래스를 정의하세요')
'''
11. c.show()
     # 홍길동님 현재 잔액은 0원입니다. 
12. c.deposit(5000)
     # 홍길동님 계좌에 5000원 입금합니다.
     # 홍길동님 현재 잔액은 5000원입니다. 
13. c.withDraw(9000)
     # 잔액이 부족합니다. 
     # 홍길동님 현재 잔액은 5000원입니다. 
14. c.withDraw(2000)
     # 홍길동님 계좌에 2000원 출금합니다.
     # 홍길동님 현재 잔액은 3000원입니다. 
15. Customer 클래스에 인스턴스 속성의 값을 을 수정할수 있는 setter, getter 
	클 추가합니다. 
      print(c.get_balance()) # 잔액값 가져오기 : 3000
      c.set_balance(30000) # 잔액을 30000으로 변경 
16. 5회 입금할때마다 
	잔액의 5%씩 이자 발생 
	c.deposit(1000)  #   31000
	c.deposit(3000)  #   34000
	c.deposit(2000)  #   36000
	c.deposit(2000)  #   38000
	c.deposit(3000)  #   41000
	# 이자발생   # 43050
17.	del c 
	# 그 동안 이용해주셔서 감사합니다 
	# 계좌 잔액 : 43050 
'''
class Customer:
    def __init__(self,name,age,pin):
        self.name=name
        self.age=age
        self.pin=pin
        self.balance=0
        self.counter=0
    
    def show(self):
        print(self.name+"님 현재 잔액은 "+str(self.balance)+"원입니다.")
    
    def deposit(self,money):
        self.counter += 1
        if self.counter%5 == 0 :
            self.balance += money
            self.balance = self.balance*1.05
        else:
            self.balance += money
            print(self.name+"님 계좌에 "+str(money)+"원 입금합니다.")
        print(self.name+"님 현재 잔액은 "+str(self.balance)+"원입니다.")
    
    def withDraw(self,money):
        if self.balance >= money:
            self.balance -= money
            print(self.name+"님 계좌에 "+str(money)+"원 출금합니다.")
        else:
            print("잔액이 부족합니다.")
        print(self.name+"님 현재 잔액은 "+str(self.balance)+"원입니다.")
    
    def get_balance(self):
        return '잔액값 가져오기 : '+str(self.balance)
    
    def set_balance(self,balance):
        self.balance = balance
        print(self.name+"님 현재 잔액은 "+str(self.balance)+"원입니다.")

    def __del__(self):
        print('그 동안 이용해주셔서 감사합니다')
        print(self.name+"님 현재 잔액은 "+str(self.balance)+"원입니다.")

c = Customer ("홍길동", 20, "990101-1234567")
c.show()
print('-------------------------')
c.deposit(5000)
print('-------------------------')
c.withDraw(9000)
print('-------------------------')
c.withDraw(2000)
print('-------------------------')
print(c.get_balance()) # 잔액값 가져오기 : 3000
print('-------------------------')
c.set_balance(30000)   # 잔액을 30000으로 변경 
print('-------------------------')
c.deposit(1000)  #   31000
print('-------------------------')
c.deposit(3000)  #   34000
print('-------------------------')
c.deposit(2000)  #   36000
print('-------------------------')
c.deposit(2000)  #   38000
print('-------------------------')
c.deposit(3000)  #   41000
print(c.counter)
# 이자발생        #   43050
print('-------------------------')
del c