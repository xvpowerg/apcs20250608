
while True:
    try:
        a = input("請輸入數字")
        a = int(a)
    except:    
        print("顯示錯誤的數字:",a)
    else:
        break
#持續輸入直到正確的數字
#如果錯誤顯示錯誤的數字

print(a)
