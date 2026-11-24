class Person(object):
    def __init__(self,name,idnumber):
        self.name= name
        self.idnumber = idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)
class Employee(Person):
    def __init__(self, name, idnumber,salary,post):
        self.salary = salary
        self.post = post 

        Person.__init__(self, name,idnumber)
    def vew(self):
        print(self.salary , self.post , self.name , self.idnumber)
        print()

obj = Employee("Urooj",183126,"25,000 Riyals","Assistant Manager")
obj.vew()

       