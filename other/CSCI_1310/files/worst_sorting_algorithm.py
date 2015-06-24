findAnimal = input("Which animal? ")
animals = ['panda', 'koala', 'monkey', 'leopard']

#i means "index" using i is the only exeption to the rule "never give your variables single character names"
i = 0

# this is a linear search that runs linearly with respect to the number of 
#items is in the list
while i < len(animals):
	animal = animals[i]
	print("is %s a %s" % (animal, findAnimal))
	if animal == findAnimal.lower():
		break
	i += 1

print("index is", i)
