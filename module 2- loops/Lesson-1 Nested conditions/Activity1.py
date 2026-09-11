# ACTIVITY 1: STUDENT CAN TAKE EXAM UNDER TWO CONDITIONS:
# Take the required input for attendance
attendance = float ( input ("Enter the attendance:"))
# - Student should have attendance >= 75%
# - Check if attendance matches above criteria
if attendance >= 75:
    print("You are allowed to take the exam.")
# - Then Print "Allowed"
# - If attendance is low, Student should have a medical certificate
else:
    medical = input("Do you have a medicial certificate(yes/no):").lower()
    if medical == "yes":
        print("You are allowed.")
    else:
        print("You are not allowed.")
# - Take input for medical certificate
# - Check if student replied Yes or No
# - If Yes, Print "Allowed"
# - Else No, Print "Not Allowed"