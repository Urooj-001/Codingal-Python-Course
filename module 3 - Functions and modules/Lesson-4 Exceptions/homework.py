try:
    age = int(input("Enter your age: "))

    if age <= 0:
        print("Invalid age! Age must be positive.")
    else:
        print("Age is valid.")

        if age % 2 == 0:
            print("The age is even.")
        else:
            print("The age is odd.")

except ValueError:
    print("Wrong value! Please enter a number.")
