myMax = int(input("請輸入最大範圍"))
num1,num2 = 1,1
myNext = num1 + num2
while myNext < myMax:
    print(f"{myNext}",end=" ")
    num1 = num2
    num2 = myNext
    myNext = num1 + num2
