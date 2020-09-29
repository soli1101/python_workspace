print('--------dictionary----------')        
mydic = dict(k1=1,k2='abc',k3=3.4)
print(mydic)
print('-------------------------')
dic = {"파이썬":"뱀","자바":"커피",'오라클':'델파이'}
print(dic, len(dic))
print('-------------------------')
print(dic['자바'])  # dictionary 안에 키 값을 넣으면 value값을 꺼내줌
print('-------------------------')
dic['스미스']="백그라운드프로세스"  # 새로운 키value값 추가
print(dic)
dic['neo']="키아누리브스"
dic['스미스']="bg"              # 있는 값을 할당하면 덮어씀
print('-------덮어쓰기---------')
print(dic)
print('-------------------------')
dic['neo']="잘생김"             # 중복 X 덮어쓴다
print(dic)
print()

print('------- value들만 출력 -------')
for val in dic.values():
    print(val)
print('------- key와 value들 출력 -------')
for key, val in dic.items():
    print("key =",key, ", value =",val)
print('---- 같은출력 다른방법 ----')
for key, val in dic.items():
    print("key : {key}, value: {val}".format(key=key,val=val))
print()

print('---- 키가 있는지 여부 판단 : in ----')
print('neo' in dic)   # True, False 형태로 리턴
print()

print('------ neo 삭제 ------')
del dic['neo']        # 키 값이 neo 인 항목 삭제
print(dic)
print()

print('--- key값에 여러개의 value를 가질 수 있다 ---')
dic['game']=['대항해시대','바람의나라','문명6','토탈워']
print(dic)
print()
dic['broadcasting_co']=['kbs','mbc','sbs','jtbc','ytn']
print(dic)
print('-------- 정렬 --------')
from pprint import pprint as pp   # 자동으로 정렬해 놓음
pp(dic)
