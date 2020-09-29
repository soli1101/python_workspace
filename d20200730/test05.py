# has - a 관계
# Aggregation Relationship

# 자동차 -- 엔진
# Composition Relationship
class Engine:
    def __init__(self):
        print("GDI 엔진입니다...")
    def start(self):
        print("엔진 동작하는 중")

class Car:
    def __init__(self):
        print("붕붕카~")
        self.engine=Engine()  # 아예 초기화 할 때 엔진 생성
        print("엔진 장착")
    def run(self):
        self.engine.start()

c = Car()
c.run()