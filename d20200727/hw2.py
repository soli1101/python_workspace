import os
print('----hw15.비의 깡 가사를 rain.txt 파일에 저장하세요 ----')
file = open('./d20200727/rain.txt','r',encoding='utf-8')
print()

print('----hw16.rain.txt 에서 4글자 단어는 모두 몇개인가?----')
n=file.read().split()
print(len([word for word in n if len(word)==4]))
print()

print('----hw17.사용자가 입력한 디렉토리의 파일과 디렉토리 목록을 dir.txt 파일에 저장하세요----')
# userinput = input("디렉토리를 입력하세요:")
# print(os.listdir(userinput))
# with open('./d20200727/dir.txt','w',encoding='utf-8') as file:
#     file.writerow(os.listdir(userinput))
# print()

print('----hw18.로또번호를 생성해서 lotto.txt 파일에 한줄씩 저장하세요----')
''' 
3
15
28
33
25
16
45
'''
import random

b = []
d = str(random.randint(1,46))
for i in range(6):
    d = str(random.randint(1,46))
    b.append(d+'\n')
print(b)

file=open("./lotto.txt","w",encoding="utf-8",newline='\r')
file.writelines(b)

print()

print('----hw19.랜덤하게 소문자 3자를 생성해서  randomchar.txt 파일에 저장하세요----')
import random
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
pick=random.sample(alphabet,3)
print(pick)
with open("./randomchar.txt",'w',encoding='utf-8') as file:
    file.write(pick[0])
    file.write(pick[1])
    file.write(pick[2])

print()
print('----hw20.다음 내용을 stock.csv 로 저장하세요!----')
'''
종목번호  회사명   현재주가 
035720  카카오   326500
005930  삼성전자  55600
047820  초록뱀     1590 
'''
import csv
file = open('./stock.csv','w',encoding="utf-8")
wr = csv.writer(file)
wr.writerow([1,'종목번호','회사명','현재주가'])
wr.writerow([2,'035720','카카오','326500'])
wr.writerow([3,'005930','삼성전자','55600'])
wr.writerow([4,'047820','초록뱀','1590'])