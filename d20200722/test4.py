print('-----#가변인수 연습-----')
# 이름: 홍길동  직업: 도적  나이:20  사는곳: 율도국  키:180.3

def show_info(name, job, age, addrs, height):
    print("이름:{0}, 직업:{1}, 나이:{2}, 사는곳:{3},키:{4}".format(name, job, age, addrs, height))

p={'name':"홍길동","job":"도적","age":20,"addrs":"율도국","height":180.3}
print(p)
# show_info("홍길동", "도적", 20, "율도국", 180.3)
print()
print('-------**사전명: value값을 불러옴------')
show_info(**p)  # 내가 주는애가 dictionary야! 
                # 이 dictionary를 인수 기준으로  
                # value값을 하나씩 대입해서 unpacking 해서 넣어줌 
print()
print('------*사전명: key값을 불러옴------')
show_info(*p)   # *한개는 key값만 unpacking 해서 넣어줌 
print()         # 주로 list, tuple 등
print('------#position 대입------')
def test(a,b,c):
    print("a:",a)
    print("b:",b)
    print("c:",c)

test(b=20,a=10,c=30)

print('------#연습문제------')
# x 리스트 값들의 합을 구하기
x = [10,20,30]

def sumvalue(a,b,c):
    return a+b+c
  
print(sumvalue(*x))

print('------#가변인수로 함수 만들수 있다------')
def sumvalue2(a,*b): # *b는 args 아규먼트라고 관습적으로 많이씀
    print("b:",b)    # 튜플 값으로 읽어냄
sumvalue2(10,x)

print('------#keyword argument------')
def show_info2(**kwargs):# kwargs 키워드아규먼트라고 많이씀
    for kw, arg in kwargs.items():
        print(kw,":",arg, sep=" ")
show_info2(name="홍길동")
show_info2(**p)

print('---#함수 연습하기 : find_birth---')
def find_birth(ssn):
    print(ssn[0:2]+"년",ssn[2:4]+"월",ssn[4:6]+"일")
find_birth('880101-1234567')
#  출력 88년 1월 1일
