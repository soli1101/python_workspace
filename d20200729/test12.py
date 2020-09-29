import random
import math

class Agar:
    def __init__(self,color,nickname):
        self.radius = 5
        self.color = color
        self.nickname= nickname
        self.x=random.randint(1,100)
        self.y=random.randint(1,100)
        self.weight = 10

    def feeding(self,other):
        if other.weight < self.weight:
            self.weight += other.weight
        else:
            self.weight += 17
            print("먹이주기")
    def split(self):
        self.weight=self.weight//2
        print("반토막나기...^^")
    
    def move(self):
        print("이동하기")
    
    def merge(self):
        self.weight += 1
        self.radius += 0.2
        print("셀 먹기 ^^")
    
    @staticmethod # 정적인 메소드: 클래스의 영향 받지 X
    def getArea(radius):
        return radius*radius*math.pi

print(Agar.getArea(50))
print('----실행하기----')
a1=Agar("green","망국이다")

a1.move()
a1.merge()
a1.merge()
a1.merge()
a1.merge()
a1.merge()
a1.merge()
a1.merge()
a1.merge()
a1.split()
a1.getArea(50)
print(a1.getArea(a1.radius))