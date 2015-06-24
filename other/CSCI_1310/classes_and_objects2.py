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

# self means whatever object recieves this message is 
# self
# always an object of the class it is in
class Team:
	def display(self):
		print(self.name, "play in", self.stadium,
		  "located in", self.location)

	def city(self):
		pieces = self.location.split(",")
		return pieces[0]

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
# usually you don't make an object and then populate
# attributes (that is what __init__ is for)
brady = Quarterback()
brady.name = "Tom Brady"
brady.number = 12

# a function that belongs to a class is called a "method"
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


broncos.display()
patriots.display()

# display_team(broncos)
# display_team(patriots)

print("team is", broncos.city())
print("team is", patriots.city())
# print(team_city(broncos), team_city(patriots))

exit()