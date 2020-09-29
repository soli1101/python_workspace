import time

# help(time)

# help(time.time)
print(time.time()) # 1970.1.1부터 지금까지의 초
print('----#ctime에서 년도값만 출력하기----')
print(time.ctime(), type(time.ctime()))
m = time.ctime().split()            # 공백단위로 끊어오기
print(m[4])
print(m[-1])                        # 뒤에서 첫번째 불러오기

# print('----#ctime 1초에 한번씩 출력하기----')
# while True:
#     time.sleep(1) # (process)에게 1초 잠들어라...
#     print(time.ctime())

print(dir(time)) # time 모듈에 있는 함수 목록을 볼 수 있다