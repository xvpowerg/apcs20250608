## 列出輸入整數的所有質因數
num = int(input("輸入整數"))
print(num,"的質因數:",end=" ")
myList = []
for i in range(2,num+1):
    if num % i != 0:
        continue
    myList.append(i)


for vNum in myList:
    isPrimeNum = True
    for i in range(2,vNum):
        if vNum % i == 0:
            isPrimeNum = False
            break
    if  isPrimeNum :
        print(vNum,end=" ")        
