# 튜플 (tuple)  : a.k.a. 읽기 전용 배열
# list와 비슷하지만 한 번 생성되면 값을 변경 할 수 없다.
# 불변한 순서가 있는 객체의 집합
a = (10, 20 , 30 , 40 , 50) #a에 괄호 안 값을 목록으로 입력해

print(a[0])                 #a리스트의 0번째 값을 출력해

b = tuple(range(5,10))      #b변수에 5부터 10 범위 안에 있는 불변리스트를 대입해

print(b[2])                 #b리스트의 2번째 값을 출력해
# b[2]=100                  #튜플은 값의 수정이 되지 않는다

print(len(b))               #len()은 b안에 있는 객체의 갯수를 가져온다 출력해

# 제어문

# 문장의 흐름을 제어해주는 명령

# for 변수 in iterable
#     반복할 명령
print('test......................')
# a <= (10,20,30,40,50)
for i in a:             
    print(i)
print('test......................')


# 연습: 1부터 20까지 화면에 출력

# 1. 프린트 문으로 출력
print(list(range(1,21,1))) 

# 2. for문
k = list(range(1,101))
for j in k:
    print(j) 
print('-----------------------------')
# 연습2 반복문을 사용해서 구구단 3단 출력
c = list(range(1,10))
for su in c:
    print ("3 x " + str(su) + "=" + str(3*su))

# 연습3 1부터 10까지 누적합을 출력

# 1. 1부터 10까지 값을 화면에 출력한다.
# print(1); print(2); print(3); print(4); print(5);
# print(6); print(7); print(8); print(9); print(10);
#반복문으로 변경
for i in range(1,11):            
    print(i)
# 2. 누적합을 담을 변수를 선언한다.
sum = 0                 #숫자값을 담을 그릇(변수) sum을 생성한다
for i in range(1,11):   #in 다음에 있는 range안의 값들을 순차적으로
                        #i에 대입시켜서 아래 명령을 실행시켜         
    sum = sum + i;      #sum에 sum+i의 값을 대입해
    print("sum:",sum,"i:",i) #출력해 sum값과 i값을

# 3. 출력하기전에 변수에 현재 진행값을 담는다.
# 4. 누적값을 출력한다.

print('---------------------------')
# 연습5 1부터 입력받은 값 까지의 누적합
# m = 0
# goal = int(input("어디까지 누적할거니"))
# for s in range(1, goal+1):
#     m = m + s
#     print("m:",m,"s:",s)
# print("1부터",goal,"까지 누적합:", m)


########################################
