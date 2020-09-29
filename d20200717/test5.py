print('------for와while-------')

a=1

while a != 5:               # while 다음에 조건이 온다 
    print(a)                # code block을 수행한다
    a += 1                  # a를 1씩 증가시킨다

# for i in 컬렉션:
#     처리할문장
#     처리할문장

# while 조건:
#     처리할문장
#     처리할문장
#     조건을 변경할 문장
# print('----------무한반복----------')
# k=1
# while True:
#     k +=1
#     print("무한반복", k)
print('-------------------------')
for i in range(5):                # i를 5번 돌려
    for j in range(3):
        print("i:",i,"j:",j)
print('---#연습4 구구단 출력---')
for m in range(9):                  # m을 9번 돌려
    print('------------', m+1)      # m+1과 구분선을 출력해
    for i in range(1,10):           # i를 1번 부터 9까지 돌려
        print(str(m+1) + " x " + str(i) + " = " + str((m+1)*i))
print('---#연습5 수 누적 출력---')
#11111
#22222
#33333
#44444
for j in range(1,6):
    for i in range(1,6):
        print(j, end="")
    print()