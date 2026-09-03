# M1 L4 A2
# 1) Take the total withdrawal amount as input from the user and store it in `Amount`.
amount = int(input("Enter your amount:"))
# 2) Find how many 100-rupee notes are needed:
note_500 = amount // 500
# Divide `Amount` by 100 (whole number division) and store it in `note_1`.

# 3) Find the remaining amount after taking out 100-rupee notes:
r_a = amount % 500
# Use the remainder of `Amount` after dividing by 100.
note_200 = r_a // 200
r_a = r_a % 200
# 4) From the remaining amount, find how many 50-rupee notes are needed:
note_100 = r_a // 100
r_a = r_a % 100
# Divide the remainder by 50 (whole number division) and store it in `note_2`.
note_50 = r_a // 50
r_a = r_a % 50
# 5) Find the remaining amount after taking out 50-rupee notes:
note_20 = r_a // 20
r_a = r_a % 20
note_10=r_a // 10
r_a= r_a % 10
# Use the remainder after dividing by 50.
print ("500 riyals=",note_500)
print ("200 riyals=",note_200)
print ("100 riyals=",note_100)
print ("50 riyals=",note_50)
print ("20 riyals=",note_20)
print ("10 riyals=",note_10)



# 6) From the remaining amount, find how many 10-rupee notes are needed:

# Divide the remainder by 10 (whole number division) and store it in `note_3`.

# 7) Print the number of 100-rupee notes, 50-rupee notes, and 10-rupee notes.