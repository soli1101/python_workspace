class Rectangle:
    def __init__(self,width,height):
        print("Rectangle 초기화 함수")
        self.width=width
        self.height=height
    def getArea(self):
        return self.width*self.height

r = Rectangle(200,300)
print(r.getArea())
