n = int(input("Enter a number and the prgram checks how many digits you have entered: "))
count = 0
while n > 0:
    n = n // 10
    count = count + 1
print("the number of digits you have put is:", count)