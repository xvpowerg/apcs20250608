class Employee:
    def __init__(self,name,salary=20000):
        self.name = name
        self.salary = salary
    def printInfo(self,title):
        print(title)
        print("name",self.name)
        print("salary",self.salary)
emp1 = Employee("Sean",50000)
emp1.printInfo("員工資訊1")
emp2 = Employee("Lucy")
emp2.printInfo("員工資訊2")
    
