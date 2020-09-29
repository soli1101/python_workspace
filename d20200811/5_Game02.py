import pygame
import random

# [0] 기본설정
pygame.init()

screen_width=1200
scree_height=800
screen=pygame.display.set_mode((screen_width,scree_height))
pygame.display.set_caption("핑퐁")

# [4-1] ball의 방향변환 함수
def changeDirection(x,y,ix,iy):
    # 화면 위쪽 벽에 맞으면 튕겨나가게 설정
    if y<=3 or y>=770:
        iy = -iy
    if x<=3 or x>=1170:
        ix = -ix
    return ix, iy

# [3-1] 시계 변수
clock = pygame.time.Clock()

# [2-1] ball 움직임 주기
''' bx,by를 변수로 주고 그 값을 random값으로 준다'''
bx = 580
by = 300
inc_x = random.randint(-10,10)
inc_y = random.randint(-10,10)

# [1-1] 배경&ball이미지 설정
bg = pygame.image.load("e:/dev/python_workspace/img/window.jpg")
bg = pygame.transform.scale(bg, (1200,800))
ball = pygame.image.load("e:/dev/python_workspace/img/lotto/ball8.png")

# [0] 기본설정 
isRunning = True
while isRunning:

    # [4-2] ball의 방향변환 함수
    inc_x,inc_y = changeDirection(bx,by,inc_x,inc_y)

    # [3] fps
    fps = clock.tick(80)

    # [2-2] ball 움직임 주기
    bx -= inc_x   # inc는 대각선으로 간다!
    by -= inc_y

    # [0] 기본설정 : 종료 설정
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

    # [1-2] 이미지 화면에 찍기
    screen.blit(bg,(0,0))
    screen.blit(ball,(bx,by))

    pygame.display.update()   # 화면 갱신해

pygame.quit()