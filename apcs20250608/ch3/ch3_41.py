def myPow(v,p=2):
    return v ** p
list1 = [1,2,3,4,5]
newList = []#內容是list1的2次方數 1 4 9 16 25
for i in list1:
    newList.append(myPow(i,3))
print(newList)    
