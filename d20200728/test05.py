print('----#CLASS연습: Car 클래스 만들기 ----')
class Car:
    def __init__(self,ccomp,cname,ccol,cyear):
        print("초기화 함수 호출")
        self.company=ccomp  # 인스턴스 변수
        self.name=cname
        self.color=ccol
        self.year=cyear
        self.wheel=4
        self.handle=1
    def status(self):       # 인스턴스 함수(or method)
        print("회사:",self.company)
        print("차명:",self.name)
        print("색상:",self.color)
        print("연식:",self.year)
        print("바퀴:",self.wheel)
        print("핸들:",self.handle)
    def forward(self):
        print("전진합니다~빵빵")
    def back(self):
        print("후진합니다!삐삐!")
    def blinking(self):
        print("깜빡이 켭니다~")
    def accel(self):
        print("가속합니다! 조심하세요")
    def decel(self):
        print("감속합니다.")
    def stop(self):
        print("☞ 정지☜")

A = Car('jaguar','jaguarXF','red',2019)
A.status()
A.forward()

print()
print('-------------------------')
ns = Car("닛산","맥시마","silver",2018)
ns.status()

# 파이썬의 method의 parameter명은 관례적으로 self 이름 사용
# 호출 시 호출한 객체 자신이 전달되기 때문에 self 이름 사용

A.forward()     # A.forward() = Car.forward(A)
Car.forward(A)
''' 
    OOP : Object Oriented Programming
    객체 중심 프로그래밍 : 객체를 중심으로 프로그램을 짜면
                         유지보수가 쉽다. 
    목적: 자원의 재활용
    Class를 사용해 객체(Instance) 생성
    Class는 새로운 이름공간을 지원하는 단위

    Instance가 맞는지 확인하는 법: isinstance(변수, 클래스명)

'''
print(isinstance(A,Car)) # A 가 Car 클래스의 instance야? 
                         # 맞으면 True, 아니면 False

