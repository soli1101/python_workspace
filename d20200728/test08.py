class gugudan:
    def __init__(self):
        print("초기화 함수 호출")
        self.dan=2

    def print(self):
        for i in range(1,10):
            print(self.dan,'x',i,'=',self.dan*i)

g = gugudan()
g.dan = 7
g.print()
