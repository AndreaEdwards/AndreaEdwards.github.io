#Input statement
mnt_height = int(input("What is the height of the mountain? "))

#Given mountains
rank_1_name = "Mount Everest"
rank_1_height = 29029
rank_2_name = "K2"
rank_2_height = 28251
rank_3_name = "Kangchenjunga"
rank_3_height = 28169

#Conditionals
if mnt_height == rank_1_height:
	assnd_mnt = rank_1_name
	rank = "first"
	result_statement = "%sft is the height of %s and is the %s highest mountain." % (mnt_height, assnd_mnt, rank)
	print(result_statement)
elif mnt_height == rank_2_height:
	assnd_mnt = rank_2_name
	rank = second
	result_statement = "%sft is the height of %s and is the %s highest mountain." % (mnt_height, assnd_mnt, rank)
	print(result_statement)
elif mnt_height == rank_3_height:
	assnd_mnt = rank_3_name
	rank = third
	result_statement = "%sft is the height of %s and is the %s highest mountain." % (mnt_height, assnd_mnt, rank)
	print(result_statement)
else:
	msg = "Height does not match that of the first three heighest mountains. Please enter a correct height!!"
	print(msg)
	
