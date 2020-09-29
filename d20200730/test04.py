class Gun:
    def __init__(self,name,bullet):
        self.namme=name
        self.bullet=bullet
    def fire(self):
        if self.bullet >= 1:
            print("빵야~~~")
            self.bullet -= 1
        else:
            print("틱~")
    def reload(self):
        print("찰칵")
        self.bullet=20

class Police():
    def __init__(self, name, position, age):
        self.name = name
        self.position = position
        self.age = age
        self.gun = None        # gun의 기본값은 None으로 설정함!
    def receive_gun(self,gun): # 총을 부여함
        self.gun=gun
    def patrol(self):
        print("순찰중...")
    def arrest(self,who):
        print(who,'를 체포합니다.')
    def notify_miranda_rights(self):
        print("당신은 묵비권을 ......")
    def eat_donut(self):
        print("냠냠......")
    def use_weapon(self):      # 총 부여-사용 가능하게 함 
        if self.gun != None:   # 경찰객체가 총이 있으면!
            self.gun.fire()    # 총을 발사
print('----경찰에게 총을 주는 함수를 부여!!----')
g= Gun("m60리볼버",8)            # 총 g를 생성
p=Police("포돌이","순경",20)     # 경찰 p를 생성
p.receive_gun(g)                # p에게 총을 줌
p.use_weapon()                  # p가 총을 쓰게 함

p1 = Police("Mia","경위",20)
p1.patrol()
p1.arrest("고양이")
p1.notify_miranda_rights()
p1.eat_donut()
print()