"""
-You have $50
-You buy an item that is $15
-with a tax of 3%
-print how much money you have left
"""

Amount= 50
item_price=15
tax_item = 0.03
remaining_amount = Amount - item_price -(item_price*tax_item)
print(remaining_amount)

print(50 - 15 -(15*0.03))