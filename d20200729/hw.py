print('----hw1:1.   object , class , instance 란? ----')
'''
★ object: 객체, 틀에 의해 만들어진 피조물
★ class: 설계도, 피조물을 찍어낼 수 있는 틀
★ instance: 실체, 틀에 의해 만들어진 피조물인 객체와 같은 것인데, 
인스턴스란 용어는 어떤 클래스의 객체인지를 관계 위주로 설명할 때 
사용된다.
'''
print()
print('----hw2: Man class를 생성하시오----')
class Man:
    def __init__(self):
        print("초기화 함수")
        self.name="홍길동"
        self.age=20
        self.eye=2
        self.gender="남"
        self.arm=2
        self.job="도적"
        self.character="스틸"
    def steal(self):
        print("# 내꼬내꼬 다 내꼬얌!!! ")
    def run(self):
        print("헛둘 헛둘")
    def runrun(self):
        print("땀나게 달려요")
    def magic_move(self):
        print("동해 번쩍 서해 번쩍")
m=Man()
print(m.name,m.age,m.eye,m.gender,m.arm,m.job,m.character)
print()
print('----hw3:변수명명법?----')
'''
1. a-z, A-Z, 0-9, _ 올 수 있다. 
2. 특수문자는 사용할 수 없다.
3. 의미가 있는 단어를 사용한다.
4. 영어 사용이 권장된다.
5. 여러 단어를 이어서 써줄 경우 대문자로 써서(카멜법) 명명한다.
'''
print()
print('----hw4: 다음 file 만들고 삼각형의 너비 구하기----')
'''
	ex4.py 
----------------------------------------
	class Triangle 
	width , height
	getArea()
----------------------------------------	
	triangle =	Triangle (100,200) # 너비 100, 높이 200 
	print(triangle.getArea())  # 삼각형의 너비 구하기 
'''
print()
print('----hw5: 다음 file 만들고 사각형의 너비 구하기----')
'''
	ex5.py
----------------------------------------
	class Rectangle
	width , height
	getArea()
----------------------------------------
	r = Rectangle(200,300)
	print(triangle.getArea())  # 사각형의 너비 구하기 
'''

print()
print('----hw6: Rectangle, Triangle의 부모 클래스인 Figure 클래스를 작성하세요 ----')
class Figure:
    def __init__(self):
        print("Figure 초기화 함수")
        self.width=200
        self.height=100
    def getArea(self):
        return self.width*self.height/2

print()
print('----hw7: Rectangle, Triangle 은 Figure 클래스의 구현클래스로 코드를 변경합니다. ----')
class Triangle(Figure):
    def __init__(self):
        super().__init__()
    def getArea(self,width,height):
        return self.width*self.height/2
triangle = Triangle()
print(triangle.getArea(100,200))

class Rectangle(Figure):
    def __init__(self):
        super().__init__()
    def getArea(self,width,height):
        return self.width*self.height

r = Rectangle()
print(r.getArea(200,300))

print()
print('----hw8: method overriding ----')
''' getArea() 는 Figure 클래스 의 getArea()를 
    method overriding 시켜줍니다. 
'''
print()
print('----hw9: 두점 사이의 거리를 계산하는 pytagoras()를 완성하세요 ----')
import math

class Utility:
    def __init__(self):
        print("Utility의 초기화 함수")
    def pytagoras(self,x1,y1,x2,y2):
        return math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))
util = Utility()
print(util.pytagoras(100,100,200,200))

print()
print('----hw10:다음을 출력----')
'''
p = Point(100,100) # (x, y) 좌표 
	p.set_x(200)  # x좌표값을 200으로 변경
	p.set_y(300)  # y좌표값을 300으로 변경

	p.get_xy() # (200,300) 형태로 출력 
	
	p.move(500,300) # (200,300) ==> (500,300)
	                     # 메세지를 출력하고 x <= 500 y <=300을 담는다.
	
	참고 ) 모든 메세드는 인스턴스 메서드 모든 속성는 인스턴스 속성
'''
class Point:
    def __init__(self,x,y):
        print("Point 초기화 함수")
        self.x=x
        self.y=y
    def set_x(self,x):
        self.x=x
    def set_y(self,y):
        self.y=y
    def get_xy(self):
        print("(",self.x,",",self.y,")")
    def move(self,x,y):
        self.x=x
        self.y=y
        print("(",self.x,",",self.y,")")
p = Point(100,100)  # (x, y) 좌표 
p.set_x(200)        # x좌표값을 200으로 변경
p.set_y(300)        # y좌표값을 300으로 변경
print('----실행----')
p.get_xy()      # (200,300) 형태로 출력 
p.move(500,300) # (200,300) ==> (500,300)