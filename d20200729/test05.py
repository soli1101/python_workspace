from test09 import animal

class monkey(animal):
    def __init__(self):
        print("원숭이 초기화")
        self.eyes=2
        self.mouth=1
        self.hands=2
        self.ears=2
        self.species="흰꼬리원숭이"
        self.name="dancing diva"
    # def eating(self):
    #     print("바나나를 까먹어요 바나바나!")
    # def sleeping(self):
    #     print("잠을 자요~ 미인이라서...zzz")
    def dancing(self):
        print("나는야 ★ dancing diva!!＊＊★")
    def jump(self):
        print("원숭이도 뛴다요!!")

if __name__=="__main__":
    r = monkey()
    print(r.eyes)
    
    r.jump()
    r.eating()
    r.sleeping()
    r.dancing()