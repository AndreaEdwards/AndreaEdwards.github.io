#!opt/local/bin/python2.7

import matplotlib
matplotlib.use('svg')
import pylab
import matplotlib.pyplot as pyplot
#import matplotlib.pyplot as plt

# length = int(input("Enter the sequence length: "))
# unique_seqs = 4 ** length
# sequence_weight = 300 * length
# print "The molecular weight of the average sequence is: ", sequence_weight
# avogadro_num = 6.022 * (10 ** 23)
# print avogadro_num
# library_weight = (sequence_weight/avogadro_num) * unique_seqs
# print "The weight of this library is ", library_weight

avogadro_num = 6.022 * (10 ** 23)
length = 1
sequence_length_list = []
library_weight_list = []
for length in range(200):
	sequence_length_list.append(length)
	sequence_weight = float((300 * length)) / float((10 ** 3))
	unique_seqs = 4 ** length
	library_weight = (sequence_weight/avogadro_num) * unique_seqs
	library_weight_list.append(library_weight)
	print "Length: %d Variants: %d Weight: %s" % (length, unique_seqs, library_weight)

#while length > 0:
#	sequence_length_list.append(length)
#	sequence_weight = 300 * length
#	unique_seqs = 4 ** length
#	library_weight = (sequence_weight/avogadro_num) * unique_seqs
#	library_weight_list.append(library_weight)
#	# print "Length: %d Weight: %s" % (length, library_weight)
#	if library_weight > (5.972 * (10**53)):
#		length += 1
#		sequence_length_list.append(length)
#		sequence_weight = 300 * length
#		unique_seqs = 4 ** length
#		library_weight = (sequence_weight/avogadro_num) * unique_seqs
#		library_weight_list.append(library_weight)
#		break
#	else:
#		length += 1

#print sequence_length_list, library_weight_list

earth = [74, 1.3153810519e+25]
universe = [123, 6.92890406539e+54]

pyplot.plot(sequence_length_list, library_weight_list, color='black', lw = 4)
pyplot.yscale('log')
pyplot.xscale('log')
pyplot.show()
pyplot.savefig('test')
