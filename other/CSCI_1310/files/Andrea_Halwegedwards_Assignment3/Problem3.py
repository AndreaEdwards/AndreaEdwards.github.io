#Input statement
Time = int(input("Input the number of seconds. "))

#Calculate variables
hours = int((Time / 60) // 60)
minutes = int((Time / 60) % 60)
seconds = round(((Time / 60) % 1) * 60)

#Create lists of time values and names
time_list = [hours, minutes, seconds]
names = ['hour', 'minute', 'second']

#Test whether time name should be plural or singular
i = 0
while i < len(time_list):
	if time_list[i] > 1 or time_list[i] == 0:
		names[i] += 's'
		i += 1
	else:
		i += 1
			
#Print result statement
print("The time is %d %s, %d %s, and %d %s" % (hours, names[0], minutes, names[1], seconds, names[2]))

