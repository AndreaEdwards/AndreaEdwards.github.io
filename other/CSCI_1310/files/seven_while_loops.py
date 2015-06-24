#counter = 0
#while counter < 10:
#	print("hello")
#	counter += 1
	
#print("end")

import random

answer = random.randint(0, 100)
print("answer %d" % answer)

while True:
	guess = int(input("What's the number? "))
	if guess < answer:
		print("That's too low! ")
	elif guess > answer:
		print("That's too high! ")
	else:
		print("Correct!")
		break
print("end")
