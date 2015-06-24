#!usr/local/python3

# review

# this is the most simple form of creating a class
# if more than one word in class name use camel casing

class Quarterback:
	pass


# display is a method of the class Team
class Team:
	def display(self):
		print(self.name)

broncos = Team()
broncos.name = "Denver Broncos"


# front (reciever) is noun. method is verb.
broncos.display()

# define our own constructor.
# The role of constructor (__init__) is to
# setup any local variables that you will need for any methods
class Quarterback:
	def __init__(self, qb_name, qb_number):
		self.name = qb_name
		self.number = qb_number

	def __str__(self):
		return "Quarterback: %s" % self.name

	def display(self): # a great function name is only a verb (verb_noun is ok)
		print(self.name, "jersey number is", self.number)

class Team:
	def __init__(self, name):
		self.name = name
		self.players = []

	def display(self):
		print(self.name, self.players)

	def city(self):
		pieces = self.location.split(",")

	def add_player(self, player):
		self.players.append(player)
		# send_email_to_espn("Quaterback changed teams! %s" % player.name)
		print("new player added %s" % player.name)


class League:
	def __init__(self):
		self.teams = []

	def move(self, team_to_move, destination):
		for team_to_move in self.teams:
			if team_to_move.location == destination:
				print("Can't move here!")
			else:
				team_to_move.location = destination
				print("New team location is %s" % destination)


broncos = Team("Denver Broncos")

peyton = Quarterback("Peyton Manning", 18)
print(peyton.name)
print(peyton) # calls the __str__ method; if __str__ is not over-written, this call will display the location of the object
peyton.display()

broncos.add_player(peyton)

nfl = League()
nfl.move(broncos)


