import random
answer = random.randint(1,10)
for i in range(5):
    guess = int(input("猜一個數字:"))
    if guess == answer:
        print("猜對了")
        break
else:
    print("答案是",answer)
print("完成")        
