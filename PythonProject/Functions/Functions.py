"""
Functions
"""

print("Hello and welcome to functions")

def my_functions():
    print("Inside my_functions")

my_functions()

def print_my_name(name):
    print(f"Hello {name} !")

print_my_name("Jim")

def print_color_red():
    color ="Red"
    print(color)

color ="Blue"
print(color)
print_color_red()

def print_numbers(highest_number,lowest_number):
    print(highest_number,lowest_number)

print_numbers(lowest_number=3,highest_number=10)

def multiply_numbers(number1,number2):
    return number1 * number2
solution =multiply_numbers(3,4)
print(solution)

def print_list(list_of_numbers):
    for number in list_of_numbers:
        print(number)
number_list = [1,2,3,4,5]
print_list(number_list)

def buy_item(cost_of_item):
    return cost_of_item + add_tax_to_item(cost_of_item)

def add_tax_to_item(cost_of_item):
    current_tax_rate =.03
    return cost_of_item  * current_tax_rate

final_cost = buy_item(50)
print(final_cost)