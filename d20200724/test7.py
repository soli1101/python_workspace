print('****compile ****')
# 패턴 : 정규식을 컴파일한 결과

# 문자열 검색
# match() : 문자열의 처음부터 정규식과 매치되는지 조사
# search() : 문자열 전체를 검색해서 정규식과 매치되는지 조사
# findall() : 정규식과 매치되는 모든 문자열을 리스트로 불러준다
# finditer() : 정규식과 매치되는 모든 문자열을 반복가능한 객체로 불러준다

import re
p=re.compile('[a-z]+')
print(p, type(p))
print()

print('***match*******************')
m = p.match("regular expression")
print(m)
print()

print('***group: 내용을 보여준다***')
if m:
    print(m.group())
else:
    print("no match")
print()

print('******search************')
result=p.search("99999999999 aaaabbbbbb")
print(result)
print()

print('******findall***********')
result2=p.findall("hello python world today is monday")
print(result2)
print()

print('***for문으로 출력해 보기***')
# for문으로 1개씩 출력
for i in result2:
    print(i)
print()

print('******finditer**********')
result3=p.finditer("today is monday")
print(result3)
for data in result3:
    print("data:",data)
    print("data.group:",data.group()) #group을 해야 값을 볼 수 있다
    print('**** ****')
    print(data.start(),":",data.end())
print()

print('****# email만 선택해서 출력 ****')
# email만 선택해서 출력
msg = "999,999 smartphone bbb@naver.com aaa@gmail.com"
p2=re.compile('[a-zA-Z0-9._]+@[a-zA-Z0-9]+.[a-zA-Z0-9]+')
print("p2의 내용:",p2)
result4=p2.findall(msg) # findall() : 정규식과 매치되는 모든 문자열을 리스트로 불러준다
print("result4:",result4)
for email in result4:
    print(email)