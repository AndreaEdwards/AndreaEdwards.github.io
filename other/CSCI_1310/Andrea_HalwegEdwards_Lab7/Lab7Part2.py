#!usr/local/bin/python3

def main():
	name_dict = name_lengths(name_list)
	print_stars()
	print("Name".ljust(0), "Length".rjust(20-len("Name")))
	print_stars()
	for name in name_dict:
		print(name.ljust(0), str(name_dict[name]).rjust(20-name_dict[name]))

def print_stars():
	name_dict = name_lengths(name_list)
	name_length_list = [name_dict[name] for name in name_dict]
	stars = ''
	for number in range(0,max(name_length_list)):
		stars += '*'
	for number in range(0, (20-(max(name_length_list))+1)):
		stars += '*'
	print(stars)

def name_lengths(name_list):
	name_information = {}
	for name in name_list:
		name_length = len(name)
		name_information[name] = name_length
	return(name_information)

name_list = [
    "Romo",
    "McNabb",
    "Brady",
    "Manning",
    "Rodgers",
    "Brees",
    "Kaepernick",
    "Flacco"
]

main()
