import os
# 운영체제에서 제공되는 여러 기능을 파이썬에서 수행할 수 있게 해주는 모듈

print(dir(os))

print('----#현재작업 디렉토리를 알고싶어!----')
print(os.getcwd())

print('----#현재작업 디렉토리에 있는 파일과 디렉토리 목록을 알고싶어!----')
print(os.listdir())
print('-------------------------')
print(os.listdir('d20200727')) # 괄호안 폴더 안의 파일 목록 확인
print('-------------------------')
print(os.listdir('.')) # . 현재 디렉토리 E:\dev\python_workspace
print('-------------------------')
print(os.listdir('..')) # .. 부모 디렉토리
# print(os.listdir("d:\dev\python_workspace"))

print('----#연습: 현재 작업디렉토리에 있는 모든 파일을 출력 ----')
# 반복문 사용해서 한개씩 출력
for file in os.listdir():  # 괄호안에 공백은 현재 작업디렉토리
    print(file)
print('----#연습: c드라이브에서 zip파일 찾기----')
print('-----------find------------')
for file in os.listdir('c:/'):  # c드라이브
    if file.find('.zip')>0:
        print(file)
print('-----------endswith------------')
for file in os.listdir('c:/'):  # endswith : 이걸로 끝나는걸
    if file.endswith('zip'):    # 찾아줘. 파일 확장자로 찾을때 씀
        print(file)
