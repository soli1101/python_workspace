print('----# 연관된 함수들의 모음 : 모듈 Module#----')
# Module의 이름은 파일이름! 해당 파일에서 부를 땐 __main__이고
# 외부 파일에서 불러오면 파일이름이 이름이 된다!
# __name__ <-- 모듈의 이름을 가진 변수 

author = "홍길동"           # 작성자! author로 표시

print('----#1# raise_sal(sal)----')
def raise_sal(sal):
    '''급여를 전달하면 10% 인상된 급여를 리턴'''
    return sal*1.1
# 3300.0000005, 컴퓨터에서 실수를 표현할 때 발생하는 오차

print('----#2# reduce_sal(1000)----')
def reduce_sal(sal):
    return sal*0.8

print('----# Test Code ----')  # 이 파일 안에서만 실행되도록 함
if __name__ == "__main__":     
    print(int(raise_sal(3000)))
    print(int(reduce_sal(1000)))
    print("잘나오나?:",author)
    print(__name__)            # __m^.^m__ 