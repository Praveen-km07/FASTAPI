"""
Lists are a collection of data
"""

my_list=[80,96,72,100,8]
print(my_list)
my_list.append(1000)
print(my_list)
my_list.insert(1,110)
print(my_list)
my_list.remove(80)
print(my_list)
my_list.pop(0)
print(my_list)
my_list.sort()
print(my_list)

people_list=["Praveen","anjana","test"]
people_list[2] ="Udemy"
print(len(people_list))
print(people_list[-1])

#slicing
print(people_list[1:2])