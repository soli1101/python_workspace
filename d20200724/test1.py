
keyword = '오늘은 비가 언제 까지 올까요?'.split()
print('----split사용해서 문자열 끊어오기 ----')
print(keyword,type(keyword))
print()

print('----# 각 단어가 몇글자 인지 알아 내기 ----')
print({len(word) for word in keyword})
print(type(len(word) for word in keyword))
print()

print('----# 3자 이상만 선택해서 가져오기 ----')
print({len(word) for word in keyword if len(word)>3})
print(type(len(word) for word in keyword))
print()

print('----# dictionary comprehension ----')
countrys={"한국":"서울","일본":"도쿄","중국":"북경","UAE":"아부다비"}

print('----key만 출력----')
capital = {country for country, capital in countrys.items()}
# in 앞에 country, capital은 각각 key, value값이 순서대로 들어간다
print(capital)