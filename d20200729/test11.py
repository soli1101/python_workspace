from test10 import parent

class child(parent):
    def __init__(self):
        super().__init__()  # 부모의 __init__ 불러오기
        self.score = 100
        self.name = "홍길동"
        self.age = 20
    
    # method overriding : 부모가 준거 안쓰고 다시 정의한다!!
    def singing(self): 
        print("와~ 여름이다~! 해변의여인~야이야이야이야이 바~")

    def goClub(self):
        print("움칫 ~ 둠칫~")

if __name__ == "__main__":
    c = child()
    print(c.score)
    print(c.name)
    print(c.age)
    print('-------------------------')
    c.eating()
    c.singing()
    c.goClub()

