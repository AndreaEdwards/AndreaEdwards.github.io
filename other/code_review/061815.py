from time import time

#myList = [seq1, seq2, 0.23, 4]

myDictionary = {'key1' : 'value1', 'key2' : 'value2'}

numbers = list(range(0, 10 * 100 * 1000))

def search_list(find, numbers):
	for number in numbers:
		if number == find:
			return number

find = 10 * 100 * 1000 - 1

start = time()
found = search_list(find, numbers)
list_duration = time() - start

numbers_dict = {}
for number in numbers:
	numbers_dict[number] = number

start = time()
found = find in numbers_dict
dict_duration = time() - start

print 'list search time: ', list_duration
print 'dict search time: ', dict_duration
print '(list duration/ dict duration) is: ', list_duration/dict_duration

def parse_fastq(file_name):
	fastq_dict = {}
	file = open(file_name)
	file_content = file.readlines()
	i = 0
	while i < len(file_content):
		if i % 4 == 0:
			fastq_dict[file_content[i].strip('\n')] = file_content[i+1].strip('\n')
			i += 1
		else:
			i += 1
	return fastq_dict

fastq_dict = parse_fastq('./R1_head.fastq')
print fastq_dict









