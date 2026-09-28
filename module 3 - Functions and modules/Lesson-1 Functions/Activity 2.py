def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y



num1 = float(input("Enter your first number:"))
num2 = float(input("Enter your second number:"))
op = input("Select one of these: + , - , * , /: ")

if op == '+':
    res=add(num1 , num2)
elif op == '-':
    res=sub(num1 , num2)
elif op == '*':
    res=multiply(num1, num2)
elif op == '/':
    res=divide(num1, num2)
print(f"The result of of these numbers are {res}")

