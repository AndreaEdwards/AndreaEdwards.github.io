#number = int(input("What is your number?"))
#print(number)
#if number < 100:
#	print("It's less than 100!")
#elif number == 100:
#	print("It's equal to 100!")
#else:
#	print("It's greater than 100!")

##poor style because redundant
b = True

#if b == True:
#	print("it's true")
	
##better	
#if b:
#	print("it's true")
	
a = 42
#if b and (a < 12):
#	print("it's true")
	
if b == a < 43:
	print("it's true")
else:
	print("it's false")

if b == (a < 43):
	print("it's true")
else:
	print("it's false")
