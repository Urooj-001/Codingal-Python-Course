# M2 L1 ACP
# The Movie Ticket Pricing System
print()
print("WELCOME TO OUR CINEMA! We know you are excited but lets check if your eligiable and lets check the ticket price!")
print()
age = int(input("Enter you age please:"))
print()
if age < 12:
    holiday = input("Is it a holiday for u? (yes/no):").lower()
    print()
    if holiday == "yes":
        print("Your ticket costs 5 riyals and you get a speical festive coupon! WoOHOO.")
    elif holiday == "no":
        print("Your ticket costs 5 riyals.")
elif age >= 12 and age <= 64:
    student_id = input("Are you a student?(yes/no): ").lower()
    print()
    if student_id == "yes":
        print("You get a discount yay! Study hard okay? Your ticket costs 8 riyals!")
    elif student_id == "no":
        print("Your ticket costs 12 riyals!")
elif age >= 65:
    holiday_2 = input("Do you have a holiday?(yes/no:)").lower()
    print()
    if holiday_2 == "yes":
        print("You get an extra senior holiday discount! Your ticket costs 5 riyals! Enjoy.")
    elif holiday_2 == "no":
        print("Your ticket costs 7 riyals , enjoy!")
else:
    print("Oh i see.")
# Objective: Write a Python program that determines the ticket price and eligibility for a cinema
# based on a customer's age, whether they have a student ID, and whether it is a holiday.
# Rules for pricing:
# Children (Under 12): Ticket is $5.
# If it is a holiday, they get a special festive treat coupon!
# Adults (12 to 64): Standard ticket is $12.
# If they are a student (have a student ID), they get a discount: Ticket is $8.
# Seniors (65 and older): Ticket is $7.
# If it is a holiday, they get an extra senior holiday discount: Ticket is $5.