class Student:
    def __init__(self,name,score):
        self.name = name
        self.scores = list(map(int,score.split(",")))
        self.scores.sort()
    def getMax(self):
        return self.scores[-1]
    def getSum(self):
        mySum = 0
        for s in self.scores:
            mySum += s
        return mySum
    def __str__(self):
        return f"{self.name}-{self.scores}"

mydata = open("mydata.txt")
line = mydata.readline()
studenList = []
while line:
    data = line.split(":")
    name = data[0]
    score = data[1]
    sr1 = Student(name,score)
    studenList.append(sr1)
    print(sr1,end="")
    #print(name,score,end="")
    line  = mydata.readline()
 

for st in studenList:
    print(st.name,st.getMax(),st.getSum())

#每一筆資料建立一個Student
#每個Student可以存放 姓名 成績
#方法可取得每位學生最高成績分數
#方法所有成績總和
