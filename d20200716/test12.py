#문자열

name = 'my name is "KS"' #''도 문자 ""도 문자로 인식한다

print(name)              #name이라는 변수를 출력해

sorry = "I am sorry"     #sorry라는 변수의 값에 ""문자열의 내용을 대입해
 
print(sorry)             #sorry라는 변수를 출력해

hobby = "cyber \nfishing"#hobby에 cyber (엔터키) fishing 문자열 값을 입력해
print(hobby)             #hobby변수를 출력해
print('------------------------')
# 5개의 정수형 변수에 10 20 30 40 50 값을 대입
a,b,c,d,e=(10,20,30,40,50)
#출력
print("a:",a,"b:",b,"c:",c,"d:",d,"e:",e)

#리스트
#목록 : [] 대괄호로 묶어 준다. 각각의 값을 Element
#Element의 구분은 ,로 한다.
a = [10, 20, 30, 40, 50]
print(a[0])
#40을 출력
print(a[3])

print('--------------------')

# 빈 리스트 작성
m = []                # 평소에는 비워 뒀다가 나중에 필요한 값을 추가해서 사용
# 연속된 값 만들기
print(range(10))      # 0 부터 10 '미만'의 범위를 갖는 녀석
m = list(range(0,10)) # m이라는 변수에 목록 (값이 0부터 10미만인)을 대입해
print(m)              # m변수를 출력해

# 10부터 19까지 10개의 연속된 숫자로 된 k list를 만들고 화면에 출력
k = list(range(10,20,2))
print(k)

# 1부터 1000 사이의 3의 배수를 목록으로 출력
print(list(range(3,1001,3))) #3~1001사이의 범위의 숫자중 3씩 증가하는 리스트를 만들어서 출력해

# range (시작값, 종료값, 증가폭)
print(list(range(3, 1001, 3))) 

# 달의 표면온도 밤 : -170도 / 낮 120도 , 3도씩 상승 한다고 가정 했을때 
# 온도의 변화를 리스트로 만들어 출력
print(list(range(-170, 121, 3)))

print(m)
print("m[3]:", m[3]) #m 목록의 3번째 값을 출력해

m[3] = 200           #m 목록의 3번째 값에 200을 대입해
print("m[3]:",m[3])  #m 목록의 3번째 값을 출력해

# 각각의 요소에 값을 추가, 변경, 삭제 