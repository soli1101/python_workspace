print('***decorator:함수안에 매게변수로 함수를 넣을 수 있다***')
def make2(fn):
    # def test():                      # 함수식
    #     return "곤니찌와" + fn()
    return lambda : "곤니찌와" + fn()   # 람다식

def make1(fn):
    return lambda : "니하오" + fn()
# def  이름없음():                 
#       return "니하오" + fn()
# 함수에 이름을 안주고 "니하오"와 fn()함수를 붙여서 return해
def hello():
    return "한라봉"        # return은 그 값을 날 불러온 애 한테 
                          # 덮어씌워 라는 뜻
t = make1(hello)
t2 = make2(t)   # make2(make1(hello))
print(t2())     # make2(make1(hello))()

print(t( ))
print(make1(hello)())

# decorator 데코레이터 : 다른 언어에서는 annotation이라고 한다
@make2
@make1                       # @함수명 을 쓰면 make1함수안에
def hello2():                # make1(hello2()) 결과를 얻는다
    return "소망이"          # 중첩한 효과!
hi = hello2
print(hi())
