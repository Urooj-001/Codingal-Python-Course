# M1 L3 A2

# 1) Create variables to store different types of values:
age = 18
# - `age` as a whole number (integer)
print(f"BEFORE : variable age has the value of {age} and type {type(age)}")
# - `weight` as a decimal number (float)
weight = 45.34
# 5) Convert `age` from an integer to a string and store it back in `age`.
print(f"BEFORE : variable weight has the value of {weight} and type {type(weight)}")
age = str(age)
# 6) Print `age` and print its datatype again to confirm it changed.
print(f"AFTER : variable age has the value of {age} and type {type(age)}")
weight=int(weight)
# 7) Convert `weight` from a float to an integer and store it back in `weight`.
print(f"AFTER : variable weight has the value of {weight} and type {type(weight)}")

# 8) Print `weight` and print its datatype again to confirm it changed.
b = False
b = int(b)
print(b)

x = 0.000000000000000000000000000000000000
x = bool(x)
print(x)