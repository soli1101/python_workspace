print('------- ord -------')
# 사용자로 부터 글자를 입력받아
# 이 문자가 대문자인지 소문자인지 판단

# 1. 사용자에게 입력값을 받아오고
# 2. 이 값의 ASCII 코드 값을 구한다.
# 3. A = 65,  a = 97
#    B = 66,  b = 98
# 4. 65 ~ 90, 97~122  범위에 있을 것
# 5. 출력

data = input("영문을 입력해: ")
print("입력값: ",data)
print("ASCII코드값:", ord(data))
if 65<=ord(data)<=90:
    print("최종출력: ", ord(data),"대문자")
elif 97<=ord(data)<=122:
    print("최종출력: ", ord(data),"소문자") 


