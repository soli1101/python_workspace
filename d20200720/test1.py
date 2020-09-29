print('***********SET***********')
a = {1,2,3}
print(a, type(a))  # print(a[0])X
b = {3,4}
print()
print('--------집합:합치기--------')
print(a.union(b)) #합집합
print(a.intersection(b)) #교집합
print(a-b, a|b, a&b) #차집합
print()
print('--------추가-------')
b.add(5) # 추가
print(b)
b.update({6,7}) #SET 추가
print(b)
b.update((8,9)) #TUPLE 추가
print(b)
b.update({10,11}) #LIST 추가
print(b)
print()
print('--------제거--------')
b.discard(7)
print(b)
b.remove(8)
print(b)
print()
print('------형변환, 삭제-------')
c=set() # set()를 통해서 형변환 가능
c = b
print(c)
c.clear() # 안의 내용을 싹 지워줄 수 있다
print()
print('----------문제----------')
# 다음 리스트의 중복된 값은 제거하려고 한다.
m=[2,3,11,29,3,2,7,8,11]
# list 순서 ㅇ, 중복 ㅇ
# 1. set으로 형변환 ? 중복값이 사라진다
mm=set(m)
print("mm:",mm)
# 2. 리스트로 변경
m=list(mm)
print("m",m)
# 3. 정렬?
m.sort()
print("sort:",m)