from random import randint
from turtle import *

a = Turtle()         # 거북이 a 생성
screen = Screen()    # 스크린 instance 생성
print(a)             # a를 출력하기
print(Screen)        # 스크린 출력하기

screen.addshape("audience.gif") # addshape:외부 이미지 가져오기
screen.addshape("turtle.gif")   # addshape:외부 이미지 가져오기
a.shape("audience.gif")         # a에 가져온 이미지 입혀주기
a.penup()                       
a.goto(0,220)        # turtle 그래픽은 화면의 정중앙이 (0, 0)

t1 = Turtle()        # 거북이 t1 생성
t1.color("#ffcc33")
t1.shape("turtle")
t1.penup()
t1.goto(-400,0)
t1.pendown()
t1.write("1번 꼬부기")

t2 = Turtle()        # 거북이 t2 생성
t2.color("#999966")
t2.shape("turtle")
t2.penup()
t2.goto(-400,-30)
t2.pendown()
t2.write("2번 꼬부기")

t3 = Turtle()        # 거북이 t3 생성
t3.color("#cc3333")
t3.shape("turtle")
t3.penup()
t3.goto(-400,-60)
t3.pendown()
t3.write("3번 꼬부기")

t4 = Turtle()        # 거북이 t4 생성
t4.color("#ff3300")
t4.shape("turtle")
t4.penup()
t4.goto(-400,-90)
t4.pendown()
t4.write("4번 꼬부기")

t5 = Turtle()        # 거북이 t5 생성
t5.color("#009966")
t5.shape("turtle")
t5.penup()
t5.goto(-400,-120)
t5.pendown()
t5.write("5번 꼬부기")

t6 = Turtle()        # 결승선 그릴 t6 생성
t6.color("#463e3f")
t6.penup()
t6.goto(-300,-150)
t6.speed(8)          # 스피드 조절
for j in range(9):   # 결승선 10번 연속해서 자동 긋기
    t6.pendown()
    t6.left(90)
    t6.forward(180)
    t6.backward(180)
    t6.rt(90)
    t6.penup()
    t6.fd(80)
             ## 응원할 꼬부기 입력받기 ##                    
n= textinput("골라:","1~5번 어떤 꼬부기를 고를거야?")
a.color("#800080")             # textinput에는 변수2가지 들어감
a.write(n+"번 꼬부기 이겨라!")  # a에 글쓰기

dis1 = 0             # 꼬부기의 거리를 누적할 기본 변수 선언
dis2 = 0 
dis3 = 0 
dis4 = 0 
dis5 = 0 

for i in range(250):        # 꼬부기 달리기 시키기!
    rnd1 = randint(1,5)     # 꼬부기 랜덤한 값으로 전진시키기!
    rnd2 = randint(1,5)
    rnd3 = randint(1,5)
    rnd4 = randint(1,5)
    rnd5 = randint(1,5)
    dis1 += rnd1            # 꼬부기 이동거리 누적하기!
    dis2 += rnd2
    dis3 += rnd3
    dis4 += rnd4
    dis5 += rnd5
    
    t1.fd(rnd1)             # 꼬부기 랜덤값 rnd 불러와 전진시키기!
    t2.fd(rnd2)
    t3.fd(rnd3)
    t4.fd(rnd4)
    t5.fd(rnd5)
                ## 1등 꼬부기 찾기!! ##
    if dis1>=700:       # 꼬부기의 누적이동거리가 700 이상이면
        t1.penup()      # 아래 코드블럭 적용하기
        t1.goto(0,100)
        t1.pendown()
        t1.shape("turtle.gif")
        break
    
    elif dis2>=700:
        t2.penup()
        t2.goto(0,100)
        t2.pendown()
        t2.shape("turtle.gif")
        break
    
    elif dis3>=700:
        t3.penup()
        t3.goto(0,100)
        t3.pendown()
        t3.shape("turtle.gif")
        break
    
    elif dis4>=700:
        t4.penup()
        t4.goto(0,100)
        t4.pendown()
        t4.shape("turtle.gif")
        break
    
    elif dis5>=700:
        t5.penup()
        t5.goto(0,100)
        t5.pendown()
        t5.shape("turtle.gif")
        break
    
t1.write(dis1)  # 꼬부기의 최종 이동거리 표시하기
t2.write(dis2)
t3.write(dis3)
t4.write(dis4)
t5.write(dis5)

mainloop()      # 코드 실행후에도 창 계속 띄워놓기