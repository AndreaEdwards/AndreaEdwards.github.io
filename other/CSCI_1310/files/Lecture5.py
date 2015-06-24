# print(sys.argv)
#gives "Name Error" because we didn't import the sys module

#below code works
import sys
print(sys.argv[0])
print(sys.argv[1])
print(sys.argv[2])

### contitionals (if statements)
weather = 'cloudy'
#relational operator "==" binary oprator takes two operands
#the result is boolean true or boolean false
if weather == 'cloudy':
	print("bring umbrella")
	
a = 42
"""
the if statement can be as long as we want it to be. you can use
different boolean operators. Group operators with parenthases 
you can alsos place conditionals within conditionals
"""
if a < 43 or (a < 1000 and a > 12):
	print("less than")
#"""
#else statement evaluates when the if statement is false
#"""
else:
	if a > 12:
		print("greater than 12")
	print("this is false")
print("we're done!")

###
a = 42
if True:
	print("less than")
elif a > 12:
	print("greater than 12")
	print("this is false")
else:
	print("runninglast ditch effort")
print("we're done!")
