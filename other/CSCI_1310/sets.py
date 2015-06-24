#!usr/local/bin/python3

# set is a unique finite set of items
# the most common use of set is to determine if something
# is a member

# create a set with the set() function
numbers = set()
print(numbers)

numbers.add(42)
numbers.add(12)
numbers.add(100)
print(numbers)
# the unique property of a set. if we add the same number
# twice.. it won't add it again. will guarantee that only
# unique items will be in there
numbers.add(100)
print(numbers)
numbers.remove(100)
numbers.add(100)

# can add any data type to a set
# numbers.add('something in here')

# can iterate through a set. sets are not ordered
for item in numbers:
	print("item is", item)

print(numbers)

ages = set([42, 12])

# can compare two different sets with union(), difference(),
# intersection()

print("numbers is ", numbers)
print("ages is ", ages)

print("union is ", ages.union(numbers))
print("difference is ", ages.difference(numbers))
# you must have the largest set first to take the difference
print("difference is ", numbers.difference(ages))
# intersection returns whatever is the same between two sets
print("intersection is ", numbers.intersection(ages))

print("some string" in ages)
print(42 in ages)


# can fake a set with a dictionary

fake_set = {}
fake_set[42] = None
fake_set[12] = None
fake_set[100] = None

print(fake_set)

print(42 in fake_set)


data = list(range(10, 10 * 1000 * 1000))

find = 10 * 1000 * 1000 - 1
from time import time
start = time()
for item in data:
	if item == find:
		break
list_duration = time() - start
print("list duration is ", list_duration)

test_set = set(data)
start = time()
find in test_set
set_duration = time() - start
print("set duration is ", set_duration)

print("list vs set ", list_duration/set_duration)




