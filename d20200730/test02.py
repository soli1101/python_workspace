class Car:
    def __init__(self):
        print('초기화 함수')
    def __del__(self):
        print('소멸자 호출: 더 이상 이 객체를 안써요... 폐 차^^')
    def __str__(self):
        # 문자열화 해서 반환 
        return "str method가 호출됨"
    #매직함수 : 가장 일반적인 용도: 오퍼레이터 오버로딩용 
    # + : __add__
    # - : __sub__
    # * : __mul__
    # / : __truediv__
    # //: __floordiv__
    # % : __mod__
    # **: __power__ (제곱)
    # < : __lt__ (less than)
    # > : __gt__ (greater than)
    # >=: __ge__ (greater equal)

c2=Car()
print(str(c2))
del c2
