print('***********CLASS연습3***********')
## 이름, 나이, 직업에 매게변수 주기
class Human:
    def __init__(self, a,b,c):  # 매게변수
        print("초기화 함수 호출")
        self.name= a            # 매게변수를 줬다!!!
        self.age= b             # 처음부터 변할 값들은
        self.job= c             # 매게변수로 지정하면 된다
        self.eye = 2
        self.mouth = 1
        self.ears  = 2
    def eating(self):
        print("냠냠 맛있다")
    def walking(self):
        print("두발로 걸어요 아장아장")
    def sleeping(self):
        print("zzz")
    def thinking(self):
        print("생각한다 고로 존재한다...")
    def status(self):
        print("이름:",self.name)
        print("나이:",self.age)
        print("직업:",self.job)
        print("눈:",self.eye)
        print("입:",self.mouth)
        print("귀:",self.ears)

p=Human("펭수",20,"직장인")
p.status()

print()
print('-------------------------')
d=Human("둘리",100000000,"백수")
d.status()