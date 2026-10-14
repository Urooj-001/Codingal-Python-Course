import math
print("What do you wanna find? \n 1.Sin? \n 2.Cos? \n 3.Tan?")
choice = int(input("Enter your choice (1 , 2 or 3): "))
if choice == 1:
    x = int(input("Enter the angle in degrees: "))
    angle1 = math.radians(x)
    print("The sin value of", x, "is", math.sin(angle1))
elif choice == 2:
    y = int(input("Enter the angle in degrees: "))
    angle2 = math.radians(y)
    print("The cos value of", x, "is", math.cos(angle2))
elif choice == 3:
    z = int(input("Enter the angle in degrees: "))
    angle3 = math.radians(z)
    print("The tan value of", z, "is", math.tan(angle3))
else:
    print("Oops not found, sorry!")
    




