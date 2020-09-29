import pygame

pygame.init()      # 항상 초기화 해야함

# 게임 화면 설정 #
'''(1) 화면크기'''
screen_width = 1200         
screen_height = 800
screen = pygame.display.set_mode((screen_width,screen_height))

'''(2) Title '''
pygame.display.set_caption("토끼 사냥")

'''(3) 배경 담기'''
bg = pygame.image.load('e:/dev/python_workspace/img/bg.jpg')
isRunning = True    # 게임을 계속 진행할지, 중지할지를 결정하는 변수

'''(4) 토끼 담기'''
rabbit1 = pygame.image.load('e:/dev/python_workspace/img/rabbit1.png')
rabbit2 = pygame.image.load('e:/dev/python_workspace/img/rabbit2.png')
# 사이즈조절 transform.scale(객체, (너비,높이))
rabbit1 = pygame.transform.scale(rabbit1,(100,130))
rabbit2 = pygame.transform.scale(rabbit2,(100,130))

'''(5) 움직이는 것 처럼 보이게 만들기 '''
cnt = 0     # 움직임 세는용
count = 0   # 움직이는 속도 조절용

'''(6) 토끼 키보드로 움직이기 '''
rx = 100
ry = 200

while isRunning:
    cnt += 1
    for event in pygame.event.get(): # 이벤트를 모아서 event에 담기(마우스프레스 등등)                
        if event.type == pygame.QUIT:# 만약 담은것 중에 QUIT이 있으면
            isRunning = False        # isRunning 을 종료해
        
    # (6) 토끼 키보드로 움직이기 
    keys = pygame.key.get_pressed()  # 키가 눌렸을 때 1 or 0을 입력
    # print(keys[pygame.K_LEFT]) Left키 누르면 1로 뜸
    
    if keys[pygame.K_LEFT] == 1:
        if count == 2:  # (5) 2번에 1번씩 움직이도록 =>속도조절
            rx -= 5
            count = 0 
        else:
            count += 1
    if keys[pygame.K_UP] == 1:
        ry -= 5
    if keys[pygame.K_RIGHT] == 1:
        rx += 5
    if keys[pygame.K_DOWN] == 1:
        ry += 5
    
    # (5) 캐릭터 움직이는 것 처럼 보이게 만들기 
    screen.blit(bg,(0,0))               # 1.배경불러오기
    if cnt%2 == 0 :                     # 2.cnt가 짝수면
        screen.blit(rabbit1,(rx,ry))    #   rabbit1찍기
    else:                               # 3.그 이외에는    
        screen.blit(rabbit2,(rx,ry))    #   rabbit2찍기


    pygame.display.update() # 게임화면을 다시 그리기

pygame.quit()