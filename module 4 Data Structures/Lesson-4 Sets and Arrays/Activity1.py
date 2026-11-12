#for sets, pop remove the first element

#set for integers
my_set = (1,2,3)
print(my_set)

#set can be of diff data types
my_set = (34,"Heyy",78.9,True)
print(my_set)

#set wont print the duplicates
my_set = (5,6,9,5,9)
print(my_set)

#using 'set' function we can convert list into a set
my_set = set([3,4,6])
print(my_set)

#using pop we can remove the first element
set1 = {2,3,4,5}
print("Original list is", set1 )
set1.pop()
print("Using pop function list is", set1 )
