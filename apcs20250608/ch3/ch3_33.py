def sumFunc(*other):
    s = 0
    for i in other:
        s += i
    return s    
print(sumFunc(1))
print(sumFunc(5,6))
print(sumFunc(5,6,9))
print(sumFunc())
