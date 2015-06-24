#!usr/local/bin/python3
from time import time

numbers = list(range(0, 10 * 1000 * 1000))

# find out if the number ten million is in the list

def search_list(find, items):

    for number in numbers:
    	if number == find:
    		return(number)

find = 10 * 1000 * 1000 -1
start = time()
found = search_list(find, numbers)


list_duration = time() - start
print("list found it?", found, list_duration)C

numbers_dictionary = {}
for number in numbers:
	numbers_dictionary[number] = number

find = 10 * 1000 * 1000 -1
# here we use the 'in' operator instead of using a for loop. 
start = time()
found = find in numbers_dictionary
# the difference in the above codes are run time

dictionary_duration = time() - start
print("dictionary found it?", found, dictionary_duration)

print("difference", list_duration/ dictionary_duration)

# dictionary is the fasted data structure.