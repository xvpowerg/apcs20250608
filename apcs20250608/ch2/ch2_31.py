for i in range(10,0,-2):
    print(i,end=" ")
print()
#5 6 7 8
for i in range(5,9):
    if i < 8:
      print(i,end=" ")
    else:
      print(i)  
print()
str1=""
for i in range(5,9):
    str1 +=f"{i} "
print(str1[:-1])    
