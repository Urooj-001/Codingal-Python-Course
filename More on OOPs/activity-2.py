class Employee():
    def __init__(self):
        print("Employee created.")
    def __delete__(self):
        print("Destructor called.")

def creating_obj():
    obj=Employee()
    print("Making object..")
    return obj
print("Calling creating_obj()...")
obj = creating_obj()
print("Program end.")