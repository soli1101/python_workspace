from pygame import *
import math
import random

init()

# 화면설정 
'''1. 화면생성'''
screen = display.set_mode((1200,800))

'''2. Title'''
display.set_caption("고군분투 따라잡기")

'''3. 배경담기'''
bg1 = image.load('e:/dev/python_workspace/img/bg1.jpg')
bg2 = image.load('e:/dev/python_workspace/img/bg2.jpg')
bg1 = transform.scale(bg1,(1200,800))
bg2 = transform.scale(bg2,(1200,800))
isrunning = True

'''4. 캐릭터 담기'''
run1 = image.load('e:/dev/python_workspace/img/run1.png')
run2 = image.load('e:/dev/python_workspace/img/run2.png')
run3 = image.load('e:/dev/python_workspace/img/run3.png')
run1 = transform.scale(run1,(100,100))
run2 = transform.scale(run2,(100,100))
run3 = transform.scale(run3,(100,100))


'''5. 캐릭터가 움직이는 것 처럼 보이게 만들기'''
cnt=0
count=0

'''6. 캐릭터를 키보드로 조작하기 '''
rx = 100
ry = 500

# '''7. 시계변수 : 화면 초당 프레임 설정'''
# clock = time.Clock()

'''8. 배경 움직이게 만들기'''
bg1X = 0 
bg2X = 1200 

'''9. 코인 그리기 & 움직이기'''
gold = image.load('e:/dev/python_workspace/img/gold.png')
goldx = 1000
goldy = 510

'''10. 코인 다량 생성 '''
goldList = []

def makeCoin():
    coin = goldCoin(1200,random.randint(400,550))
    goldList.append(coin)

class goldCoin:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __del__(self):
        print("코인 제거")

# (10) 거리 계산에 필요한 피타고라스 함수 정의
def pythagoras(x1,y1,x2,y2):
    return math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))

# (10) 충돌 체크 함수
def collision(x1,y1,x2,y2):
    global goldy
    dis = pythagoras(x1,y2,x2,y2)
    print(dis)
    result = 0
    if dis < 2:        # 맞으면~ :
        goldy = -100    # 맞으면 화면 밖으로 내보내기
        result = 1
    
    return result


while isrunning:
    cnt += 1
    
    #(10) 코인 생성 
    if cnt%20==0:   # --> 코인 생성 빈도수 
        makeCoin()

    #(10) 코인과 캐릭터 충돌 여부 체크하는 함수 호출
    for coin in goldList:
        result = collision(coin.x, coin.y, rx+50, ry-50)
        print(coin.x, coin.y, rx, ry)
        if result == 1:
            goldList.remove(coin)
            del(coin)
  
    #(5) 캐릭터 움직이게 하기
    screen.blit(bg1,(bg1X,0))
    screen.blit(bg2,(bg2X,0))

    if cnt%3 == 0 :
        screen.blit(run1,(rx,ry))
    elif cnt%3 == 1 :
        screen.blit(run2,(rx,ry))
    elif cnt%3 == 2 :
        screen.blit(run3,(rx,ry))

    for event1 in event.get():
        if event1.type == QUIT:
            isrunning = False 

    #(8) 배경 움직이게 만들기
    bg1X -= 2
    bg2X -= 2
    if bg1X <= -1200 :
        bg1X = 1200
        bg2X = 0
    if bg2X <= -1200 :
        bg2X = 1200
        bg1X = 0
    
    #(9) 코인 움직이기
    for coin in goldList:
        screen.blit(gold,(coin.x,coin.y))
        coin.x -= 3


    display.update()

quit()