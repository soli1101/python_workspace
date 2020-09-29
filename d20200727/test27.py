#1
# a=int(input("input number"))
#     b=int(input("input number"))
#     def avg(a, b):
#         return (a+b)/2

#2
def max_min(listData):
        return print(max(sList),min(sList))

#3
import os
def get_list(path):
    for file in os.listdir(path):
        if file.endswith('txt'):
            print(file)

#4
import time
def get_todate():
    m=time.ctime().split()
    if m[1] == 'Jul':
        m[1] = '7월'
    return m[1]+m[2]+'일'

#5
def get_triangle_area(width, height):
        return (width*height)/2

#6
import math

def get_circle_area(radius):
    return radius*radius*math.pi

#7

#8
def get_odd(list):
        return len([i for i in nList if i%2==1])

#9
#10
def get_last_word(list):
    wordList_3 = []
    for i in range(20):
        wordList_3.append(list[i][2:5])
    return wordList_3


if __name__ == "__main__":
    print('----#1----')
    '''
    1. 두 개의 정수 값을 받아 두 값의 평균을 구하는 함수를 작성하고 임의의 값으로 실행 하세요 

    '''
    a=int(input("input number"))
    b=int(input("input number"))
    def avg(a, b):
        return (a+b)/2
    print(avg(a,b))
    print()

    print('----#2----')
    '''
    2. sList 는 학생들의 영어 점수로 만든 리스트 이다.  최댓값과 최솟값을 반환하는 함수를 작성하세요.
    '''
    sList = [ 90, 80, 23, 55, 32, 50, 95, 90, 85, 60, 75, 35, 88, 92]

    def max_min(listData):
        return print(max(sList),min(sList))
    max_min(sList)
    print()

    print('----#3----')
    '''
    3. e:/dev/python_workspace/  경로에 있는 *.txt 파일의 목록을 파이썬 리스트로 반환하는 함수를 작성하세요.
    '''
    import os
    def get_list(path):
        for file in os.listdir(path):
            if file.endswith('txt'):
                print(file)

    get_list('e:/dev/python_workspace/')
    print()

    print('----#4----')

    '''
    4. 오늘의 월 일을 출력하는 함수를 작성하세요 
    # print(get_todate())   # 7월 27일 
    '''
    import time
    def get_todate():
        m=time.ctime().split()
        if m[1] == 'Jul':
            m[1] = '7월'
        return m[1]+m[2]+'일'
    print(get_todate())
    print()

    print('----#5----')
    '''
    5.  다음 함수를 작성하세요 
    '''
    def get_triangle_area(width, height):
        return (width*height)/2

    print(get_triangle_area(100,200))  # 10000
    print()

    print('----#6----')
    import math

    def get_circle_area(radius):
        return radius*radius*math.pi

    print(get_circle_area(10))  # 314.1592653589793
    print()

    print('----#7----')
    '''
    7. nList 에 랜덤하게 1부터 100사이 의 정수 20개 를 넣는다. 
    '''
    from random import *
    n=list(range(1,101))
    nList = sample(n,20)
    print(nList)
    print()

    print('----#8----')
    '''
    8. nList에 홀수 가 몇개가 있는지 를 리턴하는 함수를 구하세요 
    '''
    def get_odd(list):
        return len([i for i in nList if i%2==1])

    print(get_odd(nList))  # n
    print()

    print('----#9----')
    '''
    9.  5자로 구성된 랜덤문자를 만들어 20개를 넣는다. 
    '''
    alphabet='a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
    wordList = []

    for j in range(20):
        wordList.append(sample(alphabet,5))
    print(wordList)   

    # wordList = ['abcde', 'xwdsd, ....]
    print()

    print('----#10----')
    '''
    10. wordList 요소에서 뒤에 3글자만 자른 문자를 갖는 리스트를 출력하는 함수를 작성하세요
    '''
    def get_last_word(list):
        wordList_3 = []
        for i in range(20):
            wordList_3.append(list[i][2:5])
        return wordList_3

    print(get_last_word(wordList))  #  [ cde ,  dsd  , .... ]
    print()

    print('----#11----')

    '''
    11. 지금까지 만들어진 함수를 test27 라는 모듈로 작성하세요
    '''
    author = "hanah"

    '''
    print()

    print('----#12----')
    12. 현재 파일에서 실행할때만 테스트 결과가 출력되게 작성하세요 
    OK
    '''
    print()

    print('----#13----')
    '''
    13. ex1.py 파일을 작성하고  test. get_circle_area(300)을 실행시켜보세요
    '''
    print()

    print('----#13----')
    '''
    14. 다른 모듈의 함수를 불러 사용하는 방법 3가지를 정리하세요 
    '''
    print('1.import 모듈명')
    print('2.from 모듈명 import 함수명')
    print('2.from 모듈명 import *')
