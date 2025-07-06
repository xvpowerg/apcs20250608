myList = [8,9,7]
num1 = 10
num2 = 0
strNumer = "12345"#ValueError
try:
    #print(myList[5]) 
    #print(num1 / num2)
    print(int(strNumer))
except ZeroDivisionError:
    print("分母不可為0")
except (ValueError,IndexError):
    print("ValueError或IndexError的錯誤")
else:
    print("Error沒發生")

