# Lab 2 Calculations
# Author: Andrea Halweg-Edwards
# Date: 1/20/2015

sales_tax = .0735
num_items = 2
price = 15.915
cost_per_item = (price - sales_tax) / num_items

print ("The cost of each item is $%.2f" % cost_per_item)
print  ("The cost of each of the " + str(num_items) + " items is $%.2f" % cost_per_item)

sales_tax = 0.1555
num_items = 4
price = 63.82
cost_per_item = (price - sales_tax) / num_items

print ("The cost of each item is $%.2f" % cost_per_item)
print ("The cost of each of the " + str(num_items) + " items is $%.2f" % cost_per_item)
