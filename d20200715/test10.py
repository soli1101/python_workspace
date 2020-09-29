# csv 파일 ??
#a, b, c = input("숫자 3개를 콤마로 구분해서 입력하세요 : ").split(",") #split() 괄호 안에 ","를 써주면 그걸로 글자를 구분할 수 있다
#print("a:",a,"b:",b,"c:",c)
#print(a)
#print(b)
#print(c)

print(100,200,300, sep=", ")                              #sep을 사용해서 옆으로 출력가능
print("hello","python","world", sep="\n")                 #출력해(이거,이거,이거를 분리해 \n(엔터)로 구분해서)
#특수문자 제어문자 : \n  \t
print("아\n날씨가 \n좋다. \n \t \t \t 놀러\t가야지...ㅠㅠ") #출력해(이거(엔터)이거(엔터) 이런식으로...)
print("오늘은", end="\t")                                 #오늘은 \n가 아니라 end 끝에 탭해
print("수요일", end=", ")                                 #이 출력의 끝을 ,ㄹ 구분해 
print("내일은", end="\t")
print("목요일")

# year, month, day, hour, minute, second 변수를 선언하고
# 값을 대입한 후에
# 아래와 같은 출력을 얻도록 코드를 작성해 보세요

# 1
#-- 오늘은 2020/07/15 18:00:00 입니다.
year = 2020                             # year 에 2020을 대입한다
month = 7                               # month 에 7을 대입한다
day = 15                                # day 에 15를 대입한다
hour = 18                               # hour에 18을 대입한다
minute = "00"                           # minute에 '00'을 대입한다
second = "00"                           # second에 '00'을 대입한다
print("오늘은"+str(year)+"/"+str(month)+"/"+str(day)+"입니다")
#출력한다(오늘은+문자로변환(year)+/+문자로변환(month)+/+문자로변환(day) )
#2
# 2020/7/15 18:00:00
print(year, month, day, sep="/", end=" ") #변수 year,month, day를 출력하되 /로 구분하고 끝에는 엔터대신 공백을 넣어라
print(hour, minute, second, sep=":") #변수 hour, minute, second를 출력하되 :으로 구분하라