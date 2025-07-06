class Point:
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y
    def prinInfo(self):
        print(self.x,self.y)
    def __del__(self):
        print("del:",self.x,self.y)
pt1 = Point()
pt2 = Point(2,3)
print(pt1.x,pt1.y)
print(pt2.x,pt2.y)

del pt1#刪除了pt1
print(pt1.x,pt1.y)
