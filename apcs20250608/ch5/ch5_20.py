class MyException(Exception):
    pass

def test(a):
    if a < 20:
        raise MyException
    print(a)
    
test(30)
test(10)
