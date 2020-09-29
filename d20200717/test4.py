print('***********튜플***********')
t2=('a','b','c','d')
print(t2, type(t2))      # t2의 타입과 t2를 출력해
print()
print(t2, len(t2))       # t2의 갯수와 t2를 출력해
print()
print(t2.count('a'))     # t2에서 a 요소의 갯수

x = (1,2,3)
# x[0] = 10  수정불가!!
print(x)

x2=(3)                  # 튜플이 아니라 정수형으로 본다
x3=(3,)                 # ,까지 넣어야 튜플이라고 본다
print(x2, type(x2))
print(x3, type(x3))

print('--튜플을 리스트로 형변환 뒤 다시 튜플로 형변환---')
# == > 3을 30으로 수정   
print("x:",x)
y=list(x)
y[2]=30
print()
print(y)
print()
x=tuple(y)
print("x:",x)

print('----#연습3 튜플안에 있는 2값 교환----')
# t1=(10,20)
# y=list(t1)
# y[0], y[1] = y[1], y[0]
# y=tuple(y)
# print(y)

t1=(10, 20)
a, b = t1
a, b = b, a
t1 = (a, b)
print(t1)