print('***********리스트***********')
# 순서 ㅇ, 중복 ㅇ, 변경 ㅇ
print('-------------------------')
a = [1,2,3]
print(a, type(a))
print('-------------------------')
b = [10, a, True, '문자열']
print(b)
print('-------------------------')
print(b[1])                    # b리스트의 1번 인덱스 출력해
print(b[1][2])                 # 리스트 안에 있는 애에 다시 접근
print('-------------------------')
c = [[1,2], [3,4,5], [6,7,8,9]]# 리스트 안에 리스트 생성 가능
print(c)                       # c리스트를 출력
print(c[1][1])                 # c리스트의 1번list의 1번 index 출력
print(c[2][2])                 # c리스트의 2번list의 2번 index 출력
print('---------#동물---------')
pet = ['강아지','고양이','거북이','고슴도치']
print(pet)
pet.append("열대어")            # append 1개 추가하기
print(pet)
pet.remove("거북이")            # remove 목록에서 제거하기
print(pet)
pet.insert(0,"이구아나")        # insert 특정 위치에 추가
print(pet)
pet.extend(["토끼","햄스터"])   # extend 여러개 추가
print(pet)
pet += ["돼지"]                 # += 로도 여러개 추가 가능
print(pet)
print("동물의 갯수:",len(pet))  # pet의 index 갯수를 출력해
print('-----#연습2 고슴도치 제거-----')
del pet[3]                      # del 순서를 가지고 삭제 가능
print(pet)
print('-------------------------')
animal = pet
print("animal:", animal)
print("pet:", pet)

pet[0]='멍멍이'
print('-------------------------')
print("animal:", animal)
print("pet:", pet)

print(id(animal), id(pet))      # 같은 대상을 참조