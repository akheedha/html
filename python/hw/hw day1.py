import random

rice = 45
sugar = 40
oil = 130

r_sold = 3
s_sold = 2.5
o_sold = 1.8

total_cost_rice = rice * r_sold
total_cost_sugar = sugar * s_sold
total_cost_oil  = oil * o_sold

print("Cost of rice: ",total_cost_rice)
print("Cost of sugar: ",total_cost_sugar)
print("Cost of oil: ",total_cost_oil)

total_bill = total_cost_oil + total_cost_rice + total_cost_sugar
print("Total bill amount: ",total_bill)

print("\nBill as int",int(total_bill))
print("Bill as str: ",str(total_bill))

delivery = random.randrange(5,10)
total_bill = total_bill + delivery

print("\nTotal bill with delivery charge: ",total_bill)