r=int(input("Enter your radius:"))
print()
print("What would u like to find? \n 1.Area \n 2.Perimeter")
print()
choice = int(input("Enter a choice (1/2):"))
if choice == 1:
    Area = 3.14 * r ** 2
    print("Area is", Area)
elif choice == 2:
    Perimeter = 2 * 3.14 * r
    print("Perimeter is", Perimeter )
else:
    print("Not found.")