#Iterators, for loops

#inifinite loops are bad, counters allow while loops to time out
counter = 0
while counter < 10:
	 print("success")
	 counter += 1

#manually keeping track of counters and indexes can be problematic

#data types that can be iterated over include lists, ranges, strings,
#and dictionaries
#ranges are good because they don't enter every item in the memory (like
#lists do

#collection = [1, 2, 3, 4]
#collection = range(1,4)
collection = 'The quick brown fox jumped over the lazy dog.'

indexes = [0, 1, 2, 3]
animals = ['panda', 'fox', 'dog', 'kangaroo']
for item in indexes:
	print(animals[item])

for item in collection:
	print(item)

# you can iterate over heterogeneous lists and the variable (item) 
#will take on whatever type is at that position in the list

#introduce mapping
destination = []
for animal in animals:
	destination.append(animal + ' is cute')
print('original', animals)
print('mapped', destination)
print(len(animals), len(destination))

#introduce filtering
numbers = [1, 2, 3, 4]
destination = []
for number in numbers:
	if number > 2:
		destination.append(number * 2)
print(destination)
print(len(numbers), len(destination))

#reduce the dataset into single value
numbers = [1, 2, 3, 4]
accumulator = 1
for number in numbers:
	accumulator = accumulator * number
print('original', numbers)
print('sum', accumulator)

