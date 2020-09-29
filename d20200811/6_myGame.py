import math
import random
import pygame

pygame.init()

# [1] 화면 설정 및 배경 생성
screen_width=1200
screen_height=800
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("핑퐁응용 - 배구")

bg = pygame.image.load("e:/dev/python_workspace/img/milkyway.jpeg")
by = pygame.transform.scale(bg,(1200,800))

# [2] 공 생성
ball = pygame.image.load("e:/dev/python_workspace/img/whiteball.png")
ball = pygame.transform.scale(ball,(50,50))

# [3] 화면 오른쪽 바 생성
bar = pygame.image.load("e:/dev/python_workspace/img/verticalbar.png")
bar = pygame.transform.scale(bar,(10,180))

# [3-1] 화면 오른쪽 바 위아래로 움직임 주기
''' bar의 기본값'''
barx = 1150
bary = 0
''' bary의 증가값 변수로 주기'''
inc_bar_y = 2
''' bary의 증가값의 방향을 바꿔주는 함수 '''
def barChangeDirection(y,by):
    if y<=0 or y>=620:
        by = -by
    return by

# [4] 화면 왼쪽 바 생성
bar2 = pygame.transform.scale(bar,(10,100))
bar2x = 50
bar2y = 400

# [4-1] 화면 왼쪽 바 마우스 움직임으로 조작가능하게 하기

# [5] 공이 화면 안에서 대각선으로 움직이게 하기
ballx = 60
bally = 400
inc_x = random.randint(-4,4)
inc_y = random.randint(-4,4)

def ballChangeDirection(x,y,ix,iy):
    if y<0 or y>750:
        iy = -iy
    if x<0 or x>1150:
        ix = -ix
    return ix, iy

# [6] 공이 bar 충돌시 방향 반대로 바꾸게 하기
'''1 공과 bar 사이의 거리 구하기 '''
def pythagoras(x1,y1,x2,y2):
    return math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))

'''2 공과 왼쪽 bar 사이의 거리가 1이하면 반대로 바꾸게 하기'''
ballList =[]
barList =[]

def collision(blx,bly,brx,bry):
    global inc_x
    dis = pythagoras(blx, bly, brx+5, bry+50)
    print(dis, blx, bly, brx+5, bry+50 )
    if dis <= 200:
        print(dis)
        inc_x = -inc_x        
        

# [0] 화면이 돌아가는 동안 출력되는 변수들 
isRunning=True
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

    # [5] 공이 화면 안에서 대각선으로 움직이게 하기
    ballx -= inc_x    
    bally -= inc_y 
    inc_x, inc_y = ballChangeDirection(ballx,bally,inc_x,inc_y)
    
    # [1] 배경 화면에 찍기
    screen.blit(bg,(0,0))

    # [2] 공 화면에 찍기
    screen.blit(ball,(ballx,bally))

    # [3] bar 화면에 찍기
    screen.blit(bar,(barx,bary))
    
    # [3-1] 화면 오른쪽 바 위아래로 움직임 주기
    bary += inc_bar_y     # bary가 inc_y값 만큼 움직임
    inc_bar_y = barChangeDirection(bary,inc_bar_y) # inc_y값은 방향바꿈함수 안의 조언에 따라 움직임

    # [4] 화면 왼쪽 바 생성
    screen.blit(bar2,(bar2x,bar2y))

    # [4-1] 화면 왼쪽 바 마우스 움직임으로 조작가능하게 하기
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]==1:
        if 1 <= bar2y <=800:
            bar2y -= 4
    if keys[pygame.K_DOWN]==1:
        if 0 <= bar2y < 700:
            bar2y += 4

    # [6] 공과 왼쪽 bar 위치 누적 List만들기 / 충돌 함수 호출
    ballList.append([ballx,bally])
    barList.append([bar2x,bar2y])
    collision(barList[-1][0], barList[-1][0], ballList[-1][0], ballList[-1][1])


    # [0] 화면 업데이트
    pygame.display.update()

pygame.quit()