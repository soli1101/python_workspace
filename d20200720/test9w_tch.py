print('------- 문제4:자판기 -------')
# -----------------------------------
# 1. 보리차 1800원
# 2. 막걸리 2000원
# 3. 파전   5000원
# 4. 스파게티 4000원
# 5. 산삼   2억원
# 6. 돈가츠 8000원
# -----------------------------------

# 지폐를 넣어주세요 : 50000
# 번호를 선택하세요 : 1
# 수량을 선택하세요 : 2
# 물건값과 입금액을 비교해서 입급액이 많을 때만 상품을 출력
# 맞으면 상품을 내보냈어요 라는 메세지와 함께 잔돈을 출력
#     50000 : 1
#     10000 : 2 이런식으로 출력 
# 부족하면 처음부터 다시하세요라는 메세지와 함께 현금을 반환 

pname = ["보리차","막걸리","파전","스파게티","산삼","돈가츠"]
price = [1800, 2000, 5000, 4000, 200000000, 8000] 

money = int(input("★ 지폐를 넣어주세요: "))
num = int(input("\n1. 보리차 1800원\n2. 막걸리 2000원\n3. 파전   5000원\n4. 스파게티 4000원\n5. 산삼   2억원\n6. 돈가츠 8000원\n\n★ 번호를 선택하세요: "))
qtt = int(input("★ 수량을 선택하세요: "))

total = price[num-1]*qtt
print('--------- 결과 ---------')
if money>total:
    print("♡ 상품을 내보냈어요. 잔돈:", (money-total),
    "오만원:",((money-total)//50000),
    "만원:",(((money-total)%50000)//10000),
    "오천원:",((((money-total)%50000)%10000)//5000),
    "천원:",int((((((money-total)%50000)%10000)%5000)/1000))),
elif money==total:
    print("♡ 상품을 내보냈어요. 잔돈:",(money-total))
else:
    print("▨ 처음부터 다시 하세요! 반환금:",money)

