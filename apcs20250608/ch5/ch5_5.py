class Employee:
    count = 0
    company = "GJ"
    phone = "(02)-2311-4537"
    def __init__(self,name):
        self.name = name
        Employee.count += 1
    def printInfo(self):
        print("員工資訊")
        print("姓名:",self.name)
        print("公司:",Employee.company)
        print("電話:",Employee.phone)
    def getTotal():
       return Employee.count
emp1 = Employee("Ken")
emp2 = Employee("Vivin")
emp3 = Employee("Lucy")
Employee.company = "Google"
emp1.printInfo()
emp2.printInfo()

print("========")
emp1.company = "IBM"
emp1.printInfo()
emp2.printInfo()
print(Employee.getTotal())

