class Person:
    def __init__(self,name):
        self.name = name
    def sayHello(self):
        print("Hello",self.name)

p1 = Person("Ken")        
p1.sayHello()

p2 = Person("Lucy")
Person.sayHello(p2)
