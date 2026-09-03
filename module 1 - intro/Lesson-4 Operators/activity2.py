#  M1 L4 A3
# 1) Ask the user to enter marks for 4 subjects: math, english, science, and hindi.
mark1 = int(input("Enter your marks:"))
mark2 = int(input("Enter your marks:"))
mark3 = int(input("Enter your marks:"))
mark4 = int(input("Enter your marks:"))
# Store each mark in its own variable.

# 2) Add all 4 subject marks and store the total in `sum`.
sum = mark1 + mark2 + mark3 + mark4
# 3) Print the total marks stored in `sum`.
print(sum)
# 4) Calculate the percentage:
perc=sum/400*100
print(perc)
# - Divide `sum` by 400 (total maximum marks for 4 subjects, assuming each is out of 100)

# - Multiply the result by 100

# Store the final value in `perc`.

# 5) Print the percentage stored in `perc`.                