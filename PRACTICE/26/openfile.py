

file=open("./d20200727/hello.txt","r")
print(file)
print(file.read(),type(file.read()))
file.close()

# 파일 생성하기

file2=open("./d20200727/hello3.txt","w")
print(file2)
file2.write("금요일 같은 월요일,, 월요병!")

file=open("./d20200727/hello3.txt",w)
print(file2)