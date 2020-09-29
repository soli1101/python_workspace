print('---HW1: 두 주사위의 합이 4가 되는 모든 경우의 수---')

for i in range(1,7):
    for j in range(1,7):
        if i+j == 4:
            print("("+str(i)+","+str(j)+")")
print()
print('---HW2: 윤년인지 출력하는 프로그램 ---')

i = int(input("년도를 입력하시오"))
if i % 4 == 0 and i%100 or i%400==0 :
        print(i, "는 윤년")

print('---HW3: 다음 함수를 출력하는 코드 ---')
print('# print(hap(100,200))')
print('# print(minus(200,100)')
print('# print(multi(200,3))')
print('# print(div(200,3))')
print('-----<1번>-----')
def hap(num,num2):
    value = num + num2
    return value
print(hap(100,200))
print('-----<2번>-----')
def minus(num,num2):
    value = num - num2
    return value
print(minus(200,100))
print('-----<3번>-----')
def multi(num,num2):
    value = num * num2
    return value
print(multi(200,3))
print('-----<4번>-----')
def div(num,num2):
    value = num // num2
    return value
print(div(200,3))
print()
print('---HW4: 두 행렬에 대한 덧셈을 구하세요 리스트 사용 ---')
a=[]
a.append([3,2,3])
a.append([4,5,6])
a.append([1,4,9])

b=[]
b.append([1,8,7])
b.append([6,4,4])
b.append([3,2,3])

print(a[0][0]+b[0][0], a[0][1]+b[0][1], a[0][2]+b[0][2])
print(a[1][0]+b[1][0], a[1][1]+b[1][1], a[1][2]+b[1][2])
print(a[2][0]+b[2][0], a[2][1]+b[2][1], a[2][2]+b[2][2])
print()

print('---HW5: 5행 5열 리스트를 만들고 반복문 사용 값 할당 화면에 출력---')
c=[]
for j in range(1,22,5):
    for i in range(1,2):
        c.append([j,j+1,j+2,j+3,j+4])
print(c)
print()
print('---HW6: 10명의 성적 입력받고 총점과 평균을 화면에 출력---')
data = input("성적을 입력하시오: ").split() # 성적 입력받기
print(data)

for i in range(10):              # 리스트의 요소값 정수로 바꿔주기
    data[i]=int(data[i])

sum = 0                          # 데이터의 누적값 구하기
for i in data:
    sum += i
print("총점:",sum,"평균:",sum//10)# 결과 출력
print()
print('---HW7: 길이가 100개인 정수리스트에 1~100의 값 대입---')
list = []
for i in range(1,101):
    list.append(i)
    list[i-1]=int(list[i-1]) # 리스트의 값 정수로 변환
print(list)
print()

print('---HW8: 7번에 3의 배수는 3333, 5의 배수는 5555, 3과 5의 공배수는 3535를 대입하시오--')
for j in range(100):    
    if list[j]%3==0 and list[j]%5==0:
        list[j]='3535'
    elif list[j]%3==0:
        list[j]='3333'
    elif list[j]%3==0:
        list[j]='5555'
print(list)
print()
print('---HW9:정수 10개를 입력받아 리스트에 저장하고')
print('리스트에 있는 정수 중에서 3의 배수만 출력해보자.---')

num = input("정수 10개를 입력하세요: ").split()
for i in range(len(num)):       # 입력받은 값 정수로 바꿔주기
    num[i]=int(num[i])
    if num[i]%3==0:
        print(num[i])




