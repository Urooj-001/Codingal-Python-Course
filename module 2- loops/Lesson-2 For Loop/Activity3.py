#Reverse a string using for loop.

name = input("Enter a word you want to see in reverse:")
reverse = ""
for c in name:
    reverse = c + reverse
print(reverse)