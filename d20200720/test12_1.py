print('-------연습1-------')
# 1부터 100까지 수중 3의 배수 5개만 출력
tot = 0
for i in range(1,101):# 라인수를 줄일 수 있는 방법
    if i%3 == 0:      # i%3 == 0 and tot <5
        tot+=1        # tot += 1
        print(i)      # print(i)
        if  tot == 5:
            break