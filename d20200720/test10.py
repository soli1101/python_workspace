
m =      [ ]
m.append([100,200]) 
m.append([300,400,  500,600,700])
m.append([900,1000,1100])

print(m)
#print(m[행][열])
print(len(m[0]))
print(len(m[1]))
print(len(m[2]))
print('--------# 모든 행 출력---------')
for i in range(3):
    for j in range(len(m[i])):
        print(m[i][j], end=" ")
        
print()
print('-------연습1-------')
# 다음 리스트 만들고 for 문으로 출력하기
n = []
n.append([100, 50, 30, 20])
n.append([200, 100, 1])
n.append([900, 1000, 20, 20, 30, 50])
n.append([50, 70, 90])
print(n)
print(len(n))
for i in range(4):
    for j in range(len(n[i])):
        print(n[i][j], i,"행", j,"열")