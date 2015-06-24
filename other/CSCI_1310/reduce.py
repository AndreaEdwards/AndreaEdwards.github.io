#!usr/local/bin/python3

# random info:
# rm [blah] = remove blah
# rm -rf [blah] remove recursive force blah
# ls -l blah = list with permissions

# mapping filtering..  reducing
# this is an example of a general reduce algorithm
numbers = [10, 20, 30, 40]
sum = 0
for number in numbers:
	sum += number
print(sum)

from functools import reduce

# def reduce(function, list) # this is what the reduce function from 
# functools takes as arguments

def sum(accumulator, number):
	print("sum was called", accumulator, number)
	return accumulator + number
# in this case the reduce function is invoking the sum function. 
# this is an example of "functional programming"
total = reduce(sum, numbers)
# the above one line of code is equivalent to lines 11-14 above
print(total)

# this is another version of the reduce function # this is the exact 
# implementation as the provided funtion
def reduce(function, list):
	accumulated_value = list[0]
	for item in list[1:]:
		accumulated_value = function(accumulated_value, item)
	return accumulated_value

# even though we have the code above, python provides the sum function for us.
print(sum(numbers))