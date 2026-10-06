try:
    a=int(input("Enter a number: "))
    print(a)
except ValueError as ex:
    print("You have put an string.")
    print("Exception= ",ex)