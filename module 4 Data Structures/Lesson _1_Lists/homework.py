start = int(input("Enter the beginning of the range: "))
end = int(input("Enter the ending of the range: "))
squares = []
for i in range(start, end + 1):
    squares.append(i ** 2)
odd_squares = []
even_squares = []
for num in squares:
    if num % 2 == 0:
        even_squares.append(num)
    else:
        odd_squares.append(num)

print("The square values are:", squares)
print("Even square numbers are:", even_squares)
print("Odd square numbers are:", odd_squares)
