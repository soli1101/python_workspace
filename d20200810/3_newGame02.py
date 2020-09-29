# 게임의 기본틀 
import pygame
pygame.init()
screen_width=600
screen_height=900
screen = pygame.display.set_mode((screen_width,screen_height))
isRunning = True
pygame.display.set_caption("우주 전쟁")

# 배경 그리기
bg1 = pygame.image.load("e:/dev/python_workspace/img/space.jpg")
bg2 = pygame.image.load("e:/dev/python_workspace/img/space.jpg")
bg1 = pygame.transform.scale(bg1,(600,900))
bg2 = pygame.transform.scale(bg2,(600,900))

# 캐릭터 우주선 그리기
player1 = pygame.image.load("e:/dev/python_workspace/img/player1.png")
player2 = pygame.image.load("e:/dev/python_workspace/img/player2.png")
player3 = pygame.image.load("e:/dev/python_workspace/img/player3.png")
player4 = pygame.image.load("e:/dev/python_workspace/img/player4.png")

# 우주선 움직이는 것 처럼 만들기
cnt = 0

# 배경 움직이게 만들기 :y좌표 변수
bg1Y = 0
bg2Y = -900



while isRunning:            # isRunning이 True라면:
    # 캐릭터 우주선 움직이게 만들기
    cnt +=1
    
    # 배경 움직이게 만들기 :y좌표 점점 내려가게 하기 
    bg1Y +=1
    bg2Y +=1
    screen.blit(bg1,(0,bg1Y))
    screen.blit(bg2,(0,bg2Y))
    if bg1Y > 900:
      bg1Y = -900
      bg2Y = 0
    if bg2Y > 900:
      bg2Y = -900
      bg1Y = 0
    



    # 계속 화면이 출력되도록 하기
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

    
    # 캐릭터 우주선 움직이게 만들기
    if cnt % 4 == 0 :
      screen.blit(player1,(250,800))
    elif cnt % 4 == 1:
      screen.blit(player2,(250,800))
    elif cnt % 4 == 2:
      screen.blit(player3,(250,800))
    elif cnt % 4 == 3:
      screen.blit(player4,(250,800))









    pygame.display.update() # 창이 뜨면 무한반복

pygame.display.update()
pygame.quit()