'''
	ex.py 
----------------------------------------
	class Triangle 
	width , height
	getArea()
----------------------------------------	
	triangle =	Triangle (100,200) # 너비 100, 높이 200 
	print(triangle.getArea())  # 삼각형의 너비 구하기 
'''
class Triangle:
    def __init__(self,width,height):
        print("triangle 초기화 함수")
        self.width=width
        self.height=height

    def getArea(self):
        return self.width*self.height/2
triangle = Triangle(100,200)
print(triangle.getArea())
