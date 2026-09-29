#finding the factorial using a loop - hw

#finding factorial using function

def factorial(x):
    print(f"Im in factorial({x})")
    if x == 1 or x == 0:
      return 1
    return x * factorial(x-1)

num = int(input("Enter a no:"))

print(factorial(num))