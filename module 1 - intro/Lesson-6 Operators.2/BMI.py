# M1 L6 A1
# 1) Ask the user to enter their height in centimeters and store it in `height`.
height = float(input("Enter your height:"))
# 2) Ask the user to enter their weight in kilograms and store it in `weight`.
weight = float(input("Enter your weight:"))
# 3) Calculate BMI using the formula:
BMI = weight/(height/100)**2
# BMI = weight ÷ (height in meters)²
# Store the result in `BMI`.
print ("Your BMI is", BMI)
# 4) Print the BMI value.
# 5) Use if–elif–else to decide the BMI category:
if BMI <= 18.4:
    print("Your underweight!")
elif BMI <= 24.9:
    print("Your healthy!")
elif BMI <= 29.9:
    print("Your overweight!")
elif BMI <= 34.9:
    print("Your severly overweight.")
elif BMI <= 39.9:
    print("Your obese.")
else:
    print("Your severly obese.")
# - If BMI is 18.4 or less → print "underweight"

# - Else if BMI is 24.9 or less → print "healthy"

# - Else if BMI is 29.9 or less → print "over weight"

# - Else if BMI is 34.9 or less → print "severely over weight"

# - Else if BMI is 39.9 or less → print "obese"

# - Else → print "severely obese"