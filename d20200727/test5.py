print('----#import 하는 방법----')
print('ㅇㅇㅇㅇㅇ1. import 모듈ㅇㅇㅇㅇㅇ')
import random
import math
print(dir())
print('ㅇㅇㅇㅇㅇ# 2. from 모듈명 import 함수명 ㅇㅇㅇㅇㅇ')
# 모듈에서 함수 한개만 꺼내오는 방법
# 거기 안에서 어떤 함수만 가져올게!! 난 그것만 필요해~
# 이 경우 다른 모듈에 동일함 함수가 있을 경우 충돌 날 우려 있음 
from random import randint
# from deabak import randint
n=randint(100,200)
print(n)
print(dir())
print('ㅇㅇㅇㅇㅇ# 3. from random import *ㅇㅇㅇㅇㅇ')
# 그 모듈에 있는 거 다 불러와!
# random.-- 처럼 이름 안써줘도 쓸 수 있다!
from random import *
print(dir())


