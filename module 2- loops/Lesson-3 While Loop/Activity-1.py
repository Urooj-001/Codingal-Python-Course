n = int(input("Enter the no till which u want the numbers to get added:"))
i = 1
sum = 0
while i <= n:
    sum= sum+i       #ORDER MATTERS.
    i += 1
print("The sum is=",sum)