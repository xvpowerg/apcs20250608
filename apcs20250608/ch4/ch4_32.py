class Employee:
    def __init__(self,name,salary = 25000):
        self.name = name
        self.salary = salary

emp = Employee("Sean",50000)
print("Name:",emp.name)
print("Salary:",emp.salary)
emp2 = Employee("Ken")
print("Name:",emp2.name)
print("Salary:",emp2.salary)
