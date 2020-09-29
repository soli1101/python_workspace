import pygame
import math
import random
import os

os.environ['SDL_VIDEO_WINDOW.POS']="50,50"

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
def collision(x1,y1,x2,y2):
  global gy
  for m in missileList:
    dis = pythagoras(x1, y1, x2, y2)
    result = 0
    if dis < 30 :   # 맞으면:
      result = 1
  return result


# [10] 적우주선 다량 출현
## [10-1] 적우주선 만드는 클래스 생성하고 & 생성하기 
enemyList = []
def makeEnemy():
  e = EnemyShip(random.randint(1,550),50,100,1)
  enemyList.append(e)

# [11-1] 우주선이 충돌하면 게임종료하는 인자
isGameOver = False

# [11] 캐릭터 우주선과 적우주선 간의 충돌 체크를 위한 함수
def checkCollision(px,py):
  global isGameOver
  for e in enemyList:
    dis = pythagoras(e.x,e.y,px,py)
    print(dis)
    if dis <= 33:
      print("아야~~~~~")
      isGameOver = True

class EnemyShip: 
  def __init__(self,x,y,hp,type):
    self.x = x
    self.y = y
    self.hp = hp
    self.type = type  # type1:일반/ type2:보스 
  def __del__(self):
    print("적 제거됨")

# [12] 게임 점수 스코어판 만들기
score = 0
myfont = pygame.font.SysFont("Comic Sans MS",30)

# [13] 배경음악&미사일소리
'''
bgSound = pygame.mixer.music
bgSound.load("e:/dev/python_workspace/sounds/animalforest.mp3")
bgSound.set_volume(0.5)
bgSound.play()

fireSound = pygame.mixer.Sound("e:/dev/python_workspace/sounds/fire3.wav")
fireSound.set_volume(0.8)
'''


while isRunning:
  # [11-1] 우주선이 충돌하면 게임종료하는 인자
  # 게임이 진행중인 종료 상태인지 출력
  # print("isGameover:", isGameOver)
  if isGameOver:
    bg1Y = 0
    bg2Y = 0
  else:
    bg1Y +=2
    bg2Y +=2

  # [11] 캐릭터 우주선과 적우주선 간의 충돌 체크를 위한 함수
  checkCollision(px,py)
  
  # [10-2] [11] 적우주선 객체 생성
  if cnt % 200 == 0 and isGameOver == False:  # --> 적우주선 출현 빈도수  
      makeEnemy()

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
        # [13] 미사일 소리 출력
        # fireSound.play()

  # [10-3] 적우주선과 미사일의 충돌 발생 여부 체크하는 함수 호출
  for m in missileList:
    for e in enemyList:
      result = collision(e.x, e.y, m.x, m.y)
      if result == 1 :  # 맞으면:
        e.y -= 3        # 적우주선 약간 뒤로 밀기
        m.y = -100      # 미사일은 화면밖으로 뿅
        e.hp -= 50      # 적 체력 50 감소
        # [12] 점수 추가하기
        score += 50

      if e.hp <= 0:     # 적의 체력이 0이하면:
        # [12] 점수 추가하기2
        score += 100
        e.y =950        # 화면 밖으로 내보내기
        enemyList.remove(e)    # 죽은걸로 처리 
        del(e)
      

  # [8] 적우주선 그리고 움직이게 만들기
  for e in enemyList:
    if cnt % 4 == 0 :
      screen.blit(gunship0,(e.x-25,e.y-25))
    elif cnt % 4 == 1:
      screen.blit(gunship1,(e.x-25,e.y-25))
    elif cnt % 4 == 2:
      screen.blit(gunship2,(e.x-25,e.y-25))
    elif cnt % 4 == 3:
      screen.blit(gunship3,(e.x-25,e.y-25))
      e.y+=3      # --> 적우주선이 움직이는 속도 
  
  # [10] 적우주선이 밖으로 나가면 제거 
    if e.y >= 950:    # 적우주선 밖으로 나가면:
      enemyList.remove(e)    # 제거
      del(e)
  
  
  # [5] 캐릭터 우주선 움직이게 만들기
  if cnt % 4 == 0 :
    screen.blit(player1,(px-28,py-26))
  elif cnt % 4 == 1:
    screen.blit(player2,(px-28,py-26))
  elif cnt % 4 == 2:
    screen.blit(player3,(px-28,py-26))
  elif cnt % 4 == 3:
    screen.blit(player4,(px-28,py-26))

  # [12] 게임 점수 스코어판 만들기
  if isGameOver:
    myfont2 = pygame.font.SysFont('Comic Sans MS', 80)
    txt2 = myfont2.render("GAME OVER",False,(255,0,0))
    screen.blit(txt2,(50,250))
    
  else:
    txt = myfont.render("Score:"+str(score),False,(255,0,0))
    screen.blit(txt,(150,25))

  # [13] 인서트 코인
  keys = pygame.key.get_pressed()
  if keys[pygame.K_i] == 1:
    isGameOver = False
    score = 0 

  pygame.display.update() # 창이 뜨면 무한반복

pygame.display.update()
pygame.quit()