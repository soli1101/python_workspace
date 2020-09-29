print('----Regular Expression 정규 표현식----')
# 일정한 규칙(패턴)을 가진 문자열을 표현하는 방법
# 특정한 규칙을 가진 문자열의 집합을 표현하는 사용하는 형식 언어
# 대부분의 텍스트 편집기와 프로그램언어에서 문자열의 검색과 치환을 위해 지원하고 있다.

import re   # regular expression의 준말
print('----# re.match(패턴,문자열) ----')
print(re.match("hello","hello python world"))
print()

print('----# 문자열, : .find() ----')
print("hello python wolrd".find("hello")) # 0은 존재 -1은 없음
print()

print('----re.search----')

print('----# ^H ----')             # ^:찻글자 
print("re.search:", re.search("^h","hello python world"))
print()

print('----# d$ ----')             # $:끝문자
print("re.match:",re.match("d$","hello python world"))
print()

print('----# 010-2481-3049 ----')
print(re.match('[0-9]+','1234'))   # +는 1개 이상
print(re.match('[0-9]*','1234'))   # *은 0개 이상
print()

print('----#aaabbb ----') #a가 한개 이상 있는지 찾고 싶어
print(re.match('a+b','aaabbb'))    # a가 여러개오고 b가 있어?
print()

print('----# 글자 찾기 [가-힣] ----')
print(re.match('[가-힣]','불금달료보자.')) # 가-힣
print()

print('----? 사용해보기----')
# +는 1개 이상, *는 0개 이상, ?는 0 또는 1
print('----#ab9cd ab9999cd : ?사용----')
print(re.match('ab[0-9]?cd','ab9cd'))    # 9가 1개 이므로 출력
print(re.match('ab[0-9]?cd','ab9999cd')) # 9가 1개 이상이므로 x