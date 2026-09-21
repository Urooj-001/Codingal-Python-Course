emoji = "🦋"
print(emoji)
rows = int(input("How many rows do you want?:"))
columns = int(input("How many columns do you want?:"))
for i in range(rows):
    for j in range(columns):
        print(emoji, end=" ")
    print()
    