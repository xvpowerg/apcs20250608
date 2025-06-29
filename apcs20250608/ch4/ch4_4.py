list1 = [1,2,3,5,8,13,21,34,55,89]
def test(n):
    return n % 2 == 0

print(list1)
for i in list1:
    if test(i):
        print(i)
