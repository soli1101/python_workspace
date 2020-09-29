print('------- while 무한반복 -------')
while True: # 무한반복
    value = int(input("숫자를 입력:"))
    #5의 배수인가요?
    if value%5 == 0 :
        continue                 # 아래 처리할 문장이 있어도
                                 # 다음으로 넘어감
    else:
        print(str(value)+ "는 5의 배수가 아닙니다.")
print("이제 그만~~~")
print()
