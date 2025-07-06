class Student:
    def __init__(self,name,score=0):
        self.name = name
        self.score = score
        
st1 = Student("Ken",95)

st2 = Student("Vivin")

print(st1.name,st1.score)
print(st2.name,st2.score)
