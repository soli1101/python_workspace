from test09 import animal

# 부모클래스 base class, super, parent
# 자식클래스 derived class, child
# self: 자기 자신 / super: 부모 

class Rabbit(animal):
    def __init__(self,foots):
        super().__init__(foots)   ###부모의 init을 불러온다!!!###
        print("토끼 초기화")
        # self.eyes=2
        # self.mouth=1
        # self.ears=2
        # self.species="앙골라"
        # self.name="토순이"
    def jump(self):
        print("깡총깡총 뛰어요>,<")
    # def eating(self):
    #     print("당근을 먹어요▽")
    # def sleeping(self):
    #     print("쿨쿨 자요~~zzz")

if __name__=="__main__":
    r = Rabbit(4)
    print(r.eyes)
    print(r.foots)

