print('***********CLASS연습***********')

class Person:
    ''' doc string : 이 클래스가 무엇인지 설명
    인간 클래스
    '''
    def __init__(self): # 항상 처음에는 self 키워드가 들어감
        print(id(self)) # self는 'instance'에 주소를 전달해! 라는 뜻
        print("초기화 함수")
        self.name="내 이름은 홍.길.동!"
        self.age='난 ☜ 20살☞ 이지!! 하하하' 
        self.job="내 직업은 멋있는 도적§"
    def eating(self, what):
        print(self.name,"이",what,'을/를 맛있게 먹어요♬')

p1 = Person()
print("id: ",id(p1))
print('-------------------------')

print(p1.name)
print(p1.age)
print(p1.job)
p1.eating("apple")

print()
print('----2번째 Person 만들기----')
p2 = Person()
print(p2.name)
print('-------------------------')
print("id(p1):",id(p1),"id(p2):",id(p2))