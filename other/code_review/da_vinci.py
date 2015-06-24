# dictionaries are faster to search than lists

from time import time

myList = list(range(0, 10 * 100 * 1000))

def searchList(find, numbers):
	for number in numbers:
		if number == find:
			return number

find = 10 * 100 * 1000 - 1

start = time()
found = searchList(find, myList)
duration = time() - start

numbers_dict = {}
for number in numbers:
	numbers_dict[number] = number

start = time()
found = find in numbers_dict
dict_duration = time() - start

print 'list search time: ', list_duration
print 'dict search time: ', dict_duration
print '(list duration/ dict duration) is: ', list_duration/dict_duration
