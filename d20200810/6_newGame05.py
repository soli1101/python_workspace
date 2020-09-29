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

# 우주선 마우스로 조작하기: 캐릭터 우주선 좌표 변수
px = 250
py = 800

# 우주선 움직이는 것 처럼 만들기
cnt = 0

# 배경 움직이게 만들기 :y좌표 변수
bg1Y = 0
bg2Y = -900

# 미사일 발사 : 객체 생성
missile = pygame.image.load("e:/dev/python_workspace/img/missile1.png")
mx = -200
my = -900

missileList = []   # 미사일 발사하는 지점을 누적

class Missile:
  def __init__(self,x,y):
    self.x = x
    self.y = y

  def __del__(self):
    pass
    # print("소멸자: 미사일 제거됨")


while isRunning:            # isRunning이 True라면:
    # 미사일 발사 : y좌표 줄어들게 만들기
    my -=1

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
    
    # 미사일 발사 : 미사일 그리기
    for m in missileList:
      screen.blit(missile,(m.x,m.y))
      m.y-=2
      if m.y <= -50:     # 화면 밖으로 사라지면 메모리에서 삭제하기
        missileList.remove(m)
        del(m)


    # 마우스 좌표 구하기 print(pygame.mouse.get_pos())
    px, py = pygame.mouse.get_pos()

    # 계속 화면이 출력되도록 하기
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

        # 미사일 발사 : 클릭하는 이벤트 실행
        if event.type == pygame.MOUSEBUTTONDOWN:
          print("마우스 클릭됨")
          mx, my = pygame.mouse.get_pos()
          missileList.append(Missile(mx,my))

    
    # 캐릭터 우주선 움직이게 만들기
    if cnt % 4 == 0 :
      screen.blit(player1,(px-28,py-26))
    elif cnt % 4 == 1:
      screen.blit(player2,(px-28,py-26))
    elif cnt % 4 == 2:
      screen.blit(player3,(px-28,py-26))
    elif cnt % 4 == 3:
      screen.blit(player4,(px-28,py-26))









    pygame.display.update() # 창이 뜨면 무한반복

pygame.display.update()
pygame.quit()