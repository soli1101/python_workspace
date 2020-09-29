import turtle as t

m = int(input('몇각형?'))
t.shape('turtle')
t.color('#cc9900')
for i in range(m):
    t.forward(100)
    t.rt(360/m)
t.mainloop()