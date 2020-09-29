print('----#함수----')
# 반복되는 코드를 줄여주기 위해 
# 특정 코드에 이름을 부여해 놓은 것
# 내장함수
# def 함수명(매게변수,매게변수, 매게변수 --):
#   처리할 문장
#   처리할 문장
#   return 결과값
print('11111111')
def double(x):
    print('2222222')
    return x*2
print('3333333333')

y=double(10)  # 전달하는 값을 argument라고 한다 : 인수
print(y)

k=double(20)
print(k)
print()

print('----#로또번호 생성기----')
import random
def getLotto(m):
    for k in range(m):              # 코드를 m변수 만큼 반복한다
        lotto=[]                    # 빈 lotto 리스트 생성
        for i in range(6):              # 1. 1~45사이의 랜덤한 정수를 생성한다.
            i = random.randint(1,45)    # 2. 로또리스트에 담는다.
        i = 0                           # 3. 중복된 값이 있으면 다시 뽑는다.
        while i<6:                   # i가 6이하 일 때 아래를 반복해
            j = random.randint(1,45) # j변수에 1~45사이의 랜덤값 담아
            if j in lotto:           # 만약 로또리스트에 j값이 있으면
                continue             # 이번엔 스킵하고 처음으로 돌아가
            else:                       
                lotto.append(j)      # 로또리스트에 j랜덤값을 더해줘 
                i+=1                 # i는 1씩 증가하며 6개 까지만 해
        # print(lotto)                  # 4. 6자리가 모두 들어가면
        lotto.sort()                    # 5. 정렬한다.
        print(lotto)                    # 6. 출력한다.
getLotto(3)

# import random
# a = range(1,46)
# lotto = random.sample(a,6)
# lotto.sort()
# print(lotto)


