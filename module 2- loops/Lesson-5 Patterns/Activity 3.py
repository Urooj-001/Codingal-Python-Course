num = 1
rows = int(input("How many rows do you want?:"))
for r in range(1,rows+1):
    for c in range(1,r+1):
        print(num, end=" ")
        num += 1
    print()