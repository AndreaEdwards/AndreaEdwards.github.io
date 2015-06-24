""" 
Goals:
1. Go over data types
2. Go over iterator (the for loop)

Both examples, use 
sentence = "The quick brown fox jumped over the lazy dog" as example

Data types:
things that hold one value = string, integer, float
things that hold more than one value (collections) = list, dict, tuple, set

important concepts:
1. why is float called float?
2. important operators (modulus %)
3. iterating through a string and a list. strings are immutable
and lists are mutable 

break sentence up into string with split(). then iterate through
using list index and for i in range(len(list))
"""

# Data types
# when you create a variable, a location is setup in memory with the
# variable name as an identifier for that location and the value
# at that location.
# For example, you can create a variable called "a" with a value of 5
# using the 'assignment' operator. Not the same as the 'equals' sign
# in mathematics
a = 5
# After the command executes, there is a location in memory that is 
# identified as 'a' and that location holds a value of 5. 
print a
# variables have types. These variables are integers. All types have
# a specific set of built in (or custom) operations that can be
# performed on them
b = 10
c = a + b
print "Sum of a and b = ", c
# when our data types are numbers, the + operator is addition

string1 = "this is a string"
string2 = ' and this is another string'
# when our data types are strings, the + operator is concatenation
string_cat = string1 + string2 
print "Concatenation of string1 and string2: ", string_cat


# there are other data types such as floats (which are numbers with
# decimal places)
my_float = 4.5


# and boolean variables
myBool = True

# Data types are important because they dictate which operations 
# you can perform on them. Sometimes, it is important to cast
# your variable to a different type in order to perform some
# operation. For example:
my_num = 5
my_variable = int(raw_input("Enter an integer value: "))
print my_variable
new_num = my_variable + my_num
print type(my_variable)
my_variable = int(my_variable)
print my_variable
print type(my_variable)

# it's important to understand what the result of different operators are
# on different data types: two more examples / and %

# for example, the '/' operator will perform integer division if given two
# integers
7/2

# but when given at least one float, you will get the expected mathematical 
# result
7.0/2

# this is where casting can come in handy.
float(7)/2
float(my_variable)/3

# another important operator is the modulo %
# you can think of modulo as giving the remainder of integer division for 
# 6 % 2 = 0 because there is no remainder.
# 7 % 2 = 1 because 2 goes into 7 three times and 7 - 6 is 1
# 2 % 7 = 2 because 2 divided by 7 gives a fractional result leaving 2 as remainder

# modulo operator is really helpful in string operations.
my_string = "Hello!"
print "A common greating: %s" % my_string

# Python also has a variable type called a list. A list is a data type
# that contains a collection of items.
# the items in the list can be of different types.

my_list = [4, 6.5, 'a']
print(my_list)

# to access each item in the list, we use the index of the item.
# indexing starts at 0, so the first item in the list is
print my_list[0]
print my_list[1]
print my_list[2]

# we can iterate through a list or a string or a collection of numbers 
# using an iterator

indexes = [0, 1, 2, 3]
animals = ['panda', 'fox', 'dog', 'kangaroo']
for item in indexes:
	print animals[item]

collection = 'The quick brown fox jumped over the lazy dog.'
for item in collection:
	print item

list_length = len(my_list)
my_range = range(len(my_list))
print my_range

for i in my_range:
	print my_list[i]

# can combine expression
for i in range(len(my_list)):
	print my_list[i]

# you can iterate over heterogeneous lists and the variable (item) 
#will take on whatever type is at that position in the list
#introduce mapping
destination = []
for animal in animals:
	destination.append(animal + ' is cute')
print 'original:', animals
print 'mapped:', destination
print len(animals), len(destination)

#introduce filtering
numbers = [1, 2, 3, 4]
destination = []
for number in numbers:
	if number > 2:
		destination.append(number * 2)
print destination
print len(numbers), len(destination)


#reduce the dataset into single value
numbers = [1, 2, 3, 4]
total = 0
for number in numbers:
	total += number
print 'original:', numbers
print 'total:', total


##### Next time! apply a string operator and then find some interesting characteristics
##### sentence = 'The quick brown fox jumped over the lazy dog.'
##### my_words = sentence.split()
##### print my_words
##### 
##### counts = {}
##### for word in my_words:
##### 	if word in counts:
##### 		counts[word] += 1
##### 	else:
##### 		counts[word] = 1
##### print counts
##### 	
##### 
##### indexes = [0, 1, 2, 3]
##### animals = ['panda', 'fox', 'dog', 'kangaroo']
##### for item in indexes:
##### 	print(animals[item])
##### for item in collection:
##### 	print(item)












