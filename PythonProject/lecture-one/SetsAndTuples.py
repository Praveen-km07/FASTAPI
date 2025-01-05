"""
Sets are similar to lists but unordered and cannot contain duplicates.
Use curly brackets
"""
my_set ={1,2,3,4,5,1,2}
print(my_set)
print(len(my_set))

for x in my_set:
    print(x)

my_set.discard(3)
print(my_set)
my_set.add(6)
print(my_set)
my_set.union([7,8])
print(my_set)


#Tuples
my_tuples = (6,7,8,9,10)
print(my_tuples)
print(len(my_tuples))
print(my_tuples[1])
