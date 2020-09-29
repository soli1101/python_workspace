print('----map: built-in 함수----')
'''

#map함수 : built-in 함수 설치하면 기본적으로 들어있는 함수

list나 dictionary 와 같은 iterable 한 데이터를 인자로 받아 list 안에

개별 item을 함수의 인자로 전달하여 결과를 list형태로 출력하는 함수

ex)random, input, print, map


'''
def func1(x):
    return x*2  # 간단한 로직
m = [10,20,30,40]
n = []
for i in range(len(m)):
    n.append(func1(m[i]))
print(n)
print('------map함수사용-----')
print(list(map(func1,m)))

t = { 1:100,2:200,3:300 }
print('-------key값 넣기--------')
print(list(map(func1,t)))
print('t는 key값')
print('-------value값 넣기--------')
print(list(map(func1,[t[i] for i in t]))) 
print('t[i]는 value값')
# t는 key값이고 t[i]는 value값
print('-------------------------')
for i in t:
    print(t[i])
print()

print('----연습1: 3의 배수만 출력------')
a= [1,2,3,4,5,6,7,8,9,10]
# makeString(x) 'x'라는 문자로 출력하도록
def makeString(x):
    words=[]
    if x%3==0:          # 3의 배수이면
        return str(x)   # x를 글자로 리턴하고
    else:               # 아니면 
        return x        # 그냥 숫자로 리턴해
print(str([i for i in a if i%3==0]))   # 리스트 내포 사용해서 출력    
print('--------3의 배수만 숫자로 나머진 문자로 -----------------')
# map 함수로 묶어서 쓰기
print(list(map(makeString,a))) 
print('------람다함수로! 3의 배수만 숫자로 나머진 문자로-------')
print(list(map(lambda x : str(x) if x%3==0 else x,a))) 
print()


print('----연습2: 소수면 실수로, 아니면 자기자신을 리턴 ----')
# 실수로 리던 : float() 3->3.0 
# 아니면 자기자신 4->4
def primeNumber(x):
    c= 0
    for i in range(2,x):
        if x%i==0:
            c+=1
    if c==0 :         # 2부터 x바로 전 수까지 x로 나누어서 하나라도 
        return float(x) # 나머지가 0이면 소수가 아니다
    else:
        return x
t = primeNumber(20)
print(t)
print()
print('----#filter----')
#filter : 조건에 일치하는 값만 추출할 때 사용하는 함수
def test2(x):
    if x>0:
        return x
    else:
        return None
n = [-3,-2,-1,0,1,2,3]

print(list(filter(test2,n)))
print()
print('----#filter 람다식으로 표현----')
print(list(filter( lambda x: x>0, n)))
print()
print('----연습3: filter, 람다식으로 60점 이상 추출----')
score =[80,70,53,50,76,80,45,55]
print(list(filter( lambda x: x>60, score)))

print()
print('----연습4: 현재 작업디렉토리에서 파일들의 목록 가져와----')

file_names = ['movie1.jpg','movie2.png','rabbit.png','bg.png','test.txt','test2.py']
# png 파일의 확장자만 검사해서 파일의 이름 출력
# 람다식으로 만들어 보기
# print(list(map( lambda x: x if 'png' in file_names[i]),file_names))
# for i in range(len(file_names)):
print('----연습4: filter 사용해서 표현----')

def png_Finder(x):
    if x.find('.png') != -1:
        return x        # 위 조건을 만족하는 x값을 리턴해 
    else :              # else 일 때 할 일이 없으면 filter
        return None     # else도 조건이 있으면 map 사용

print(png_Finder("movie.png"))
print(list(filter(png_Finder,file_names)))
print()

print('----연습4: lambda 사용해서 표현----')
# print(list(filter(lambda x: x if file_names[i].find(x) != -1), file_names))
print(list(filter( lambda x: x.find('.png')  != -1 ,file_names)))