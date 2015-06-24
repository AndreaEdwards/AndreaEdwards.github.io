#!usr/local/python3

# when you run this, you see the key word "class"
print(type(11))
print(type(11.23))
print(type("string goes here"))

# names of classes always begin with an uppercase leter
# and always begins with a noun
class Quarterback:
	# this is a class code
	pass # this is an escape key for satisfying the syntax

class Team:
	pass

# prints class 'type' indicating this is a special type developed
# outside of python
print(type(Quarterback))
peyton = Quarterback()
print(type(peyton))

# classes are containers for attributes
peyton.name = "Peyton Manning"
peyton.number = 18

# here you see a hexadecimal that indicates where it is
# stored in memory
print(peyton)

# dot is operator. or left we have instance.
# on right we have attribute we are trying to extract from
# class
# name and number are attribues of the class object
brady = Quarterback()
brady.name = "Tom Brady"
brady.number = 12

# now we have two instances of the class Quarterback
# we have intantiated the class twice
# and we see that they have two unique locations in memory
print(brady)

def display_player(player):
	print(player.name, " jersey number is ", player.number)

display_player(peyton)
display_player(brady)

broncos = Team()
broncos.name = "Denver Broncos"
broncos.location = "Denver, CO"
broncos.stadium = "Mile High Stadium"
broncos.players = []

patriots = Team()
patriots.name = "New England Patriots"
patriots.location = "Foxborough, MA"
patriots.stadium = "Gilette Stadium"
patriots.players = []

def display_team(the_team):
	print(the_team.name, "play in", the_team.stadium,
		  "located in", the_team.location)

def team_city(the_team):
	pieces = the_team.location.split(",")
	return pieces[0]

display_team(broncos)
display_team(patriots)
print(team_city(broncos), team_city(patriots))

exit()

# a function is the name of statement we would like to 
# run later.

def display():
	print("this vale is ", 1)

# this is what's known as "calling", "invoking", "running", or
# "executing" the function
display()

# passing in arguments make functions more flexible
def display(a):
	print("this vale is ", a)

display(1)

# any argument you pass into a function is local to that 
# function. Cannot ask to print "a" after you've run the function

# adding a return statement allows the program to return
# a value back (instead of just printing something)
# to capture a return value, store it in a variable

""" Sums the numbers in the list and returns the total.
	list - the list of integers
	returns an integer
"""

def add(a, b):
	sum = a + b
	return sum

print(add(1, 2))

# to capture a return value store it in a variable.
my_total = add(1, 2)

# best practice == functions should perform only 1 logical 
# task.
# usually function names begin with verbs (because they are
# performing a task)









