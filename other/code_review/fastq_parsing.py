
"""
Dictionaries are faster than lists. If you know you will need to be looking
something up in a really large collection of items, it's best to use a 
dictionary.
"""

from time import time

numbers = list(range(0, 10 * 100 * 1000))

# is the number ten million in this list?

def search_list(find, numbers):
	for number in numbers:
		if number == find:
			return number

find = 10 * 100 * 1000 - 1

start = time()
found = search_list(find, numbers)
list_duration = time() - start

numbers_dictionary = {}
for number in numbers:
	numbers_dictionary[number] = number

start = time()
found = find in numbers_dictionary
dictionary_duration = time() - start

print 'list search time: ', list_duration
print 'dictionary search time: ', dictionary_duration
print '(list duration / dictionary duration) is: ', list_duration / dictionary_duration


"""
Build a dictionary in which the keys are sequence identifiers and the values
are the sequences.
"""

def parse_fastq(file_name):
	"""Parses fastq file looking for first (identifier) and second
	(sequence) lines only. Outputs a dictionary in which the key is
	the identifies and the value is the sequence
		
	Useful for downstream processing such as finding all the sequences
	of a particular length or eliminating sequences with invalid characters

	Parameters
	----------
	file_name: string
		input string corresponds to a file path pointing to a .fastq file

	Returns
	-------
	dict
		Dictionary containing sequence ids (key) paired with sequences
		(values)  

    Examples
    --------
    >>> fastq_handlers = FastqHandlers()
    >>> fastq_dict = fastq_handlers.parse_fastq('path/to/fastq_file')
	
	"""	
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

"""
What is the average composition of each nucleotide (A, G, C, T) in the .fastq
files?
"""

import numpy

nt_freq = {'A' : [], 'G' : [], 'C' : [], 'T' : []}
for key in fastq_dict:
	nt_freq['A'].append(float(fastq_dict[key].count('A')) / len(fastq_dict[key]))
	nt_freq['G'].append(float(fastq_dict[key].count('G')) / len(fastq_dict[key]))
	nt_freq['C'].append(float(fastq_dict[key].count('C')) / len(fastq_dict[key]))
	nt_freq['T'].append(float(fastq_dict[key].count('T')) / len(fastq_dict[key]))
print nt_freq

#def CalcFreq(nt, seq):
#	nt_freq = float(seq.count(nt)) / len(seq)
#	return nt_freq
#
#for key in fastq_dict:
#	nt_freq['A'].append(CalcFreq('A', fastq_dict[key]))
#	nt_freq['G'].append(CalcFreq('G', fastq_dict[key]))
#	nt_freq['C'].append(CalcFreq('C', fastq_dict[key]))
#	nt_freq['T'].append(CalcFreq('T', fastq_dict[key]))

for key in nt_freq:
	print 'average composition of', key, numpy.mean(nt_freq[key]), '+/-', numpy.std(nt_freq[key])

"""
User USEARCH to build a merged .fastq file
"""
import os

fwd = './R1_head.fastq'
rev = './R2_head.fastq'
os.system("usearch7 -fastq_mergepairs " + fwd + " -reverse " + rev 
			+ " -fastqout merged.fastq")
















