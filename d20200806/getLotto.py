print('-------import-------')
print("이미 내장된 객체를 불러와서 사용하는 것") 
print('------- random -------')
import random
for i in range(10):
    print(random.random()) # 0~1 사이의 실수값
for j in range(15):
    print(random.randint(1,6),end=" ") # randint(1,100) 괄호안의 사이의 숫자
print()
print('-------------------------')
m = list(range(1,46)) # 리스트는 순서 ㅇ, 중복 ㅇ

print(m)
print('----------로또-----------')
# 랜덤하게 두개의 값을 출력
# m 리스트의 값을 1개만 랜덤하게 뽑아 출력하고자 한다.
for i in range(1000):
    a = random.randint(0,44)
    b = random.randint(0,44)
    m[a], m[b] = m[b], m[a] # 값 교환하기 <-이 부분이 섞어주기!!
for j in range(6):
    print(m[j], end="\t")
#print("m[",a,"] : ",m[a],"m[",b,"] : ",m[b])
# print("m[",a,"] : ",m[a],"m[",b,"] : ",m[b])

print()
print('-------로또 정렬 출력--------')
n = list(range(6))   # 1. 새로운 리스트 6
print(n)
for i in range(6):   # 2. 앞에서 6개의 새로운 리스트 담기
    n[i] = m[i]
print(n)
n.sort() # 3. 6칸 까지 리스트를 정렬
print(n) # 4. 순서대로 출력

print('-------대박 번호--------')
for i in range(6):
    print(n[i], end="\t")
    
print()
print('-------대박 번호: 여러번 돌리기--------')
cnt = int(input("몇번?: "))
for k in range(cnt):
    m = list(range(1,46)) 
    print('---------------------')
    for i in range(1000):
        a = random.randint(0,44)
        b = random.randint(0,44)
        m[a], m[b] = m[b], m[a] 
    for j in range(6):
        print(m[j], end="\t")
    print()
    n = list(range(6))   
    for i in range(6):   
        n[i] = m[i]
    n.sort()             
    for i in range(6):
        print(n[i], end="\t")
    print()