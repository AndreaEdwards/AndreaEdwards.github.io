#!usr/local/bin/python3

quote = "It was the best of times, it was the worst of times."

length = len(quote)
word_list = quote.split(' ')
for i in range(4):
	print(word_list[i])
print(' '.join(quote.split(' ')[::-1]))

def exponentiation(x, y):
	return(x ** y)

print(exponentiation(2, 5))

months = {1: 'Jan', 2: 'Feb', 3: 'Mar'}
print(months[1])

num_list = [1, 2.45, 5, 3.654]
sum = 0
for num in num_list:
	sum += float(num)
mean = sum/len(num_list)
print(mean)

# 5.2
# 0
# blablablablabla
# 3.14

file = open("/Users/Andrea/Desktop/CSCI_1310/students.txt", "r")
new_file = open("/Users/Andrea/Desktop/CSCI_1310/students_list.txt", "w")
for line in file:
	first, last, student_id = line.replace(" ", "").split(",")
	new_file.write('\t'.join((last, first, student_id)))
new_file.close()
file.close()
