# 練習：字串練習
## 檢查使用者輸入的字串是否為迴文
##ABA 是迴文 顯示True
##VCB 不是 顯示False
inStr = input("輸入字串:")
reStr = inStr[::-1]
print(inStr == reStr)
