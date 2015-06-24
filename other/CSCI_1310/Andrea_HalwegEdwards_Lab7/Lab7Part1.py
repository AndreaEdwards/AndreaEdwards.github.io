#!usr/local/python3


def create_seq_set(seq):
	seq_set = set()
	for base in seq:
		seq_set.add(base)
	return(seq_set)

def calculate_seq_length():
	seq_set = create_seq_set(seq)
	return(len(seq_set))

def return_seq_information():
	seq_set = create_seq_set(seq)
	length = calculate_seq_length()
	print("The DNA string has", length, "unique elements.")
	print("The elements are:", seq_set)

seq = 'CGCAAATTTGCCGGATTTCCTTTGCTGTTCCTGCATGTAGTTTAAACGAGATTGCCAGCACCGGGTATCATTCACCATTTTTCTTTTCGTTAACTTGCCGTCAGCCTTTTCTTTGACCTCTTCTTTCTGTTCATGTGTATTTGCTGTCTCTTAGCCCAGACTTCCCGTGTCCTTTCCACCGGGCCTTTGAGAGGTCACAGGGTCTTGATGCTGTGGTCTTCATCTGCAGGTGTCTGACTTCCAGCAACTGCTGGCCTGTGCCAGGGTGCAGCTGAGCACTGGAGTGGAGTTTTCCTGTGGAGAGGAGCCATGCCTAGAGTGGGATGGGCCATTGTTCATG'
return_seq_information()