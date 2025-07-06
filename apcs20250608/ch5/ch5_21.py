class MyBreak(Exception):
      pass
try:
    for i in range(1,5):
        print("i:",i)
        for k in range(1,5):
            print("k:",k)
            if i == 2:
                raise MyBreak
        print("=============")   
except MyBreak:
    pass
   
