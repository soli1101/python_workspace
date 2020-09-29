import random

def raise_rnd_salary(sal):
    rnd = random.randint(0,1)
    if rnd == 0:
        print("강화성공")
        return sal*1.5
    else:
        print('아무일도 일어나지 않았습니다')
        return sal

def reduce_rnd_salary(sal):
    rnd = random.randint(0,1)
    if rnd == 0:
        print("강화실패")
        return sal*0.5
    else:
        print('아무일도 일어나지 않았습니다')
        return sal
if __name__ == "__main__":
    print(raise_rnd_salary(100))
    print(reduce_rnd_salary(100))