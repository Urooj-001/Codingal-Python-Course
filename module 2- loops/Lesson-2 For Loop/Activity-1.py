#To find the sum of the first n natural numbers.

n = int(input("Enter the number till which you want the sum:"))
sum = 0
for i in range(1,n+1):
    sum = sum+i
print(sum)