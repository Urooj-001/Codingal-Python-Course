n = int(input("Enter a range till where you want to: "))

odd_numbers = [i for i in range(n) if i % 2 != 0]

print("Odd numbers:", odd_numbers)

fruits = ["apple", "banana", "mango", "orange", "grapes"]

new_list = [i.capitalize() for i in fruits]

print(new_list)