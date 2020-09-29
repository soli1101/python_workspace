class SiegeTank:
    def __init__(self):
        self.hp=200
        self.attackpoint=30
        print("객체 초기화")
    def cannon(self, other):
        if other.hp > 4:
            other.hp -= self.attackpoint
        else:
            print("고마 해라... 마이 뭇다 아이가")
        print("체력이 %d 상태입니다"%other.hp)
    def Shockcannon(self, other):
        if other.hp > 60:
            other.hp -= 70
        else:
            print("고마 해라... 마이 뭇다 아이가")
        print("체력이 %d 상태입니다"%other.hp)
    def SiegeMode(self):
        print("공성에 돌입했습니다!")
    

class Ghost:
    def __init__(self):
        self.hp=100
        self.attackpoint=4
        print("객체 초기화")
    def nuclearlaunch(self, other):
        other.hp = 0
        print("안녕.... 좋은 세상이었다...")
    def attack(self, other):
        if other.hp > 4:
            other.hp -= self.attackpoint
        else:
            print("고마 해라... 마이 뭇다 아이가")
        print("체력이 %d 상태입니다"%other.hp)
    def move(self):
        print("GoGoGo")

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
md=medic()  # 메딕 생성
md.heal(m1) # 메딕 힐링
md.hold()

print('----------marine->Ghost공격-----------')
G1=Ghost()
m1.attack(G1)

print('----------medic->Ghost치료-----------')
md.heal(G1)

print('----------Ghost->Marine공격-----------')
for i in range(10):
    G1.attack(m1)

print('----------Ghost->Medic공격-----------')
for i in range(5):
    G1.attack(md)

print('----------Ghost->Medic공격-----------')
G2=Ghost()
for i in range(8):
    G1.attack(G2)

print('----------SiegeTank->Maine공격-----------')
Tank1=SiegeTank()
Tank1.cannon(m1)
Tank1.SiegeMode()

print('----------SiegeTank->Medic공격-----------')
Tank1=SiegeTank()
Tank1.cannon(md)
Tank1.SiegeMode()

print()
print('----hw4: TV 객체를 생성할수 있는 클래스를 작성하세요----')
''' turnOn(), turnOff(), changeChannel(n) '''
class TV:
    def __init__(self):
        print("객체 초기화")
    def turnOn(self):
        print("TV가 켜졌습니다!")
    def turnOff(self):
        print("TV가 꺼졌어요. 안녕~!")
    def changeChannel(self):
        print("채널을 바꿉니다!!")
tv = TV()
tv.turnOn()
tv.turnOff()

print()
print('----hw5: Handphone 클래스를 작성하세요----')
'''	hp = HandPhone()
	hp.call("010-1234-5678")  #011-1111-2222에서  010-1234-5678번으로 전화거는중 
	hp.phone_number= "010-1234-5678" # 011-1111-2222 에서 전화번호를 010-1234-5678 로변경함 
	hp.connect_internet() # 인터넷에 연결되었습니다. 
'''
class HandPhone:
    def __init__(self):
        self.phone_number="011-1111-2222"
    def call(self, number):
        print(hp.phone_number,"에서",number,'번으로 전화거는중')
    def connect_internet(self):
        print("인터넷에 연결되었습니다.")

hp = HandPhone()
hp.call("010-1234-5678")
hp.phone_number="010-1234-5678"
print(hp.phone_number)
hp.connect_internet()
