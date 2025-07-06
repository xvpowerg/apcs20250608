myList = [8,9,7]
num1 = 10
num2 = 0

try:
    print(myList[8])
    print(num1 / num2)
except IndexError:
    print("list index 錯誤發生")
except ZeroDivisionError:
    print("分母不可為0 錯誤發生")
