print('------- 대소문자변환 -------')
msg = "HELLO"

# 1. 각 문자의 아스키 코드값을 구한다.
# 2. 대문자의 범뷔: 65~90 이라면 이것을 대문자로 바꾼다,
# 3. 소문자의 범위: 97~122 
# 4. 대문자와 소문자의 관계는 +-32

# print(len(msg))           # msg의 글자 갯수를 알 수 있다
for i in range(len(msg)): # msg 안의 글자의 갯수만큼 돌린다
                          # print(msg[i],end=" ") 출력확인
    code = ord(msg[i])    # msg 글자의 ASCII 코드값을 가져옴
    if 65<=code<=90:      
        print(chr(code+32), end="")  # chr숫자를 문자로 
print()
print('----입력받은 값 대소문자변환----')
m = input("Input text :")
for j in range(len(m)):
    a = ord(m[j])
    # print(a, end="\t")      # m 문자의 아스키 코드 값
    if 65<=a<=90:
        print(chr(a+32), end="")  # 대문자를 소문자로 
    elif 97<=a<=122:
        print(chr(a-32), end="")  # 소문자를 대문자로   