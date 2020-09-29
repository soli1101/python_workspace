a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")


A = [70,60,55,75,95,90,80,80,85,100]
total = 0
for score in A:
    total += score
average = total/len(A)
print(average)

numbers = [1,2,3,4,5]
result = [i in numbers if i%2==0]
print(result)