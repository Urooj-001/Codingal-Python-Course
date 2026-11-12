set_a = {"green", "pink" , "red" , "purple"}
set_b = {"orange", "pink" , "gold" , "purple"}
print(set_a)
print(set_b)
set_c = set_a.intersection(set_b)
set_d = set_a.symmetric_difference(set_b)
set_e = set_b.union(set_a)
set_f = set_a.difference(set_b)
print("The intersection of these two sets are", set_c )
print("The common element removed in these two sets , so the set is ", set_d )
print("The union of these sets are", set_e )
print("The difference of set a is " , set_f )
