"""
Based on the dictionary:
  my_vehicle ={
    "model":"Ford",
    "year":1978,
    "make":"Ashley",
    "mileage":8000,
  }
  -Create a for loop to print all keys and values
  -Create a new variable vehicle2,which is a copy of my_vehicle
  -Add a new key 'number_of_tires' to the vehicle2 variables that is equal to 4
  -delete the mileage key and value from vehicle2
  -Print just the keys from vehicle2
"""

my_vehicle ={
    "model":"Ford",
    "year":1978,
    "make":"Ashley",
    "mileage":8000,
  }

for x,y in my_vehicle.items():
    print(x,y)

vehicle2 = my_vehicle.copy()
print(vehicle2)
vehicle2['number_of_tires'] = 4
print(vehicle2)
vehicle2.pop('mileage')
print(vehicle2)

for x in vehicle2:
    print(x)