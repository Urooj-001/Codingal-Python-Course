s1 = {4,6,8}
s2 = {5,7,9}
s3 = list(zip(s1,s2))
print(s3,"\n")

lst1 = [1,2,3,4]
lst2 = [5,6,7,8]
for x,y in zip(lst1,lst2[: : -1]):
    print(x , y)

abcd = ["hello" , "computer" , "coding"]
efgh = ["Byee" , "urooj" , "easy"]
new_dict = {abcd : efgh for abcd,efgh in zip(abcd,efgh) }
print("\n{}".format(new_dict))
