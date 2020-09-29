# 부모클래스 animal
class animal:
    def __init__(self,foots):
        print("초기화 함수")
        self.eyes=2
        self.mouth=1
        self.ears=2
        self.foots=foots

    def eating(self):
        print("먹이를 먹어요▽")

    def sleeping(self):
        print("쿨쿨 자요~~zzz")

