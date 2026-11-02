#1) Create a list `L` with some integer values and print it as the original list.
L = [1 , 45 , 23 , 15]
print(L)
# 2) Initialize a variable `count = 0` to store the sum of all elements in the list.
count = 0
# 3) Use a `for` loop to iterate through each element `i` in the list `L`:
for i in L:
    count+= i
avg = count / len(L)
# a) Add each element to `count` using `count += i`.
# 4) Calculate the average of the list:
# a) Divide the total sum `count` by the number of elements `len(L)`.
# b) Store the result in `avg`.
# 5) Print the total sum and the average.
print("The total sum is", count , "and the average is", avg)
# 6) Sort the list `L` in ascending order using `L.sort()`.
L.sort()
# 7) After sorting:
# a) The smallest element will be at index 0 → print `L[0]`.
print("The smallest number is ", L[0])
# b) The largest element will be at the last index → print `L[-1]`.
print("The largest number is ", L[-1])