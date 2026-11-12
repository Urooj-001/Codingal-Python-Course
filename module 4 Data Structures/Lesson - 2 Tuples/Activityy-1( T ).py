# 1) Create a tuple `tuplex` containing different data types (string, boolean, float, integer)
tuplex = ('HELLO' , True , 89.9 , 60 )
# and print the tuple.
print(tuplex)
# 2) Create another tuple `tuplex` containing only integer values and print it.
tuplex = (4 , 23, 18)
print(tuplex)
# 3) Demonstrate tuple immutability:
# a) Tuples cannot be modified directly (cannot add/change elements in the same tuple).

#tuplex[1]=56

# b) Use the `+` operator to merge tuples and create a new tuple.
tuplex = (4 , 23, 18) + ('HELLO' , True , 89.9 , 60 )
print(tuplex)
# c) Add a single element (9) using `(9,)` and store the new tuple back in `tuplex`.
# d) Print the updated tuple.
# 4) Create a tuple `tuple1` and count occurrences of a specific value:
tuple1= (4,5,6,7,50,9,55,50)
# a) Use `tuple1.count(50)` to count how many times 50 appears.
print(tuple1.count(50))
# b) Print the count.
# 5) Create a tuple `tuplex` with multiple integers to demonstrate slicing.
tuplex = (4,89,6,23,45,1,2)
# 6) Slice a portion of the tuple using indexing:
print(tuplex[3:5])
# a) Use `tuplex[3:5]` to get elements from index 3 up to index 4 (stop index is excluded).
# b) Store it in `_slice` and print it.
_slice = tuplex[3:5]
print(_slice)
# 7) Slice from the beginning when the start index is not provided:
_slice= tuplex[:6]
print(_slice)
# a) Use `tuplex[:6]` to get elements from index 0 up to index 5.

# b) Store it in `_slice` and print it.