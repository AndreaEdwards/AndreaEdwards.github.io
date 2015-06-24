#Input statements
string_list = []

#for loop that prints uppercase
for i in range(1,6):
	string_list.append(input("Input string " + str(i) + " in lowercase font. "))
	print(string_list[i-1].upper())
