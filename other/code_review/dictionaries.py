#!usr/local/bin/python3

# dictionaries stores keys and values
# two ways to create a dictionary
names = dict()
# or
names = {}

# to modify a dictionary
names['Manning'] = 18
names['Brady'] = 12
names['Elway'] = 7

print(names['Manning'])

# you can overright dict key/value pairs (don't use the same key twice unless
	# you wan to overright what you had before)
names['Manning'] = 9
print(names['Manning'])

# you can only have one value per key. However, the value can be a container 
# such as a tuple or a list

# dicts are iterable
for key in names:
	print(key, names[key])

# check if a key already exists: use the keyword 'in'
print('Brady' in names) # prints True
print('Brees' in names) # prints False
# can also use keyword 'in' for a list

#remove a value from the dict
print("deleted brady", names.pop('Brady'))
print(names)

# keys don't have to be strings. key can be any data type the python
# considers hashable (strings, integers, floats). 
# lists and dicts cannot be keys
numbers = {1: 2, 3: 4, 5: 6}
print(numbers[5])

# are the keys ordered? no. there is no order at all in dicts. the loops will
# randomly loop through the dict.

# the syntax of dict looks simlar to list syntax
# major difference is that the key lookup for dict does not have to be integer.

