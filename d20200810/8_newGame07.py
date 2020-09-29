import pygame
import math

# [1] 게임의 기본틀 
pygame.init()
screen_width=600
screen_height=900
screen = pygame.display.set_mode((screen_width,screen_height))
isRunning = True
pygame.display.set_caption("우주 전쟁")

# [2] 배경 그리기
bg1 = pygame.image.load("e:/dev/python_workspace/img/space.jpg")
bg2 = pygame.image.load("e:/dev/python_workspace/img/space.jpg")
bg1 = pygame.transform.scale(bg1,(600,900))
bg2 = pygame.transform.scale(bg2,(600,900))

# [3] 캐릭터 우주선 그리기
player1 = pygame.image.load("e:/dev/python_workspace/img/player1.png")
player2 = pygame.image.load("e:/dev/python_workspace/img/player2.png")
player3 = pygame.image.load("e:/dev/python_workspace/img/player3.png")
player4 = pygame.image.load("e:/dev/python_workspace/img/player4.png")

# [4] 배경 움직이게 만들기 :y좌표 변수
bg1Y = 0
bg2Y = -900

# [5] 우주선 움직이는 것 처럼 만들기
cnt = 0

# [6] 우주선 마우스로 조작하기: 캐릭터 우주선 좌표 변수
px = 250
py = 800

# [7] 미사일 발사 : 객체 생성
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

# [8] 적우주선 그리기 & 움직이기
gunship0 = pygame.image.load("e:/dev/python_workspace/img/gunship0.png")
gunship1 = pygame.image.load("e:/dev/python_workspace/img/gunship1.png")
gunship2 = pygame.image.load("e:/dev/python_workspace/img/gunship2.png")
gunship3 = pygame.image.load("e:/dev/python_workspace/img/gunship3.png")
gx = 200
gy = 0

# [9] 적우주선이랑 미사일이랑 충돌 이벤트

## [9-1] 미사일과 적우주선 사이의 거리 측정
def pythagoras(x1,y1,x2,y2):
  return math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))

## [9-2] 충돌 체크 함수
def collision():
  global gy
  for m in missileList:
    dis = pythagoras(gx, gy, m.x, m.y)
    if dis < 30 :   # 맞으면:
      print("아야",dis)
      gy -= 2       # --> 맞으면 우주선 살짝 뒤로 밀리게 하기
      m.x = -100    # --> 맞으면 미사일 사라지게 하기

while isRunning:            # isRunning이 True라면:

    
    # [4] 배경 움직이게 만들기 :y좌표 점점 내려가게 하기 
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

    # [5] 캐릭터 우주선 움직이게 만들기
    cnt +=1
 
    # [7] 미사일 발사 : y좌표 줄어들게 만들기
    my -=1
    
    # [7] 미사일 발사 : 미사일 그리기
    for m in missileList:
      screen.blit(missile,(m.x,m.y))
      m.y-=2
      if m.y <= -50:     # 화면 밖으로 사라지면 메모리에서 삭제하기
        missileList.remove(m)
        del(m)

    # [7] 마우스 좌표 구하기 print(pygame.mouse.get_pos())
    px, py = pygame.mouse.get_pos()

    # [1] 계속 화면이 출력되도록 하기
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

        # [7] 미사일 발사 : 클릭하는 이벤트 실행
        if event.type == pygame.MOUSEBUTTONDOWN:
          print("마우스 클릭됨")
          mx, my = pygame.mouse.get_pos()
          missileList.append(Missile(mx,my))

    # [9-3] 적우주선과 미사일의 충돌 발생 여부 체크하는 함수 호출
    collision()

    # [8] 적우주선 움직이게 만들기
    gy +=1
    if cnt % 4 == 0 :
      screen.blit(gunship0,(gx-25,gy-25))
    elif cnt % 4 == 1:
      screen.blit(gunship1,(gx-25,gy-25))
    elif cnt % 4 == 2:
      screen.blit(gunship2,(gx-25,gy-25))
    elif cnt % 4 == 3:
      screen.blit(gunship3,(gx-25,gy-25))
    
    # [5] 캐릭터 우주선 움직이게 만들기
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