test_dict = {'codingal': 2 , "is":3 , "best": 4, "coding" : 1}
print("The original dictonary:" + str(test_dict))
k=4 #just initialzing the value
res = 0
for key in test_dict:
    if test_dict[key]==k:
        res+=1
print("The frequency of k :" + str(res))