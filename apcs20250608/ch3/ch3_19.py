## for-else結構改寫計算所輸入的數是否為質數程式
num = int(input("輸入整數"))

for i in range(2,num):
    if num % i == 0:
        print(num,"不是質數")
        break
else:
    print("是質數")
