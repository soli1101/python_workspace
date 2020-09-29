print('------- 문제3 -------')

# 태어난 년도를 입력하면 띠 출력
# 년도를 12로 나눈 나머지를 구한다
# 자축인묘진사오미신유술해
# 4,5,6,7,8,9,10,0,1,2,3

year = input("출생년도는?")
year = int(year)
mod = year%12
if mod == 4: 
    print('쥐띠')
if mod == 5: 
    print('소띠')
if mod == 6: 
    print('호랑이띠')
if mod == 7: 
    print('토끼띠')
if mod == 8: 
    print('용띠')
if mod == 9: 
    print('뱀띠')
if mod == 10: 
    print('말띠')
if mod == 11: 
    print('양띠')
if mod == 0: 
    print('원숭이띠')
if mod == 1: 
    print('닭띠')
if mod == 2: 
    print('개띠')
if mod == 3: 
    print('돼지띠')
