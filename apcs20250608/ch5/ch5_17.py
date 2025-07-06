num1 = 10
num2 = 0


try:
   print(num1/num2) 
except ZeroDivisionError as ex:
    print("例外類型:",type(ex))
    print("例外訊息:",str(ex))
finally:
    print("完成")
