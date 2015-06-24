#Parsing a fastq file using BioPython

"""
What does it mean to parse a file?
Parsing (syntactic analysis) is the process of analysing a string of symbols
that conform to a particular set of rules.

This means that in order to parse a file, you have to know ahead of time What
the format of that file is. 

Things to ask yourself:
1. What is the format of the file you are trying to extract information from?
2. What information are you trying to extract from the file?

A fastq file normally uses four lines per sequence:
1. Always begins with the '@' character and is followed by a sequence identifies
2. Always the raw sequence
3. Always begins with a + character and is optionally followed by the same sequence identifier.
4. Always encodes the quality values for the sequence in line 2 and must contain the same number
	of symbols as the letters in the raw sequence.

Let's look at a .fastq file.

Always check that the file is in the correct format before you begin to write or apply
a parser.

Here is an example function. The question I was asking is: how many reads above 30nt are in this file?
"""

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

fastq_dict = parse_fastq("/Users/Andrea/Desktop/code_review/Sample_R1.fastq")
print fastq_dict

def filter_by_length(fastq_dict, filter_length):
	filtered_dict = {}
	for key in fastq_dict:
		if len(fastq_dict[key]) >= filter_length:
			filtered_dict[key] = fastq_dict[key]
	return filtered_dict

filtered_dict = filter_by_length(fastq_dict, 30)
print filtered_dict 

percent = (float(len(filtered_dict))/len(fastq_dict)) * 100
print percent

"""
How to find out if BioPython contains a utility you are interested in?

Consult the documents!! Look at website for example.

Here is an example of using the parse method of the SeqIO object to print out
all the sequences in the fastq file.
"""
from Bio import SeqIO

handle = open("/Users/Andrea/Desktop/code_review/Sample_R1.fastq")
for record in SeqIO.parse(handle, "fastq"):
	print record.seq
handle.close()


"""
Bio.SeqIO is the sequence input/output interface for BioPython. For implementations,
see the tutorials (there are many).

Bio.SeqIO provides a simple uniform interface to input and output assorted
sequence file formats (including MSAs), but will only deal with sequences as
SeqRecord formats.

What is Bio.SeqIO?
What is a SeqRecord object?

In BioPython, sequences are usually held as Seq objects, which hold the sequence
and an associated alphabet. The Seq object essentially combines a Python string with
an (optional) biological alphabet.
"""

from Bio.Seq import Seq
my_seq = Seq("AGTACACTGGT")
print my_seq
#Seq('AGTACACTGGT', Alphabet())
print my_seq.alphabet
#Alphabet()

"""
In the above example, we haven't specified an alphabet so we end up with a default
generic alphabet. Biopython doesn't know if this is a nucleotide sequence or a 
protein rich in alanines, glycines, cysteines and threonines. If you know, you
should (can) supply this information.
"""

#from Bio.Seq import Seq
from Bio.Alphabet import generic_dna, generic_protein
my_seq = Seq("AGTACACTGGT")
print my_seq
#Seq('AGTACACTGGT', Alphabet())
my_dna = Seq("AGTACACTGGT", generic_dna)
print my_dna
#Seq('AGTACACTGGT', DNAAlphabet())
my_protein = Seq("AGTACACTGGT", generic_protein)
print my_protein
#Seq('AGTACACTGGT', ProteinAlphabet())

"""
Supplying this information is important because it allows for error handling.
For example, it doesn't make any sense to concatentate a protein and nucleotide 
sequence, so BioPython will throw an error if you try to do this.
"""

my_protein + my_dna
#Traceback (most recent call last):
#...
#TypeError: Incompatable alphabets ProteinAlphabet() and DNAAlphabet()

"""
Similarly, an error will be thrown if you try to do something like translate
a protein sequence.
"""


"""
The Seq object has a number of methods which act just like those of a Python
string (For example, the find and count methods).
"""

#rom Bio.Seq import Seq
#from Bio.Alphabet import generic_dna
my_dna = Seq("AGTACACTGGT", generic_dna)
print my_dna
#Seq('AGTACACTGGT', DNAAlphabet())
my_dna.find("ACT")
#5
my_dna.find("TAG")
#-1
my_dna.count("GG")
#note that count is non-overlapping
"AAAAAAA".count("AA")


"""
BioPython has several built-in functions for biological applications:
complement, reverse complement, translation, back translation
"""

#from Bio.Seq import Seq
#from Bio.Alphabet import generic_dna
#my_dna = Seq("AGTACACTGGT", generic_dna)
print my_dna
my_dna.complement()
#Seq('TCATGTGACCA', DNAAlphabet())
my_dna.reverse_complement()
#Seq('ACCAGTGTACT', DNAAlphabet())
my_dna.transcribe()



















