class player:
    # 클래스 속성 : 인스턴스 끼리 공유
    cnt=0 
    bag=[]          # class에 bag이라는 리스트의 공유 속성 부여

    def __init__(self,name):
        print("초기화 함수")
        self.name=name
        player.cnt+=1
    
    def put(self,obj):
        player.bag.append(obj)
        print(obj+"를 bag에 넣었어☆.☆")
    
    # class method 로 만들어주기
    @classmethod
    def getbag(cls):
        print("아이템",cls.bag)
    
    def attack(self,other):
        print(other.name+"을 공격했습니다.")
    def greeting(self,other):
        print(other.name+"부모님은 잘 계시니?~~")


print('---------instance생성------')
p1=player("에코")
p2=player("야스오")
print("p1.cnt:",p1.cnt)
print("p2.cnt:",p2.cnt)

print()
print('---------attack------------')
p1.greeting(p2)
p1.attack(p2)

print()
print('---------bag---------------')
p1.put("권총")
print("p2 bag: ",p2.bag)    # instance명으로도 접근 하고
print("class:",player.bag)  # class명으로도 접근 가능하다

print()
print('----classmethod:getbag-----')
p1.getbag()
p2.getbag()