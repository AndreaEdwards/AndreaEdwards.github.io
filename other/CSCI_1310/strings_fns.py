#!usr/local/bin/python3

DNA = "ACCAATCTATCA"

index = DNA.find("CAA")
print("CAA found at: ", index)

DNA = "ACCAATCAATCA"
i = DNA.count("CAA")
print("there are ", i, "instances of CAA")

myStr = "Four score and seven years ago"
myStr = myStr.replace("seven", "many")
print(myStr)

DNA = "ATGCCATGCTATGGG"
DNANew = DNA.replace("A", "T")
print("Original: ", DNA, "New: ", DNANew)

wordlist = myStr.split(" ")
print(wordlist)

#Formatting
f = 4.5678
print("formatted float: %.2f" %f)
print("formatted float {:.2f}".format(f))
print("formatted float {:8.2f}".format(f))
print("DNA {:>20s} ".format(DNA))

myStr = "This is a test string"
print(myStr)
myStr = "This \t is \t a \t test \t string"
print(myStr)
myStr = "This is a \n\n test string"
print(myStr)


# declare variable
DNA = "AAGTCATGCCCGGGTTCGGA"

# use find to identify starting codon in the DNA
i = DNA.find("ATG")

# i is an index, a new string can be created by starting at that index
#and grabbing everything to the end
gene = DNA[i:]

# use count on the gene string to count the instances of the GGA and GGG
GGA = gene.count("GGA")
GGG = gene.count("GGG")

print(gene)
print("Number is ", GGA + GGG)

#Hamming Distance
DNA1 = "ATGCCATGCGGG"
DNA2 = "AAGCCATACGGA"
hd = 0
L = len(DNA1)
for x in range(0,L):
	if DNA1[x] != DNA2[x]:
		hd += 1
print(hd)