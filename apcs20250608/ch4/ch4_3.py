list2 = ["a","b","c","d"]

def myUpper(x):
    return x.upper()

newList1 = list(map(lambda x:x.upper(),list2))
newList2 = list(map(myUpper,list2))
print(newList1)
print(newList2)
