#상속

class Person:
    def __init__(self,name,age,job,hobby):
        print("슈퍼맨 초기화")
        self.name=name
        self.age=age
        self.job=job
        self.hobby=hobby
    def fly(self):
        print("비행: 날아보아요~~~")
    def laser(self):
        print("지이이이이이잉~~~~!")
    def sleeping(self):
        print("쿨쿨 자용~~~zzzzzzz")
    def eating(self,what):
        print(self.name,"이",what,"을/를 맛있게 먹어요")


# Person 클래스를 상속받은 Superman 클래스

class superman(Person):     # self가 아닌 Person이 들어간다
    def __init__(self,name,age,job,hobby):
        print("슈퍼맨 초기화")
        self.name=name
        self.age=age
        self.job=job
        self.hobby=hobby
    def fly(self):
        print("비행: 날아보아요~~~")
    def laser(self):
        print("지이이이이이잉~~~~!")

sm=superman("슈퍼맨",20,"신문기자","연애")
sm.fly()
sm.laser()
sm.eating("바나나")     # superman 클래스에 없어도 함수 호출가능
sm.sleeping()          # superman 클래스에 없어도 함수 호출가능
