print('***********CLASS연습2***********')

class Human:
    def __init__(self):
        print("초기화 함수 호출")
        self.name="고길동"
        self.age=30
        self.job="고위공직자"
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

print(Human, id(Human), type(Human))

ko = Human() # 인스턴스변수=클래스명() # 클래스의 초기화 함수 호출됨
print(ko.name) # . 연산자 의미 : 주소를 찾아가~~
print(ko.eye)
print(ko.mouth)
print(ko.ears)
print('---함수호출---')
ko.thinking()   # 인스턴스변수.method명 : method 호출하는 법
ko.eating()
ko.walking()
ko.sleeping()
ko.status()

print()
print('---펭수만들기---')
p = Human()
p.name = "펭수"
p.age = 10
p.job = "EBS 직장인"
p.status()