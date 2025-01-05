"""
-Given my_list=["Monday","Tuesday","Wednesday","Thursday","Friday"]
-Create a while loop that prints all the elements in my_list variable 3 times
-when printing the elements use a for loop to print the elements
-However if the element of the for loop is equal to monday,continue without printing
"""
my_list=["Monday","Tuesday","Wednesday","Thursday","Friday"]
x=0
while x <3:
    x+=1
    print(my_list)

for days in my_list:

    if("Monday" in days):
        continue
    print(days)