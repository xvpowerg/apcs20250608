num1 = 10
num2 = 0
nums = [1,3,5,7,9]
try:
 #print(num1 / num2)
  #print(nums[0])
    print(nums[9])
except ZeroDivisionError:
    print("分母不可為0")
else:
    print("沒有錯誤")
finally:
    print("一定跑一次")
    
