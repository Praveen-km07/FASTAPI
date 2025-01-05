"""
For and While Loops
"""
my_list = [1,2,3,4,5,6,7,8,9]
# for item in my_list:
#     print(item)

for x in range(3,6):
    print(x)


sum_of_for_loop = 0
for y in my_list:
    sum_of_for_loop += y
print(sum_of_for_loop)

week =['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
for week in week:
    print(f"Happy {week}!")

i=0
while i <5:
    i +=1
    if i==3:
        continue
    print(i)
    if i==4:
        break
else:
    print("I is now larger or equal to 5")