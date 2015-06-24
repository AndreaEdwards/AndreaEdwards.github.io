#Conditional expression
if False:
	result = 43
else:
	result = 12
print(result)

#Is there an easier way than assigning result twice?

result = 42 if True else 12
print(result)
#Fitting all logic on one line

result = 11
result = 42 if (12 < 14) else result
print(result)

#Compound relational expressions
a = 1
b = 2
if a > 0 and a < b:
	print("it worked")

#stated more simply (chaining if statement stuff is unique to python)
if 0 < a < b:
	print("it worked")
