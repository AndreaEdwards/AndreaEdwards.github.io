from Bio import SeqIO

handle = open("/Users/Andrea/Desktop/code_review/Sample_R1.fastq")
for record in SeqIO.parse(handle, "fastq"):
	print record.seq
handle.close()