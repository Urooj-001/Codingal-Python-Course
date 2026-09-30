# name = input("Enter your name: ")
# for i in name:
#     if i == "O":
#         print("O is found in your name.")
#         break
#     else:
#         print("O not found in your name.")


# for i in range(1,51):
#     if i % 3 == 0:
#         continue
#     print(i)


while True:                                   #works for infinite
    pin = input("Enter your pin: ")
    if len(pin) != 4:
        print("Error: Please enter a 4 digit code.")
        continue
    print("Valid pin.")
    break