num1 = [2,4,6]
num2 = [1,3,5]
print(num1)
print(num2)
result = map (lambda x,y : x + y , num1 , num2 )
print ("Addition of two lists")
print(list(result))

 #using map
nums = [5,6,7,8]
print(nums)
def square(n):
    return n*n
square = list(map(square , nums ))
print("The square of the numbers are")
print(nums)