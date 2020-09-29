print('------- 문제2 -------')
# 사용자로 부터 국어, 영어, 수학 점수를 한꺼번에 입력받아
# 각 점수의 합계와 평균을 구하고
# 평균 점수에 따라 A, B, C 학점을 출력한다

kor, eng, mat = input("국어, 영어, 수학 점수를 띄어써서 입력").split()
kor = int(kor)
eng = int(eng)
mat = int(mat)
sum = kor + eng + mat
avg = int(sum/3)
print("sum:", sum, "avg:", avg)
if avg>=90:
    print("A학점")
elif 80<=avg<90:
    print("B학점")
elif 70<=avg<80:
    print("C학점")
elif 60<=avg<80:
    print("D학점")
else:
    print("F학점")