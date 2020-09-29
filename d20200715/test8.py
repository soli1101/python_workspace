#문제 a: 100, b: 200, c:300 --> a:300, b:100, c:200
a,b,c = 100,200,300
print("before a:",a,"b:",b,"c:",c)
a,b,c = c,a,b
print("after a:",a,"b:",b,"c:",c)

#문제 각변수의 값에서 10씩 증가
a += 10
b += 10
c += 10
print("a.after a:",a,"b:",b,"c:",c)

#사칙연산
a, b = 10, 20
print(a+b)
print(a-b)
print(a*b)
print(a/b)      # int 연산 int ==> int 0.5
print(a//b)     # int/int ==> int (2.0 방식 연산구현)
print(a%b)      # 나머지값을 구하는 연산자 
#Shift + Alt + 화살표 아래 방향키
print("--------------------------------")
a= -a
print(a)
print("--------------------------------")

#msg = input("출력할 메세지를 입력하세요") #입력할 값을 변수에 담고
#print(msg)                              #'메아리' 그것을 출력

#문제3 사용자로 부터 두 수를 입력받아 화면에 출력
x = input("첫번째 출력값 입력해")
y = input("두번째 출력값 입력해")
print("x:",x,"y:",y)
print(x+y)
x = int(x) #x의 값을 정수로 바꿔줌
y = int(y) #y의 값을 정수로 바꿔줌
print(x+y)
