#List variables and inputs
number_folds = int(input("How many times is the paper folded? "))
paper_thickness = 1 / 200
factor = pow(2, number_folds)
folded_thickness = (paper_thickness * factor)

#Conditional for one or multiples folds
name = 'fold'
if number_folds > 1:
	name += 's'
else:
	pass

#Print results statement
print("The thickness after %s %s will be %.2f cm." % (number_folds, name, folded_thickness))
