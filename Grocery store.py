rice_price = 45
sugar_price = 40
oil_price = 130

rice_quantity = 3
sugar_quantity = 2.5
oil_quantity = 1.8

rice_total = rice_price * rice_quantity
sugar_total = sugar_price * sugar_quantity
oil_total = oil_price * oil_quantity

print("Rice total:", rice_total)
print("Sugar total:", sugar_total)
print("Oil total:", oil_total)

total_bill = rice_total + sugar_total + oil_total

print("Total bill in integer:", int(total_bill))
print("Total bill in string: " + str(total_bill))

import random
delivery_charge = random.randrange(5, 11)
print("Delivery charge:", delivery_charge)

final_bill = total_bill + delivery_charge
print("Final bill including delivery:", final_bill)
