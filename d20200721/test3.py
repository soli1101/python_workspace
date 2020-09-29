print('------- # 가위바위보 -------')

# 1. 가위바위보 라는 글자를 가진 리스트를 선언
# 2. 0, 1,2 중 한개를 리턴하는 랜덤인트를 사용해서
# 3. 리스트의[]번호로 삼고 출력!

import random

li = ["가위", "바위", '보']
idx = random.randint(0,2)
print(idx, li[idx])
print('-------------------------')
print('1. 가위  2. 바위  3. 보')
userinput = int(input("가위바위보 중 선택하세요!"))
userinput-=1      # 컴퓨터의 랜덤 인덱스값과 일치시키기 위해 -1
print(userinput)
print('--------#승부판정---------')
# 사용자의 입력값과 컴퓨터의 랜덤값의 차를 비교
print("사용자 입력값: ", userinput, li[userinput])
print("컴퓨터 랜덤값: ", idx, li[idx])
print("차이값: ", userinput-idx) 
if userinput-idx == 0:           # 차이값이 0이면 비김
    print("비김")
elif userinput-idx < 0:          # -값:사용자승
    print("사용자 승!")
elif userinput-idx > 0:          # +값:컴퓨터승
    print("컴퓨터 승!")
                    
