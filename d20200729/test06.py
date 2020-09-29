from test09 import animal

class whale(animal):
    def __init__(self):
        print("고래 초기화")
        self.eyes=2
        self.mouth=1
        self.species="흰수염고래"
        self.name="dancing queen"
    # def eating(self):
    #     print("크릴새우 크릴크릴!")
    # def sleeping(self):
    #     print("잠을 자요~ 수면위에서??...zzz")
    def dancing(self):
        print("나야말로 이 시대의 ★ dancing Queen!!＊＊★")
    
if __name__=="__main__":
    r = whale()
    print(r.eyes)
    
    r.eating()
    r.sleeping()
    r.dancing()