rows = int(input("How many rows do you want?: "))

for r in range(1, rows+1):
    for s in range(rows-r):
        print("  ", end="")

    for c in range(1, r+1):
        print(c, end=" ")

    print()