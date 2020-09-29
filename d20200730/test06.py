class Weapon:               # Weapon 이라는 부모 클래스 만든다
    def __init__(self):
        pass
    def use(self):
        pass
    def reuse(self):
        pass

class Gun(Weapon):          # Gun에 Weapon의 속성을 부여한다
    def __init__(self,name,bullet):
        print("Gun")
        self.namme=name
        self.bullet=bullet
    def fire(self):
        if self.bullet >= 1:
            print("공격: 총질 빵야~~~!")
            self.bullet -= 1
        else:
            print("틱~")
    def reload(self):
        print("장전: 찰칵")
        self.bullet=20
    def use (self):
        self.fire()

class Sword(Weapon):
    def __init__(self):
        print('Sword')
    def slicing(self):
        print("공격: 베기 시전!")
    def use (self):
        self.slicing()
    
class Bomb:
    def __init__(self):
        print('Bomb')
    def bombing(self):
        print("공격: 폭탄 투하!!")
    def use (self):
        self.bombing()
    
class Grenade:
    def __init__(self):
        print('Granade')
    def Grenading(self):
        print("공격: 수류탄 투하＠")
    def use (self):
        self.Grenading()
    

class Player:
    def __init__(self):
        print('Player')
        self.hp = 100
        self.weapon = None
        
    def moving(self):
        print("이동: 움직인다")
    
    def receive(self,weapon):         # 무기를 부여함
        self.weapon=weapon

    def use(self,weapon):             # 무기를 사용한다
        self.weapon.use()

p = Player()    # 플레이어 생성

s = Sword()     # 칼 생성
g = Gun("k2",20)# 총 생성

p.receive(g)    # 총 받기
p.use(g)        # 총 사용하기
