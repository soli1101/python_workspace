# print('----#hw1: 세계최초의 암호화 ----')
# # setEncryption(문자열) 함수 생성
# # 1. 사용자로부터 단어를 입력받는다
# # 2. 글자를 불러와서 아스키코드 값으로 바꾸고 
# # 3. 그것에 3을 더해서 출력한다.
# # 4. 끝에 3자는 다시 a,b,c가 될 수 있도록
# # 5. 3번째 뒤에 글자를 출력한다.
# # 6. getDecode(~~~암호값) 함수 생성
# #hw_teacher
# def setEncryption(msg):
#     v = ""                      # 문자열 빈 변수 만들기
#     for i in range(len(msg)):   # msg의 문자열에서 한글자씩
#         code=ord(msg[i])        # 아스키 코드값을 구하고
#         code+=3                 # 구한 코드값에서 +3을 해주고
#         if code >= 91 and code <=93 :   # XYZ->ABC
#             code-=26
#         elif code >= 123 and code <=125:# xyz->abc
#             code-=26
#         # print(chr(code))      # 이 값을 문자열로 변환시켜서
#         v+=chr(code)            # 문자열로 변환시켜서 v에 누적
#     # print(v)
#     return v                    
# data = 'Hello'
# x= setEncryption(data)
# print(x)
# print('---------deCode---------')
# def deCode(aaa):
#     e = ""
#     for j in range(len(aaa)):
#         decode=ord(aaa[j])
#         decode-=3
#         if 94 <= decode <=96:
#             decode+=26
#         elif 62 <= decode <=64:
#             decode+=26
#         e+=chr(decode)
#     return e
# p=deCode(x)
# print(p)
# print()
# print('----#hw2: 6행 5열 행열 만들고 총점 및 평균 구하기 ----')


print('----#hw3: 야구 게임 만들기----')
import random
com = []
cnt = 0
while len(com) <3:
    rnd = random.randint(0,9)
    if rnd in com:
        continue
    else:
        com.append(rnd)
print("컴퓨터 랜덤숫자: ",com)
cnt = 0          # 몇회만에 성공했는지를 보여주기 위한 숫자!
while True:      # 무한 반복!! 
    cnt+=1       # 이 while이 한 번 돌 때마다 1씩 카운트 해준다!            
    # 2. 사용자로 부터 값 입력받아 리스트에 한개씩 넣어주기
    userdata = int(input("3자리 숫자를 입력하세요~!: "))
    user = []                       # 사용자가 입력한 값을
    user.append(userdata//100)      # 컴퓨터 값과 비교하기 위해
    user.append(userdata%100//10)   # 한개씩 리스트에 붙여주기!!
    user.append(userdata%10)
    # 3. 판별한다
    strike = 0
    ball = 0 
    for i in range(3):                  
        if com[i] == user[i]:           # 자릿값이 같을때 같은 수
            strike+=1                   # 인지 판별!!
        else:
            for j in range(3):          # ** 이부분이 핵심!!!
                if com[i] == user[j]:    # com값과 user값을 비교해서
                    ball+=1             # ball을 카운트!!!!
    print(str(strike)+'S'+str(ball)+'B')
    if strike==3:
        print("정답! 축하합니다.",cnt,"회만에 성공하셨습니다.")
        break