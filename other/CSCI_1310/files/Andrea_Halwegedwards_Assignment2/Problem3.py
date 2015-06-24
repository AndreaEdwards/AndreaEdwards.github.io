#List the variables
one_way = 35
mpg = 13
price_per_gal = 2.00
days_per_month = 30
months_per_year = 12

#Calculate round trip cost and print result
round_trip = price_per_gal * (one_way / mpg)
statement1 = "The cost of a round trip is $%.2f." % round_trip

#Calculate monthly cost and print result
monthly_cost = round_trip * days_per_month
statement2 = "The monthly cost is $%.2f." % monthly_cost

#Calculate annual cost and print result
annual_cost = monthly_cost * months_per_year
statement3 = "The annual cost is $%.2f." % annual_cost

print(statement1)
print(statement2)
print(statement3)

