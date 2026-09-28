# #This is a function defination
# def greet():
#     print("Good Evening")
#     #greet()
# #calling a function
# greet()
# when u call a function inside the same function it is known as recursion

#(name,age.xyz) known as argument
def intro(name, age):
    print(f"Hello This is {name} and am {age} years old.")
intro("Urooj",16)




def sqrt(n):
    return n**(1/2)  #returns the value where u called the function


number = int(input("Enter a no:"))
answer = sqrt(number)
print(f"The square root of {number} is = {answer}")