def checkScore(s):
     if s >= 0 and s <= 59:
        print("不及格")
     elif s >= 60 and s <=100:
        print("及格")
     else:
         raise OverflowError
         #print("錯誤")
    #是否及格0~59不及格
    #60~100及格
    #其他錯誤
score = int(input("輸入成績"))
print("Start")
try:
    checkScore(score)
except  OverflowError:   
    print("錯誤的成績")
print("End")
