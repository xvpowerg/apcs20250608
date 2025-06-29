class Employee:
    pass

def change(emp,name,salary):
    emp.name = name
    emp.salary = salary

emp = Employee()

emp.name = "Sean"
emp.salary = 50000
print("Name:",emp.name)
print("Salary:",emp.salary)
emp2 = Employee()
emp2.name = "David"
emp2.salary = 60000
print("Name:",emp2.name)
print("Salary:",emp2.salary)
change(emp2,"Iris",25000)
print("Name:",emp2.name)
print("Salary:",emp2.salary)
