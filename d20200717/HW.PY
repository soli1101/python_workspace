print('---HW1 1부터 100까지 출력---')
for i in range(1,101):      # 1~100까지 순차적으로 i에 대입해
    print(i, end=", ")      # i를 출력해 끝은 공백으로 연결해
print()
print('---HW2 ---')         # 11111,22222,33333,44444,55555
for j in range(1,6):        # j변수에 1~5까지 순차적으로 대입해
    print()                 # 한 줄 띄기 실행해
    for i in range(1,6):    # i에 1~5까지 순차적으로 대입해
        print(j, end="")    # j값을 출력해
print()         
print('---HW3 ---')         # 99999, 88888, 77777, 66666, 55555
for j in range(9,4,-1):     # 4~9까지 역순으로 j에 대입해
    print()                 # 한 줄 띄기 실행해
    for i in range(1,6):    # i에 1~5까지 순차적으로 대입해
        print(j, end="")    # j를 출력하고 끝은 공백으로 연결해
print()
print('---HW4 ---')         # 1234, 5678
for j in range(2):          # j에 0,1을 순서대로 대입해
    a = range(1,5)          # a변수에는 1,2,3,4 값을 대입해
    b = range(5,9)          # b변수에는 5,6,7,8 값을 대입해
    if j == 0 :             # 만약 j 값이 0이랑 같으면:
        for i in a:         # 반복해 i는 a를 순차적으로 가져와서
            print(i, end="")# 출력해 i를 
    else:                   # 그 외의 경우에는 
        for i in b:         # i에 b의 index를 순차적으로 가져와
            print(i, end="")# 공백으로 연결하면서 i를 출력해
    print()
print()    
print('---HW5 ---')
for i in range(1,10):             # i에 1~9값을 대입해
    print("8 x ",str(i),"=",str(i*8)) 
print()    
print('---HW6 2단 부터 9단까지 출력 ---') # 2단~9단까지 출력해
for j in range(2,10):             # j에 2~9값을 대입해
    print('-----------',j,"단")   # 구분선과, 'j단'을 입력해
    for i in range(1,10):         # i에 1~9값을 대입해
        print(j," x ", i, "=",j*i)# jxi=값을 출력해
print()    
print('---HW7 구구단3단 출력 ---')
for i in range(1,10):                 # i에 1~9값을 대입해서 
    print("3 x ",str(i),"=",str(i*3)) # 3x문자i=값을 출력해
print()            

print('---HW8 1 11 111 1111 11111---')
for k in range(1,6):        # k에 1~5를 순차적으로 대입해
    for i in range(k):      # i를 k번 실행해
        print(1, end="")    # 1을 공백으로 연결해서 출력해 
    print()                 

print('---HW9 1부터 100합계를 출력---')
cum = 0
for i in range(1,101):
    cum += i
    print(cum)
print()
print('---HW11 * ** *** **** *****---')
for k in range(1,6):            # k값은 변수 인데 그것은 1~6까지 순차적으로 들어가
    for i in range(k):          # range(k)니까 k번 만큼 반복해
        print('*', end="")
    print()
print()
print('---HW11teacher---')
for i in range(1,6):
    print('*'*i)
print()
print('---HW12 1 12 123 1234 12345---')
for k in range(1,6):            # k값은 변수 인데 그것은 1~6까지 순차적으로 들어가
    for i in range(k):          # range(k)니까 k번 만큼 반복해
        print(i+1, end="")      # i+1을 출력하고 끝은 공백으로 연결해
    print()
print('---HW12teacher---')
msg = ""
for i in range(1,6):
    msg = msg +str(i)
    print(msg)
print()
print('---HW13 2단 부터 9단까지 출력 가로로 ---')
for j in range(2,10):
    print('-----------',j,"단")
    for i in range(1,10):
        print(j," x ", i, "=",j*i, end=" ")
print()    
print('---HW14 ***** **** *** ** *---')
for i in range(5,0,-1): #5에서 1까지 역순으로 숫자 생성
    print('*'*i)        #"*"에 i를 곱해서 출력해
print()
print('---HW15 time converter---')
time=int(input("시간입력"))
print(time)
# 1분 --> 60초 
# 1시간 --> 60 x 60초 = 3600초
# 1일 --> 60*60*24 = 86400초
day = time/(60*60*24)  #90061/86400 -->1
hour = time%(60*60*24)/(60*60) # 3661/3600 -->1
minute = time/(60*60*24)%(60*60) # 61/60 -->1
second = time%60 

print('%d일 %d시간 %d분 %d초'%(day,hour,minute,second))

print('---HW16 잔돈교환기(큰화폐순으로)---')
money = int(input("돈값을 입력해"))
_5man = money//50000
_1man = (money%50000)//10000
_5chon = ((money%50000)%10000)//5000
_1chon = (((money%50000)%10000)%5000)//1000
_500won = ((((money%50000)%10000)%5000)%1000)//500
_100won = (((((money%50000)%10000)%5000)%1000)%500)//100
_50won = ((((((money%50000)%10000)%5000)%1000)%500)%100)//50
_10won = (((((((money%50000)%10000)%5000)%1000)%500)%100)%50)//10
_1won = int(((((((((money%50000)%10000)%5000)%1000)%500)%100)%50)%10)/1)
print("50000권:",_5man,"매")
print("10000권:",_1man,"매")
print("5000권:",_5chon,"매")
print("1000권:",_1chon,"매")
print("500원:",_500won,"개")
print("100권:",_100won,"개")
print("50원:",_50won,"개")
print("10원:",_10won,"개")
print("1원:",_1won,"개")

