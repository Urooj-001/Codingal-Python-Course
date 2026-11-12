#array- collection of items stored in contiguous memory spaces is referred to as an array.
#insert- first the index value then the value u wanna give (index,value)
#append-adds the element in the end js give the value

import array as arr 
ar1 = arr.array("i" , [4,3,2,6] )
print("Original array: "+ str(ar1))

#counting the no of occurances-
print("The no of times 3 has appeared in ar1 ", str(ar1.count(3)))

#reversing-
ar1.reverse()
print("The reverse of this array is ", str(ar1))