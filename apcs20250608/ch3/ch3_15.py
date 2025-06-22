## 檢查所輸入的數是否為質數
num = int(input("輸入整數"))
isPeimeNum = True
for i in range(2,num):
    if num % i == 0:
        isPeimeNum = False
        break
    
if isPeimeNum:
    print("是質數")
else:
    print("不是質數")
