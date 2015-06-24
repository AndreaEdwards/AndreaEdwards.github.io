#Example FizzBuzz
#Loop through integers and print "Fizz" if it's diviible 3
#Print "Buzz" if it's divisibly by 5

counter = 0
while counter < 20:
	print 'counter is: ', counter
	if counter % 3 == 0 and counter % 5 == 0:
		print 'FizzBuzz'
	elif counter % 3 == 0:
		print 'Fizz'
	elif counter % 5 == 0:
		print 'Buzz'
	else:
		pass
	counter += 1

#Example why dictionaries are better than lists

from time import time

numbers = list(range(0, 10 * 100 * 1000))

def search_list(find, numbers):
	for number in numbers:
		if number == find:
			return number

find = 10 * 100 * 1000 - 1

start = time()
found = search_list(find, numbers)
list_duration = time() - start

numbers_dict = {}
for number in numbers:
	numbers_dict[number] = number

start = time()
found = find in numbers_dict
dict_duration = time() - start

print 'list search time: ', list_duration
print 'dict search time: ', dict_duration
print '(list duration/ dict duration) is: ', list_duration/dict_duration

#Example OO football team