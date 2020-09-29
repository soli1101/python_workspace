# 0-9 사이의 정수를 랜덤하게 생성
# 예외란? 프로그램 실행 중 발생한 예상치 못한 오류: 가벼운 오류
# 예외를 처리 해 줄 수 있다.

# casebycase 

# try:
#   문장1
#   문장2
# except ????:
#   예외처리문장1:
#   예외처리문장2:

##사용자 정의형 에러
class EvenError(Exception):
    def __init__(self,msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg

import random
try:
    n = int(input("숫자입력: "))
    # 사용자 정의형 에러
    # 사용자가 입력한 값이 짝수이면 실행안함
    # 원래 시스템상의 에러가 아니라 내가 만든 것 
    if n%2 == 0 :
        raise EvenError("짝수만 입력해라... -.-")

    for i in range(10):
        a = random.randint(0,10)
        print(n/a)
except EvenError as ee: # EvenError의 이름을 ee라고 해
    print(ee)           # ee를 찍어봐 
    print("짝수는 계산 안해줘~~")
except ValueError:
    print("숫자만 입력하세요")
except ZeroDivisionError:
    print("0으로 나눌 수 없음")
finally:
    print("이 부분은 예외가 있던 없던 항상 실행됩니다 ♥ ")

E1 = EvenError("안뇽")
print(E1)