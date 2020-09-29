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
bg1 = pygame.image.load('e:/dev/python_workspace/img/bg.jpg')
bg2 = pygame.image.load('e:/dev/python_workspace/img/bg.jpg')
bg1 = pygame.transform.scale(bg1,(1200,800))
bg2 = pygame.transform.scale(bg2,(1200,800))
isRunning = True    # 게임을 계속 진행할지, 중지할지를 결정하는 변수

'''(4) 토끼 담기'''
rabbit1 = pygame.image.load('e:/dev/python_workspace/img/rabbit1.png')
rabbit2 = pygame.image.load('e:/dev/python_workspace/img/rabbit2.png')
# 사이즈조절 transform.scale(객체, (너비,높이))
rabbit1 = pygame.transform.scale(rabbit1,(100,130))
rabbit2 = pygame.transform.scale(rabbit2,(100,130))

'''(5) 움직이는 것 처럼 보이게 만들기 '''
cnt = 0                     # 움직임 세는용

'''(6) 토끼 키보드로 움직이기 '''
rx = 100
ry = 200

'''(7) 시계 변수 : 화면 초당 프레임 수 조절로 속도 조절 '''
clock = pygame.time.Clock() # 시계변수 : 움직이는 속도 조절용

'''(8) 배경 움직이게 만들기'''
bg1X = 0
bg2X = 1200

'''(9) 배경 음악 setting '''
# pygame.mixer.music.load('e:/dev/python_workspace/sounds/backsound.mp3')
# pygame.mixer.music.set_volume(1) # 1 ~ 0.1
# pygame.mixer.music.play(1)

'''(10) 토끼 화면 밖으로 나가지 않게 setting '''
# 좌측상단이 항상 (0,0) #

'''(11) snipe 조준경 담기 '''
snipe = pygame.image.load("e:/dev/python_workspace/img/snipe.png")
snipe = pygame.transform.scale(snipe,(210,200))
sx = 100
sy = 100

while isRunning:
    cnt += 1
    

    # (10) 토끼 화면 밖으로 나가지 않게

    # (8) 배경 움직이게 만들기
    bg1X -= 2  
    bg2X -= 2
    if bg1X <= -1200:
        bg1X = 1200
        bg2X = 0 
    if bg2X <= -1200:
        bg2X = 1200
        bg1X = 0

    # (7) Frame 지정
    #     Frame 확인 print('fps:'+str(clock.get_fps()))
    fps = clock.tick(100) # 화면의 초당 프레임수 30

    for event in pygame.event.get(): # 이벤트를 모아서 event에 담기(마우스프레스 등등)                
        if event.type == pygame.QUIT:# 만약 담은것 중에 QUIT이 있으면
            isRunning = False        # isRunning 을 종료해
        
    # (6) 토끼 키보드로 움직이기 
    keys = pygame.key.get_pressed()  # 키가 눌렸을 때 1 or 0을 입력
    # print(keys[pygame.K_LEFT]) Left키 누르면 1로 뜸
    
    if keys[pygame.K_LEFT] == 1:
        if 5 <= rx <=1105:
            rx -= 5
    if keys[pygame.K_UP] == 1:
        if 5 <= ry <= 705:
            ry -= 5
    if keys[pygame.K_RIGHT] == 1:
        if 0 <= rx <=1100:
            rx += 5
    if keys[pygame.K_DOWN] == 1:
        if 0 <= ry <= 700:
            ry += 5
    
    # (9) 음악 play & stop
    # if keys[pygame.K_1] == 1:       # 1번키가 눌리면,
    #     pygame.mixer.music.stop()   # 음악을 중지해
    # if keys[pygame.K_2] == 1:       
    #     pygame.mixer.music.play()


    # (5) 캐릭터 움직이는 것 처럼 보이게 만들기 
    screen.blit(bg1,(bg1X,0))           # 1.배경불러오기
    screen.blit(bg2,(bg2X,0))            

    if cnt%2 == 0 :                     # 2.cnt가 짝수면
        screen.blit(rabbit1,(rx,ry))    #   rabbit1찍기
    else:                               # 3.그 이외에는    
        screen.blit(rabbit2,(rx,ry))    #   rabbit2찍기

    # (11) snipe 담기
    screen.blit(snipe,(sx,sy))


    pygame.display.update() # 게임화면을 다시 그리기

pygame.quit()