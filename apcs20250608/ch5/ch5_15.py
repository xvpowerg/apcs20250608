count = 0
for i in range(1,5):
    print("i:",i)
    for j in range(1,5):
        print("j:",j)
        try:
            for k in range(1,5):
             print("K:",k)
             print("===============")
             count += 1
             if i == 2 and j == 3:
                x = 1/0
                
        except ZeroDivisionError:
             print("ZeroDivisionError")
             break
        finally:#一定會執行一次
            count = 0   
    print("count:",count)                            
