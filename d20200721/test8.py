print('----연습2: 리스트에서 최대값 출력----')
# 1. 랜덤하게 10개의 숫자를 생성(1~999)
# 2. 이것을 리스트에 담는다.
# 3. 임시변수를 선언한다.
# 4. 리스트의 모든 요소와 비교해서 큰 값을 임시변수에 담는다.
# 5. 임시변수에 들어있는 값이 최대값이다 출력

import random                 # random을 불러온다
data = []                     # 이름이 data인 빈 list를 만든다
for i in range(10):           # 랜덤을 10번 돌려서 data에 담는다
    n = random.randint(1,999)
    data.append(n)
print(data)                   # data를 출력해 본다

temp=-1                       # 임시변수 temp에 -1을 준다
for i in data:                # data에서 i를 뽑아서
    if i > temp:              # temp값과 비교해서 크면 
        temp = i              # temp에 그 i값을 대입한다

print(temp)                   # 가장 큰 최대값이 들어간다
print('----연습2-1: 최소값 출력하기----')
# 아 허무해
print(min(data),max(data))
