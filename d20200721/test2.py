from turtle import *  # 그냥 turtle 에 있는 걸 다 가져올 거야 

name = textinput("이름", "당신의 이름을 입력하세요.") # 첫번째는 타이틀, 두번째는 팝업창 내용
print(name)
shape('turtle')
color('pink')

lt(90)

# 몇개의 명령들을 모아서 이름을 부여해 놓은 것 : 함수
# 자주 사용하는 명령기능에 이름을 부여한 것 

# def 이름():
#     처리할 문장

def w():
    fd(50)

def d():
    rt(90)
    fd(50)

def a():
    lt(90)
    fd(50)

def s():
    lt(180)
    fd(50)

onkey(w,'w') # 함수와 키 연결 키보드의 w키를 누르면 w 함수를 실행함
onkey(d,'d') 
onkey(a,'a') 
onkey(s,'s') 

listen()     # 내가 입력하는 지 여부를 들을 수 있다

mainloop()