# Take a variable num and assign any positive number to it
num = int(input("Enter a number to convert it into a binary digit: "))
binary_digits = ""
# Run while loop - as long as n does not go below 0
n= num
while n>0:
    remainder = n % 2
    binary_digits = binary_digits + str(remainder)
    n = n//2
binary_digits = binary_digits[ : : -1]
print("The binary number for", num, "is", binary_digits)




