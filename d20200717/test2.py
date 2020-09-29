print('***********자료형***********')
s='sequence'
print(s, len(s), s.count('e'), s.find('e')) 
    # └count: ()의 문자가 몇개 있니? / 
    # └find: e가 몇번째 자리인지 찿아줘
print(s.find('e',3), s.rfind('e'))
ss = 'mbc'
print('mbc', type(ss), id(ss))
print()
print('********문자열 자르기********')
print(s, s[2:4], s[:3], s[3:], s[3::2]) # sequence, qu, seq, uence, une

# 공백제거함수
msg = " Hello Python "
print(msg)                 # msg를 출력해
print(msg.strip())         # 공백을 지워
print(msg.rstrip()+"^^")   # right 공백을 지워
print(msg.lstrip())        # left 공백을 지워
print('----------연습1-----------')
#연습1 m 리스트 만들고 반복 출력
msg = "구정,신정,성탄절,초파일,추석"
m = msg.split(",")
for i in m:
    print(i) 
print('-------------------------')
str_time = ['10','44','30']
print(str_time)           # join 없이 출력했을 때
print(":".join(str_time)) # join을 사용 했을 때

# 문자열을 , 단위로 잘라서 리스트 ==> split(",")
# 리스트에, 문자를 붙여서 문자열로 ==> ",".join(리스트)

print('-------------------------')
msg3 = list('hello')
print(msg3)
print('-------------------------')
print(msg3[4])
print('-------------------------')
msg3[0]='m'
print(msg3)