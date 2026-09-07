print()

print("=======✨WELCOME TO UROOJ'S FOOD HOUSE!✨========\n")

print()

# MENU SELECTION
while True:

    print("Please select your type of Menu: Veg? Non veg? or Mixed?😋\n")

    m = input("Enter your type of menu please: ").lower()

    if m == "veg":

        print()

        print("Welcome to the veg food house! We have:\n"
              "1. Masala Dosa - 30 riyals\n"
              "2. Margherita Pizza - 35 riyals\n"
              "3. Vegetable Spring Rolls - 30 riyals\n"
              "4. Falafel Wrap - 32 riyals\n"
              "5. Paneer Tikka - 38 riyals\n"
              "6. Veggie Tacos - 35 riyals\n"
              "7. Mushroom Pasta - 40 riyals\n"
              "8. Vegetable Sushi - 42 riyals\n"
              "9. Hummus & Pita - 30 riyals\n"
              "10. Veggie Burger - 38 riyals\n"
              "11. Greek Salad - 30 riyals\n"
              "12. Aloo Paratha - 30 riyals\n"
              "13. Vegetable Fried Rice - 35 riyals\n"
              "14. Ratatouille - 40 riyals\n"
              "15. Cheese Quesadilla - 35 riyals")

        print()
        break

    elif m == "non veg":

        print()

        print("Welcome to the non veg food house! We have:\n"
              "1. Chicken Biryani - 40 riyals\n"
              "2. Chicken Shawarma - 35 riyals\n"
              "3. Chicken Tikka - 40 riyals\n"
              "4. Beef Burger - 42 riyals\n"
              "5. Chicken Kebab - 38 riyals\n"
              "6. Seekh Kebab - 40 riyals\n"
              "7. Mutton Kebab - 45 riyals\n"
              "8. Tandoori Chicken - 42 riyals\n"
              "9. Chicken Teriyaki - 40 riyals\n"
              "10. Fish & Chips - 43 riyals\n"
              "11. Chicken Alfredo - 42 riyals\n"
              "12. Korean Fried Chicken - 40 riyals\n"
              "13. Mutton Rogan Gosh - 45 riyals\n"
              "14. Fish Tacos - 40 riyals\n"
              "15. Chicken Satay - 38 riyals")

        print()
        break

    elif m == "mixed":

        print()

        print("Welcome to the mixed food house! We have:\n"
              "1. Mixed Grill Platter - 45 riyals\n"
              "2. BBQ Platter - 45 riyals\n"
              "3. Sushi Combo - 42 riyals\n"
              "4. Taco Platter - 40 riyals\n"
              "5. Pizza & Wings Combo - 45 riyals\n"
              "6. Shawarma Platter - 42 riyals\n"
              "7. Kebab Platter - 45 riyals\n"
              "8. Pasta Combo - 40 riyals\n"
              "9. Rice Bowl Combo - 35 riyals\n"
              "10. Sandwich Platter - 38 riyals\n"
              "11. Breakfast Platter - 40 riyals\n"
              "12. Mediterranean Mezze Platter - 42 riyals\n"
              "13. Asian Noodle Combo - 38 riyals\n"
              "14. Curry & Naan Combo - 40 riyals\n"
              "15. International Food Platter - 45 riyals")

        print()
        break

    else:

        print()
        print("Oops..not found! Try again :)")
        print()


print("Great choice! Now what would you like to order maam/sir?😄")
print()

order = input("Enter your order please!💫 : ")

foods = order.split(",")

print()

print("Would that be all sir/maam? Okay... your total bill would be💵:")
print()

# PRICES
veg_prices = {

    "Masala Dosa": 30,
    "Margherita Pizza": 35,
    "Vegetable Spring Rolls": 30,
    "Falafel Wrap": 32,
    "Paneer Tikka": 38,
    "Veggie Tacos": 35,
    "Mushroom Pasta": 40,
    "Vegetable Sushi": 42,
    "Hummus & Pita": 30,
    "Veggie Burger": 38,
    "Greek Salad": 30,
    "Aloo Paratha": 30,
    "Vegetable Fried Rice": 35,
    "Ratatouille": 40,
    "Cheese Quesadilla": 35

}


nonveg_prices = {

    "Chicken Biryani": 40,
    "Chicken Shawarma": 35,
    "Chicken Tikka": 40,
    "Beef Burger": 42,
    "Chicken Kebab": 38,
    "Seekh Kebab": 40,
    "Mutton Kebab": 45,
    "Tandoori Chicken": 42,
    "Chicken Teriyaki": 40,
    "Fish & Chips": 43,
    "Chicken Alfredo": 42,
    "Korean Fried Chicken": 40,
    "Mutton Rogan Gosh": 45,
    "Fish Tacos": 40,
    "Chicken Satay": 38

}


mixed_prices = {

    "Mixed Grill Platter": 45,
    "BBQ Platter": 45,
    "Sushi Combo": 42,
    "Taco Platter": 40,
    "Pizza & Wings Combo": 45,
    "Shawarma Platter": 42,
    "Kebab Platter": 45,
    "Pasta Combo": 40,
    "Rice Bowl Combo": 35,
    "Sandwich Platter": 38,
    "Breakfast Platter": 40,
    "Mediterranean Mezze Platter": 42,
    "Asian Noodle Combo": 38,
    "Curry & Naan Combo": 40,
    "International Food Platter": 45

}

print()

total = 0

# ORDER CALCULATION
for food in foods:

    food = food.strip().title()

    if food in veg_prices:

        price = veg_prices[food]

    elif food in nonveg_prices:

        price = nonveg_prices[food]

    elif food in mixed_prices:

        price = mixed_prices[food]

    else:

        print(food, "- Sorry, this item was not found!")
        continue

    print(food, "-", price, "riyals")

    total = total + price


print("Total:", total, "riyals")

print()

print("Thank you very much for ordering at Urooj's Food House!🎀")

print("Your order will be coming up soon!")

print()