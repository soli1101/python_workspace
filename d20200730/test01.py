class Car:
    def __init__(self,handle=1,wheel=4,eye=2,nose=1,mouth=1):
        self.handle=handle
        self.wheel=wheel
        self.eye=eye
        self.nose=nose
        self.mouth=mouth
        print("초기화 함수 호출..")
    def run(self):
        print("붕붕카 달리는 중♪")
    def stop(self):
        print("sTOP!!")
    def smell(self,what):
        print(what,"냄새 맡는 중~♣")
    def talk(self):
        print("Miao! 혼자 중얼 중얼중 얼중 얼중 ~~")
    def __add__(self,otherCar):
        print("☞  ☜ 충돌났네요ㅠ.,ㅠ 힝구")
    def __sub__(self,otherCar):
        print("???")
c1=Car()
c1.talk()
c1.run()
print(c1.handle)

print()
print('----Car를 상속받는 오픈카 만들기----')
class inheritedCar(Car):
    def lightOn(self):
        print("라이트를 켜요!ㅇ..ㅇ")
    def run(self):
        print("☜ 오픈카로 달려요!☞")
ic1=inheritedCar()
c1.smell('꽃')
c1.run()
ic1.smell("장미")
ic1.lightOn()
ic1.run()

print()
print('----Overloading 파이썬의 특징----')
c1+ic1
c1-ic1