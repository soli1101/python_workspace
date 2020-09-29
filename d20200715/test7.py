# 숫자형 변수
# 정수형 (integer) ==> int
# 실수형 (float) 3.14 
# 복소수 (complex 1.3 + 1.9j)

# 동적타이핑 언어 - 자료형을 미리 결정하지 않고 
#                  나중에 할당하는 순간 자료형을 결정한다
a = 10             #a변수에 10을 대입
print(type(a))     #어떤 타입인지 출력
b = 20             #b변수에 20을 대입
c = "10"
# 형변환 : int(), float(), complex(), str()
print(b, type(b))         #b변수와 b변수의 타입을 출력
print("a:" + str(a))      #a:에 a변수값 출력
print("b:" + str(b))      #b:에 b변수값 출력
print("c:"+c)             #c:에 b변수값 출력 +는 앞에있는 문자와 
                          #뒤에있는 문자를 붙여: 연결연산자
# a ==> 10 , b = 20
# 
# b = 10, a = 20
print("before : a:",a,"b:",b)
                          # 임시변수를 만든다 : temp 
temp = 0
                          # 첫번째 변수의 값을 임시변수에 담는다.
temp = a                  # temp변수에 a값을 대입
                          # 두번째 변수의 값을 첫번째 변수에 담는다.
a = b 
                          # 임시변수의 값을 두번째 변수에 담는다.
b = temp
                          # 끄읏~~~
print("after : a:",a,"b:",b)

a, b = b, a                #a에는 b를 대입, b에는 a를 대입
print ("====> : a :",a, "b:", b)

x=10                       #x변수에 10을 대입해
y=10                       #y변수에 10을 대입해
z=10                       #z변수에 10을 대입해
print("x:",x,"y:",y,"z:",z)#x,y,z를 출력해 

x=y=z=20                   #x,y,z에 20을 대입해
print("x:",x,"y:",y,"z:",z)#x,y,z를 출력해

i, j = 100, 200
print ("i:",i,"j:",j)

#아무것도 없는 값
x = None #다른 언어들은 null
print("x:",x) 

a = 100        # a변수에 100의 값을 대입해
               # 20을 증가시킨 후 출력
a = a + 20     # a변수에 20을 더한 후 a변수에 대입해
print("a:",a)

a += 20        # a변수에 20을 더한 후 a변수에 대입해
print("a:",a)

