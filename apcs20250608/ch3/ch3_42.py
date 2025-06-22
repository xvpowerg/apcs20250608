myFunc = lambda x,p=2:x**p
list1 = [1,2,3,4,5]
newList = []#內容是list1的2次方數 1 4 9 16 25
for i in list1:
    newList.append(myFunc(i,3))
print(newList)    
