print('------- while 무한반복 -------')
while True: # 무한반복
    value = int(input("숫자를 입력:"))
    #5의 배수인가요?
    if value%5 == 0 :
        print(str(value)+ "는 5의 배수입니다.")
        break
    else:
        print(str(value)+ "는 5의 배수가 아닙니다.")
print("이제 그만~~~")