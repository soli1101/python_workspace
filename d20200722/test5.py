# 객체 : mutable , immutable
# 
# immutable : bool, int, float, tuple, str
# mutable : list, set, dictionary
a=100 # a변수 100이라는 값을 대임
b=a   # b변수 a변수의 값을 대입
print(type(a), type(b))
print(id(a),id(b))      # reference 값을 갖게 함으로써 표현
a+=1
print("a:",a,"b:", b)   
print(id(a),id(b))
print('-------------------------')
m=[1,2,3]
n=m
print(id(m),id(n))
print('n[0]:',n[0])
n[0]=100
print('n[0]:',n[0],'m[0]:',m[0])
print('id(n):',id(n),'id(m):',id(m))
print('-----슬라이싱해서 주소변경-----')
k = m[:]            # 슬라이싱해서 처음부터 끝까지 다 잘라서 넣어
print('id(m):',id(m),'id(k):',id(k))

print('----------is!!-----------')
c = [10,20,30]
d = c[ : ]
print('id(c):',id(c),'id(d):',id(d))
print(c==d)     # == 사용하면 내용만 비교하는 것
print(c is d)   # is 는 같은 참조값을 가지는지를 비교하는 것

print('-------------------------')
q = [[1,2],[3,4]]   # 1 2
                    # 3 4

p = q[ : ]                  # p는 q 전체를 슬라이싱 해 와
print('q-d:',id(q),'p-d:',id(p))    # 다른 값
print(id(q[0]),id(p[0]))    # 내부의 객체는 같은 주소
                            # (리스트 안의 리스트는 id가 같다...)
q[0][0]=5
print(p[0][0])

# shallow copy : 겉에만 복사
# deep copy : 아주 자세한 복사
print('*****DEEP copy!! copy.deepcopy모듈사용!*****')
print('-----s와t리스트는 달라도 내부값은 같다!!-----')
import copy
s = [[1,2],[3,4]]       
t = copy.deepcopy(s)   # deepcopy모듈을 사용해서 s를복사한다

print("id(s):",id(s),"id(t):",id(t))
print("id(s[0]) :",id(s[0])," id(t[0]):",id(t[0]))
print()
print('-----s값을 바꾸면 뭐가 바뀔까??-------')
s[0][0]=300
print("s[0][0]:",s[0][0],"t[0][0]:",t[0][0])
print("id(s) :",id(s)," id(t):",id(t))
print("id(s[0]) :",id(s[0])," id(t[0]):",id(t[0]))
print()
