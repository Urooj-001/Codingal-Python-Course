#DOCSTRING- document string

def sum(a,b):
    """What does the function do?
    prints a+b"""

    print(a + b)

print(sum.__doc__)

def greet(name,greeting="Hello"):
    print(f"{greeting} {name}")

greet("Urooj","Good Morning")  #give the arguments in order
