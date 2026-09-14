# ================================
# SWIMMING POOL ENTRY CHECKER
# ================================

# print("=== Swimming Pool Entry Checker ===")
# print("Answer 3 questions and I will tell you which pool you can use.\n")
print()
print ("---------------✨Swimming Pool Entry Checker!!✨----------------------")
print()
print ("Weclome! I know your excited for swimming, but you have to answer 3 important questions! Then i'll tell you which pool you are eligiable to use.")
# ---------- collect the three answers ----------
# YOUR CODE HERE
print()
age = int(input("Enter your age please!:"))
print()
can_swim = input("Can you swim 25 metres? (yes/no):")
print(can_swim.lower())
print()
adult = input("Is an adult here with you?(yes/no):")
print(adult.lower())
print()
print ("----Entry decision----")
print()
# ---------- PART 1: age group, using if / elif / else on a NUMBER ----------
if age <= 4:
    print("You fall in the toddler category! Welcome, you can only splash water , you should always be with an adult!")
elif age <= 12: 
    print("You fall in the child category! Welcome, you can swim in the main pool but with an adult!")
elif age <= 18:
    print("Alright, you fall in the teen category! Welcome, you can use the main pool alone!")
else:
    print("Well you are an adult! Welcome, all pools are open to you!")
print()
# ---------- PART 2: did they actually answer yes or no? ----------
# YOUR CODE HERE

# For can_swim: if it is not "yes" AND not "no", print an input error
#   and set  swim_known = False.  Otherwise set  swim_known = True.
# Do the same for adult_here, setting  adult_known.


# ---------- PART 3: AND - the deep pool ----------
# YOUR CODE HERE
# Allowed only when they CAN swim AND an adult IS present.


# ---------- PART 4: OR - the shallow end ----------
# YOUR CODE HERE
# Warn when they are under 12 OR they cannot swim.


# ---------- PART 5: NOT - the lifeguard reminder ----------
# YOUR CODE HERE
# Remind when there is no adult — but only if adult_known is True.
# Think about why that extra check is needed before you write it.


# ---------- PART 6: the final verdict ----------
# YOUR CODE HERE
# First: if either answer was not understood, refuse to decide.
# Then work through the real cases with elif, ending in a plain else.


# print()
# print("Have a safe swim!")