n  = int(input("Enter a number: "))
for i in range(2,n):
    if n % i == 0:
        print("Its not prime.",i,"is the factor.")
        break #breaks the loop when the condition is true
else: #If for loop doesnt break, the else statement will run.
    print("its prime.")

 #Solution 2 -> We could count the factors in the for loop and when the loop ends if the no of factors is 0 its prime no.