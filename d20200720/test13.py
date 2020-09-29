import turtle as t

t.shape('turtle')
t.color('#ff6600')
gap = 0
for i in range(4):
    gap +=10
    t.forward(100+gap)
    t.right(90)

t2 = t.Pen()              # 연필로 찍고 그리는 것(자국남음)
t2.shape('turtle')
t2.color('#ccff00')
t2.penup()
t2.goto(-200,100)
t2.pendown()
t2.begin_fill()
t2.circle(70)             # 반지름 25 원
t2.end_fill()

t3 = t.Pen()
t3.shape('turtle')
t3.color('#3300ff')
t3.penup()
t3.goto(100,200)
t3.pendown()
for j in range(5):
    t3.fd(100)
    t3.rt(72)

t4 = t.Pen()
t4.shape('turtle')
t4.color('#660000')
t4.penup()
t4.goto(-100,-200)
t4.pendown()
t4.circle(20,100)       # 반지름 20 각도 100도 만큼 그리기


t.mainloop()