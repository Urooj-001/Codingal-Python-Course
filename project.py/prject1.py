# ================================
# FUNCTION CALCULATOR
# ================================

# ---------- PART 1: four functions ----------
# YOUR CODE HERE
# Write add(a, b), subtract(a, b), multiply(a, b) and divide(a, b).
# Each one should return its answer. Do not print inside the functions.

# ---------- MAIN PROGRAM (given to you) ----------


# ---------- PART 2, 3 and 4: input, choose, errors ----------
# YOUR CODE HERE
# Put everything below inside a try block:
#   Ask for the first number and the second number. Turn each into a number with float().
#   Ask for the operation: add, subtract, multiply or divide.
#   Use if / elif / else to call the right function and print the result.
#   For any other word, print "Unknown operation."
# Then add:
#   except ValueError: for letters instead of numbers
#   except ZeroDivisionError: for dividing by zero
#   finally: print a thank-you line

#my program-


print()
print("WELCOME TO THE CALCULATOR BUILT BY UROOJ!!!")
print("Am still learning so the only math operations you can use are addition, subraction , multiplication and division!")
print()

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b



try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    operation = input("Choose an operation (add, subtract, multiply, divide): ").lower()

    if operation == "add":
        print("Result:", add(num1, num2))

    elif operation == "subtract":
        print("Result:", subtract(num1, num2))

    elif operation == "multiply":
        print("Result:", multiply(num1, num2))

    elif operation == "divide":
        print("Result:", divide(num1, num2))

    else:
        print("Unknown operation.")

except ValueError:
    print("Error: Please enter valid numbers.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

finally:
    print("Thank you for using the Function Calculator!")
