def personInfo(name,age,**other):
    print("name:",name)
    print("age:",age)
    for key in other:
        print(key,":",other[key])
        
personInfo("Sean",40)
personInfo("David",35,phone="0988117556",company="IBM")
