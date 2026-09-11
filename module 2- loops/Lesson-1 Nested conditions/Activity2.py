# M2 L1 A2
# ACTIVITY 3 - CUSTOMIZE YOUR FOOD DELIVERY ORDER
# 1) Display a menu asking the user to select a food category:
print("This is the menu: \n 1.Biryani \n 2.Pizza")
choice = int(input("Enter your choice (1 / 2):"))
if choice == 1:
    print("Great, \n 1.Veg \n 2.Chicken")
    choice2 = int(input("Enter your choice (1 / 2):"))
    if choice2 == 1:
        print("Your veg biryani is on the way!")
    elif choice2 == 2:
        print("Your chicken biryani is on the way!")
    else:
        print("Not found in our menu.")
elif choice == 2:
    print("Great, \n 1.Paneer \n 2.Chicken")
    choice3 = int(input("Enter your choice (1 / 2):"))
    if choice3 == 1:
        print("Your Paneer pizza is o the way.")
    elif choice3 == 2:
        print("Your chicken pizza is on the way!")
    else:
        print("Not found in our menu")
else:
    print("Oops, not found in our menu!")
# - 1 for Biryani

# - 2 for Pizza

# 2) Take the user’s input and store it in `choice`.

# 3) If `choice` is 1 (Biryani):

# a) Show Biryani options (Veg / Chicken)

# b) Take the user’s input for Biryani type and store it in `choice2`

# c) If `choice2` is 1, print "Your order is on the way: Veg Biryani"

# Else, print "Your order is on the way: Chicken Biryani"

# 4) Else if `choice` is 2 (Pizza):

# a) Show pizza options (Paneer / Chicken)

# b) Take the user’s input for pizza type and store it in `choice3`

# c) If `choice3` is 1, print "Your order is on the way: Paneer Pizza"

# Else, print "Your order is on the way: Chicken Pizza"

# 5) Else (if `choice` is not 1 or 2):

# Print "Wrong choice!"