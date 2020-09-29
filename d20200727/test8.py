print('----with open ----')
# with open("파일명", "모드") as 파일객체:
#      코드
# open과 동시에 close하는 기능

# with open("./d20200727/msg.txt","w") as file: 
#     file.write("오늘은 여기까지... \n")


file3=open("./d20200727/msg.txt","r")
n=file3.read().split()
print(n)
print()

print('----특정단어가 몇번 나오는지 카운트하기----')
f=[word for word in n if word.find('해지')>=0]
print(f)
print(len(f))









file3.close()