#!usr/local/bin/python3

DNA = 'ACTZATZCTAZZZACCAZ'
print("original sequence is: ", DNA)

# Calculate length of string
length = len(DNA)
print("length of sequence is: ", length)

# Remove letter 'Z' and reverse string

DNA1 = ''
for nt in DNA:
    if nt != 'Z':
        DNA1 += nt
print("Edited sequence is: ", DNA1)
print("Reversed, edited sequence is: ", DNA1[::-1])