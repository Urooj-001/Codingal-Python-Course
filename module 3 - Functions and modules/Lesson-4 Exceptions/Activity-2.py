# 1) Start a `try` block to run code that may cause exceptions.
try:
    #a = int(input("Enter 2 numbers: "))
    num1,num2=eval(input("Enter 2 numbers,separated by comma: "))
    res = num1/num2
    print(res)
except ZeroDivisionError:
    print("Division by 0 is error.")
except SyntaxError:
    print("Please put the correct format-spearate it by comma.")
except:
    print("Wrong input.")
else:
    print("The result is",res,"and no exception has happened.")
finally:
    print("This executes no matter!")

# 2) Take two numbers from the user in a single input, separated by a comma:

# a) Use `eval(input(...))` to read and convert the input.

# b) Store the two values in `num1` and `num2`.

# 3) Perform division:

# a) Compute `result = num1 / num2`.

# b) Print the result.

# 4) Handle possible errors using multiple `except` blocks:

# 5) If a `ZeroDivisionError` occurs (when `num2` is 0),

# print "Division by zero is error !!".

# 6) If a `SyntaxError` occurs (for example, the comma is missing or format is incorrect),

# print a message explaining the correct input format: "1, 2".

# 7) If any other error occurs, use a general `except` block

# and print "Wrong input".

# 8) If no exception occurs in the `try` block, run the `else` block

# and print "No exceptions".

# 9) Run the `finally` block no matter what happens (error or no error),

# and print "This will execute no matter what".