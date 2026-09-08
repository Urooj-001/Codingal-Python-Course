# age=int(input("Enter your age:"))
# if age >= 13 and age<=19:
#     print("Your a teenager.")


# a=0
# b=-15 
# print("bool(a)=",bool(a))  
# print("bool(b)=",bool(b))
# #every int is true other than 0(false)
# if a and b:
#     print("idk")


day = input("Enter the day of the week:")

if day=="friday" or day=="saturday": #use it when u need one condition true.
    print("Its a weekend.")
else:
    print("Its a weekday.")


#example
attendance = int(input("Enter your attendance:"))
medical_certificate = True
if attendance >= 75 or medical_certificate == True :
    print("You can go to other section.")

#NOT- flips the value of boolean. 
lunch_done = False
if not lunch_done:
    print("Please eat your lunch.")