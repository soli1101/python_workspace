with open("./d20200727/msg3.txt","r", encoding="utf-8") as file:
    data=file.readlines() # 단어별로 끊어서 가져올 수도 있다
    print(data)
                          
                          # 한줄쓰기!!
lines = ["안녕하세요\n","오늘은 금요일\n","이면 좋겠넹\n"]

with open("./d20200727/msg3.txt", 'w', encoding="utf-8") as file:
    file.writelines(lines)
    # 내용을 한줄로!! 입력시킬 수 있다!!
