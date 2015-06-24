#!usr/local/bin/python3

numbers = []
numbers = [10, 20, 40, ]
print(numbers[0])
print(numbers[2])
# find the last item in the list
last = len(numbers)-1
print("the length is", len(numbers))
print("last index is", last)
# prints the last item in the list. most programming languages require
# something like this
print(numbers[last])
# if you try to ask for data that isn't there, you will get an error.
# indices don't have to be positive integers
# prints the last item in the list (unique to python, ruby, and a few others)
print(numbers[-1])

# slicing. last index is not included
print(numbers[0:2])
# gives the entire list
print(numbers[0:])
# also gives the entire list
print(numbers[:])

# here is an easy way to generate a new list without corrupting the original
copy = numbers[:]
print(numbers)
copy.append(12)
print(copy)

# to change data in the middle. lists are mutable unlike strings
numbers[1] = 300
print(numbers)

# can also mutate a range of values
numbers[1:3] = [300, 400]
print(numbers)

numbers = [10, 20, 40, 60, 80]
numbers.insert(1, 500)
print(numbers)

# removing data
del numbers[2]
print(numbers)

# append and pop are symetrical
last = numbers.pop()
print(numbers)
print("last item in the list", last)

# numbers is "expensive" because it is a linear search
numbers = [10, 20, 40, 60, 80]
numbers.remove(60)
# in order to expunge all instances of "60", would have to go in a loop
# only removes the first instance
numbers = [10, 20, 40, 60, 80, 60, 60, 60, 60]
numbers.remove(60)
print(numbers)

# list comprehensions.
# map reduce filter example
# mapping is "changing data from one form to another without
# changing the original"
the_best_qbs = []
names = ["Manning", "Brees", "Brady"]
for name in names:
    the_best_qbs.append(name.upper())

print("all caps is", the_best_qbs)

numbers = [10, 20, 40, 60, 80]

# not list comp
squares = []
for number in numbers:
    squares.append(number ** 2)
# list comp
squares = [x ** 2 for x in numbers]

print("original is ", numbers)
print("squares is ", squares)

# filtering
# similar to map with addition of boolean predicate.
# if true include. if false reject
the_best_qbs = []
names = ["Manning", "Brees", "Brady"]
for name in names:
    if name == 'Manning' or name == 'Brees':
        the_best_qbs.append(name.upper())

print("original", names)
print("the best", the_best_qbs)

# more pythonic ==> filtering inside of a list comprehension
the_best_qbs = []
names = ["Manning", "Brees", "Brady"]
the_best_qbs = [name.upper() for name in names if name == 'Manning' or name == 'Brees']
print("original", names)
print("the best", the_best_qbs)





