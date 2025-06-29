## 英文字母接龍
str_result = input("請輸入接龍字串:")
eCount = 0
while eCount < 5:
    print(f"目前的字串{str_result}")
    str_in = input(f"請輸入{str_result[-1]}開始的字串")
    if str_result[-1] ==  str_in[0]:
        str_result += "-"+str_in
    else:
        eCount += 1
        print(f"錯誤次數:{eCount}")
print("遊戲結束!")
