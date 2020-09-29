# 제어문
# 조건 분기문
# 주어진 조건이 발생하면 다른 문장이 실행되게 처리

# if 조건:
#     처리할문장
#     처리할문장

# elif 조건:
#     처리할문장
#     처리할문장

# else :
#     처리할문장
#     처리할문장

#사용자로부터 성적입력받기
# score=int(input("당신의 성적을 입력하세요:"))
# print(score>90)
# print('-------------------------')
# if score>=90:
#     print("당신의 성적은", score, "입니다. A 학점")
#     print("축하합니다. 짝짝짝")
# elif score>=80:
#     print("당신의 성적은", score, "입니다. B 학점")
# elif score>=70:
#     print("당신의 성적은", score, "입니다. C 학점")
# elif score>=60:
#     print("당신의 성적은", score, "입니다. D 학점")
# else:
#     print("당신의 성적은", score, "입니다. F 학점")
# print()
print('------ !!문제!! ------')

# 문제1 1,2,3,4,5,6,7, --- 20
for i in range(1,21):
    print(i, end=", ")
print()
# 문제2 홀수만 출력 (if문)
#   반복문을 사용해서 1~20까지 출력
#   만약 홀수라면 출력
for i in range(1,21):        # 1~21범위의 값을 순차적으로 i에 대입해
    if i%2 == 1:             # 만약 i/2의 나머지가 1이면 실행해
        print(i, end=", ")   # i를 출력해
print()
# 문제3 구구단 5단 출력 
# 5 * 1 = 5
# 5 * 2 = ****
# 5 * 3 = 15
for i in range(1,10):           # i를 1번 부터 9까지 돌려
    if i%2 == 0:                # 만약 i/2의 나머지가 0이면 실행
        print("5 x " + str(i) + " = ****")
    else :
        print("5 x " + str(i) + " = " + str(5*i))


