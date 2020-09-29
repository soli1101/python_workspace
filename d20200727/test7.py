print('----# 현재 작업중인 디렉토리 경로 얻어오기----')
import os
print(os.getcwd())  # 현재 작업디렉토리를 볼 수 있다

print('----# 파일 입출력 ----')  

# open("파일명","모드")

file = open("./d20200727/hello.txt", "r")   #1. 연다
print(file)                                 #2. 출력(파일속성보여줌)
print(file.read(), type(file.read()))       #3. 파일을 읽어들인다
file.close()                                #4. 파일 닫기!

# ***** 닫지 않으면, 다른 데서 사용할 수 없어서 오류가 난다!
# 또는 좀비 프로세스가 된다!! *****
print()

print('----# 파일 생성! 입력하기!! ----')

file2=open("./d20200727/hello2.txt",'w')  # mode='w'는 write!
print(file2)                              # 실행하면 파일 생성
file2.write("금요일 같은 월요일... 월요병") # 파일에 내용 입력
file.close                                # 파일 닫기!!

