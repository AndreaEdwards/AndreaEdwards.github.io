#Loop through integers and print "Fizz" if it's diviible 3
#Print "Buzz" if it's divisibly by 5

counter = 0 
while counter < 20:
	if counter % 3 == 0:
		print(counter, "Fizz")
	if counter % 5 == 0:
		print(counter, "Buzz")
	counter += 1
	print("counter", counter)
	
counter = 0 
while counter < 20:
	if counter % 3 and counter % 5 == 0:
		print(counter, "FizzBuzz")
		counter += 1
		continue
	if counter % 3 == 0:
		print(counter, "Fizz")
	if counter % 5 == 0:
		print(counter, "Buzz")
	counter += 1
	print("counter", counter)
	
counter = 0 
zz = ""
while counter < 20:
	if (counter % 3) == 0:
		zz = "Fizz"
	if (counter % 5) == 0:
		zz += "Buzz"
	if len(zz) > 0:
		print(counter, zz)
		zz = ""
	counter += 1
