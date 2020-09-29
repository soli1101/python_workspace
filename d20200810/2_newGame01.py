# [1] 게임의 기본틀 
import pygame
pygame.init()
screen_width=600
screen_height=900
screen = pygame.display.set_mode((screen_width,screen_height))
isRunning = True
pygame.display.set_caption("우주 전쟁")
    # 여기 사이에 코드가 반복
while isRunning:            # isRunning이 True라면:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
    pygame.display.update() # 창이 뜨면 무한반복

pygame.display.update()
pygame.quit()