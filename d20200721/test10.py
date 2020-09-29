print('----함수 : 여러개의 실행문을 하나의 묶음으로 만든 실행단위 ----')
print('    └내장함수 : 설치할 때 포함된 함수 ')
print('    └사용자지정함수 : def 함수명(): ')
print('                         처리할 문장')
print('                         처리할 문장')
print('                         return (반환)')
print()
print('----연습3: 별 1개씩 늘려가면서 출력하기 ----')
def printStar(num):             # printStar라는 함수로 정의해 줌
    for n in range(1,num):      # (num)을 넣어줌으로써 
        print('*'*n)            # 나중에 바뀌는 값이라는 뜻
    return                      # 나를 부른애한테 줘
printStar(3)                    # num에 자동으로 3이 들어감
print('--------------')
printStar(2)                    # num에 자동으로 2이 들어감
print('--------------')
printStar(7)                    # num에 자동으로 7이 들어감
print()
print('----연습4: 구구단3단을 출력하는 코드----')
def gugudan(num):
    print('--------------------',str(num),'단')
    for i in range(1,10):
        print(num,"X",i,'=',num*i)
# gugudan(1)
# gugudan(2)
# gugudan(3)
print()
print('----연습5: 1~지정한 값까지 누적합----')
def accumulated(num1):          # 함수를 선언
    sum = 0                     # sum 이라는 변수에 값 0 대입
    for i in range((num1+1)):   # 0~지정값 까지 i에 대입 반복해
        sum=sum+i               # sum에 sum + i값을 대입해
    print('1부터'+str(num1)+'까지의 합은'+str(sum))# sum을 출력해
        # 지금 계산한 값을 날 호출한 코드에 전달하고 싶다
    return sum                  # 날 호출한 애한테 이 값을 줘
    print("이이하ㅣ히ㅏ망러")    # 노란밑줄은 dead code 어짜피 실행안되는 코드
accumulated(10)                 # 함수를 실행해
print(accumulated(100))         # 함수를 실행한 결과값을 출력해

x = accumulated(50)
y = accumulated(100)
print(x+y)

print('----연습7: 1~지정한값까지 no배수의 누적합----')
def odd(num,no):
    value = 0
    for i in range(1,num+1):
        if i%no == 0 :
            value+=1
    print(value) 
    return value
# print('-------------------------')
a= odd(8,2)
b= odd(9,3)
print(a+b)

# print('----연습8: 지정값의 배수 누적합----')

        




