print('Operators and Algorithms')

#integers
x = 12
y = 3

print(x + y)

#can't mix data types
#print (12 + "hi")

#gives 0 because the two variables are integers
print(1 / 5)

#gives the remainder 
print(1 % 5)

#modulus operator is useful for hash operators.

#convert 200 seconds to minutes and seconds
# If you just do division only, you'll have a fractional number of minutes but you won't have minutes and seconds. To get seconds, you need to use the mod operator.

minutes = 200/60
seconds = (200%60)
#seconds = input("How many seconds? ")
#seconds = raw_input("How many seconds? ")
#seconds = int(raw_input("How many seconds? "))
print(seconds)
print (str(minutes) + str(seconds))
print("minutes is", minutes, "seconds is", seconds)

co2 = 19.4
mpg = 26
miles = 12000

#python executes things left to right. When the floating point number is moved to the front, we get the more accurate result.
#because the result of 19.4/12000 is a float. The result of co2 * miles / mpg is a float.
print("How much CO2?", miles / mpg * co2, " pounds.")
print("How much Co2", co2 * miles / mpg, "pounds.")
print("How much CO2?", float(miles) / mpg * co2, "pounds.")
pounds = miles / mpg * co2
#string = "pounds %s" % pounds
string = "pounds %.2f" % pounds
#string = "pounds %.4f and miles %s" % (pounds, miles)
#string = "pounds %.4f and miles %d" % (pounds, pounds)
print(string)


#strings and numbers are called "string literals". floats are called "floating point literals"
co2 = 19.4
mpg = 26.0
miles = 12000
print("How much CO2?", miles / mpg * co2, " pounds.")
print("How much Co2", co2 * miles / mpg, "pounds.")


co2 = 19.4
mpg = 26.0
miles = input("How many miles? ")
print("How much CO2?", miles / mpg * co2, " pounds.")
print("How much Co2", co2 * miles / mpg, "pounds.")



