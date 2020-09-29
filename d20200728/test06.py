class marine:
    def __init__(self):
        self.hp=100
        self.attackpoint=4
        print("객체 초기화")
    def attack(self, other):
        if other.hp > 4:
            other.hp -= self.attackpoint
        else:
            print("고마 해라... 마이 뭇다 아이가")
        print("체력이 %d 상태입니다"%other.hp)
    def move(self):
        print("GoGoGo")
    def steampack(self):
        if self.hp >= 6:
            print("힘이솟아요! 뿅뿅~")
            self.hp-=5
            print("체력이 %d 상태입니다"%self.hp)

class medic:
    def __init__(self):
        self.hp=100
        self.x=0
        self.y=0
        self.mp=50
        self.defense=100
        self.healforce=10
    def heal(self, target):
        target.hp += self.healforce
        print("대상의 체력이 %d 상태입니다"%target.hp)
    def move(self):
        print("GoGoGo")
    def hold(self):
        print("현재 위치를 사수합니다...")
        
print('-------marine생성&공격--------')
m1=marine() # 마린1 생성
m2=marine() # 마린2 생성
m1.steampack()  # 스팀팩 사용

print('----------medic힐링-----------')
me=medic()  # 메딕 생성
me.heal(m1) # 메딕 힐링
me.hold()
