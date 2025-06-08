name = "小民"
age = 12
# 小民今年12歲
# 1 msg
msg =name+"今年"+str(age)+"歲"
print(msg)
# 2 print() print()
print(name,end="")
print("今年",end="")
print(age,end="")
print("歲")
print(name,"今年",age,"歲",sep="")

#%d 整數 %f 浮點數 %s字串
msg = "%s今年%d歲"%(name,age)
print(msg)
#f-string
msg = f"{name}今年{age}歲"
print(msg)

