#!usr/local/bin/python3

# Named parameters

def combine(a, b, c):
	print(a, b, c)

# positional arguments
combine(1, 2, 3)
# example of named parameters
combine(b = 1, c = 2, a = 3)

values = [5, 1, 3, 2, 4]
# this works because they are all integers
values.sort()
print("sorted values", values)

# we can also sort by any parameter we like
import random
def by_random(item):
	print("by_random called with item: ", item)
	return(random.randint(0, 100))

# passing a function into another function
values.sort(key = by_random)
print("sorted values", values)

players = [
	('Manning', 18, 39),
	('Brady', 12, 37),
	('Brees', 5, 36)
]

players.sort()
print("sorted players", players)

def by_jersey(player):
	jersey = player[1]
	return jersey

players.sort(key = by_jersey)
print("sorted players", players)

# build our own hash table
# hash tables need to handle collisions. look up what this means
class HashTable:
	def __init__(self):
		self.capacity = 10
		self.buckets = [[] for i in range(0, self.capacity)]
		print(self.buckets)

	def __str__(self):
		return(str(self.buckets))

	def get(self, key):
		some_huge_number = hash(key)
		index = some_huge_number % self.capacity
		# return self.buckets[index]

		chain = self.buckets[index]
		for entry in chain:
			if entry[0] == key:
				return entry[1]
		return None

	def set(self, key, value):
		some_huge_number = hash(key)
		index = some_huge_number % self.capacity
		# self.buckets[index] = value

		evicted = False
		chain = self.buckets[index]
		print("chain is ", chain)
		# evict previous key
		for entry in chain:
			if entry[0] == key:
				evicted = True
				entry[1] = value
				break
		# brand new key
		if not evicted:
			chain.append([key, value])

players = HashTable()
players.set("Manning", 18)
players.set("Brady", 12)
players.set("Brees", 5)
print(players.get("Brady"))
print("Tom's number is", players.get("Brady"))
print("Drew's number is", players.get("Brees"))
print("Peyton's number is", players.get("Manning"))
print(players)















