import pygame
import math
import random

#시작
pygame.init()
screen = pygame.display.set_mode((600,900))
isRunning = True
pygame.display.set_caption("우주 전쟁")

#배경
bg1 = pygame.image.load("e:/dev/python_workspace/img/space.jpg")
bg2 = pygame.image.load("e:/dev/python_workspace/img/space.jpg")
bg1 = pygame.transform.scale(bg1,(600,900))
bg2 = pygame.transform.scale(bg2,(600,900))

#우주선
player1 = pygame.image.load("e:/dev/python_workspace/img/player1.png")
player2 = pygame.image.load("e:/dev/python_workspace/img/player2.png")
player3 = pygame.image.load("e:/dev/python_workspace/img/player3.png")
player4 = pygame.image.load("e:/dev/python_workspace/img/player4.png")



while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
    
    #배경 움직이게 하기
    screen.blit(bg1,(0,bg1Y))
    screen.blit(bg2,(0,bg2Y))

    screen.blit(player1,(300,550))
    screen.blit(player2,(300,550))
    screen.blit(player3,(300,550))
    screen.blit(player4,(300,550))
    
    
    pygame.display.update()


pygame.quit()