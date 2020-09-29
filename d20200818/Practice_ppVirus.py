from pygame import *
import random

init()

screen_width = 1200
screen_height = 800
screen = display.set_mode((screen_width,screen_height))
display.set_caption("ping-pong virus")

bg = image.load("e:/dev/python_workspace/img/bg.jpg")
bg = transform.scale(bg,(1200,800))

ball = image.load("e:/dev/python_workspace/img/lotto/ball7.png")
bx = 580
by =700

inc_x = random.randint(-10,50)
inc_y = random.randint(-10,50)

def changeDirection(x,y,ix,iy):
    if y<=3 or y>=770:
        iy = -iy
    if x<=3 or x>=1170:
        ix = -ix
    return ix, iy

isRunning = True
while isRunning:

    bx -= inc_x
    by -= inc_y    

    inc_x, inc_y = changeDirection(bx,by,inc_x,inc_y)

    screen.blit(bg,(0,0))
    screen.blit(ball,(bx,by))

    for e in event.get():
        if e.type == QUIT:
            isRunning = False

    display.update()


quit()