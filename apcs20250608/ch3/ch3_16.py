## 列出輸入整數的所有因數
num = int(input("輸入整數"))
print(num,"的因數:",end=" ")
myList = []
for i in range(1,num+1):
    if num % i != 0:
        continue
    print(i,end=" ")

