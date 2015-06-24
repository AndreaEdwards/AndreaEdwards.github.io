#!usr/local/bin/python3

quote = "It was the best of times, it was the worst of times."
print(quote)

length = len(quote)

quote_words = quote.split(" ")
for i in range(0,4):
	print(quote_words[i])

reverse_list = quote_words[::-1]
reverse_sentence = " ".join(reverse_list)
print(reverse_sentence)

def exponentiation(x, y):
	return(x ** y)

print(exponentiation(2, 5))

months = {1: 'Jan', 2: 'Feb', 3: 'Mar'}
print(months[2])

num_list = [2, 4.6665, 5.8324, 5, 0.3495873, 6]
sum = 0
for num in num_list:
	sum += float(num)
average = sum / float(len(num_list))
print(average)

def fun1():
	x = 5.3
	return(x)
print(fun1())

def fun2(num):
	y = num * 5
	z = y ** 2
	return(z)

print(fun2(0))

def fun3(str):
	new_str = 5 * str
	return new_str

print(fun3('bla'))

def fun4(pi, r):
	c = pi * r * r

print(fun4(3.14, 1.0))

# for line in file:
# is great for reading each line in huge files
# file.readlines() opens the whole file into memory at once
# great for small files, bad for large files
# file.read() is the same as readlines, except that the readlines() stores
# the full contents of the file into a list while the read() function
# stores the entire file as a string.

file = open("/Users/Andrea/Desktop/CSCI_1310/students.txt", "r")
new_file = open("/Users/Andrea/Desktop/CSCI_1310/student_list.txt", "w")
for line in file:
	new_line = [(line.replace(" ", "")).split(",")[1], 
				(line.replace(" ", "")).split(",")[0], 
				(line.replace(" ", "")).split(",")[2]]
	new_file.write('\t'.join(new_line))
new_file.close()

file = open("/Users/Andrea/Desktop/CSCI_1310/students.txt", "r")
new_file = open("/Users/Andrea/Desktop/CSCI_1310/student_list_new.txt", "w")
for line in file:
	first, last, number = (line.replace(" ", "")).split(",")
	new_file.write('\t'.join((last, first, number)))
new_file.close()

file = open("/Users/Andrea/Desktop/CSCI_1310/students.txt", "r")
output = open("/Users/Andrea/Desktop/CSCI_1310/output.txt", "w")
for line in file:
	record = line.strip()
	if (len(record) == 0):
		continue
	last, first, number = record.split(",") #  because this is a 3 element list, we can apply a destructing assignment
	last = last.strip()
	first = first.strip()
	number = number.strip()
	output.write(
		"\t".join([first, last, number])
		)
output.close()



