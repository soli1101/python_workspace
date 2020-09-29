import pygame
import math

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
isRunning = True    # 게임을 계속 진행할지, 중지할지를 결정하는 변수 flag

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
snipe = pygame.transform.scale(snipe,(110,100))
sx = 100
sy = 100

'''(12) hole 담기'''
hole = pygame.image.load("e:/dev/python_workspace/img/hole.png")
hole = pygame.transform.scale(hole,(20,20))
hx = 300
hy = 300


'''(15) 반동 변수'''
rebound = 0 # 조준경 그릴 때 rebound 만큼 빼기 


'''(16) 점수판 만들기 '''
# 16-1 font 객체
pygame.font.init()
myfont = pygame.font.SysFont("Comic Sans MS", 30)

# 16-2 점수 변수
score = 0 



# 특정 사운드 객체 
# fsound = pygame.mixer.Sound("e:/dev/python_workspace/sounds/fire.wav")
# fSound.set_volume(1)
# fSound.play()

'''(13) 맞으면 "명중입니다!" 안맞았으면 "shot!"출력하기''' 
# 토끼의 중심좌표와 마우스 클릭 위치의 거리를 구하기
def pythagoras(x1,y1,x2,y2):
    return math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))

'''(14) 명중하면 '아야' 소리 연결하기'''
# scream = pygame.mixer.Sound("e:/dev/python_workspace/sounds/scream.wav")
# scream.set_volume(1)


while isRunning:
    cnt += 1

    # (5) 캐릭터 움직이는 것 처럼 보이게 만들기 
    screen.blit(bg1,(bg1X,0))           # 1.배경불러오기
    screen.blit(bg2,(bg2X,0))            
    if cnt%2 == 0 :                     # 2.cnt가 짝수면
        screen.blit(rabbit1,(rx,ry))    #   rabbit1찍기
    else:                               # 3.그 이외에는    
        screen.blit(rabbit2,(rx,ry))    #   rabbit2찍기
    
    # (6) 토끼 키보드로 움직이기 
    #     print(keys[pygame.K_LEFT]) Left키 누르면 1로 뜸
    keys = pygame.key.get_pressed()  # 키가 눌렸을 때 1 or 0을 입력
    if keys[pygame.K_LEFT] == 1:
        if 5 <= rx <=1105:       # (10) 토끼가 밖으로 나가지 않게 setting
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

    # (7) Frame 지정
    #     Frame 확인 print('fps:'+str(clock.get_fps()))
    fps = clock.tick(100) # 화면의 초당 프레임수 30

    # (8) 배경 움직이게 만들기
    bg1X -= 2  
    bg2X -= 2
    if bg1X <= -1200:
        bg1X = 1200
        bg2X = 0 
    if bg2X <= -1200:
        bg2X = 1200
        bg1X = 0

    # (9) 음악 play & stop
    # if keys[pygame.K_1] == 1:       # 1번키가 눌리면,
    #     pygame.mixer.music.stop()   # 음악을 중지해
    # if keys[pygame.K_2] == 1:       
    #     pygame.mixer.music.play()

    # (11)(12) snipe, hole 담기
    #      print(pygame.mouse.get_pos())     # 마우스의 포지션
    #      print(pygame.mouse.get_pressed()) # 마우스 눌렸는지 여부 감지
    screen.blit(hole,(hx-10,hy-10))
    screen.blit(snipe,(sx-56,sy+-52-rebound))
    sx, sy = pygame.mouse.get_pos()
    
    # (15) 반동
    if rebound > 2:
        rebound -=2



    for event in pygame.event.get(): # 이벤트를 모아서 event에 담기(마우스프레스 등등)                
        if event.type == pygame.QUIT:# 만약 담은것 중에 QUIT이 있으면
            isRunning = False        # isRunning 을 종료해
        
        # (12) hole 담기 (마우스 클릭할 때)
        if event.type == pygame.MOUSEBUTTONUP:
            
            # (15) 반동
            rebound = 50  # 총소리와 함께 약간 위로 올라가도록 설정

            # (9) fSound.play() --> 출력기기 없어서 안됨 
            print("Shot!")

            # 마우스 클릭한 위치에 hole의 x,y좌표 찍어서 그림 붙이기
            hx, hy = pygame.mouse.get_pos()      
            dis = pythagoras(rx+50,ry+60,hx,hy)
            print(dis)
            
            # (12) 맞으면 "명중입니다!" 안맞았으면 "shot!"출력하기
            if 0 <= dis <=70:
                # scream.play()
                print("명중!")     

                # (16-4) 맞으면 점수 올리기
                score += 100 

    # (16-3) 점수판
          ## antialias <== False
          ## 화상 내의 선과 모서리를 매끄럽게 나타내는 효과
    txt = myfont.render("Score:"+str(score),False,(255,0,0))
    screen.blit(txt,(550,50))


    pygame.display.update() # 게임화면을 다시 그리기

pygame.quit()