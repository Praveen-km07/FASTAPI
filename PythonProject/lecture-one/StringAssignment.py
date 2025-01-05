"""
-Ask the user how many days until their birthday
-Using the print() function.print an approx number of weeks until their birthday
-1 week is = to 7 days
"""
days_left_for_birthday =int(input("How many days until their birthday?"))

week_containing_days = 7
print(round(days_left_for_birthday/week_containing_days,2))