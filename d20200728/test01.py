print('***********CLASS***********')
'''
class 클래스명:
    속성

#   함수, method
#   객체 : 사물
#   class : 설계도
#   대상 : instance
'''
class Human:                # __함수__ : magic method
    def __init__(self):     # initialize 초기화: 초기화 하는 
        print("초기화 함수") # 순간 자동호출
    def eating(self):
        print("냠냠 맛있게 먹어요")
    def sleeping(self):
        print("쿨쿨 잠을 자요")


hong = Human()  # instance(실체): Human 클래스를 실행해서 hong이라는 실체를 만듦
print(hong)     # hong = new Human() --> 파이썬은 없음
hong.eating()
hong.sleeping()

print()
print('----새로운 Human만들기----')
lucy = Human()  # 앞에 정의된 class에서 계속 불러올 수 있음
lucy.eating()   # 예를 들면 class는 붕어빵 틀을 만들어 놓은 것!
lucy.sleeping()
