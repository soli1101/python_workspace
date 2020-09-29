print('---- #버블정렬 ----')
a=[3,0,1,8,7,2,5,4,6,9]
print(a)
print(len(a))
print('-------이중for문으로 표현--------')
for j in range(9,0,-1):         # 9~1까지 역순으로 j값에 입력
    for i in range(j):          # range(j)부분에 8~0까지 들어감
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
        print(a)
        print('------------------------')

