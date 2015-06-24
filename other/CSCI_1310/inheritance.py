#!usr/local/python3

# Inheritance hierarchy. In these examples we are using the default constructor
# no __init__ here
# will not see inheritence more than one level deep. 
# in general the alternative to inheritence is called composition, and 
# composition (which we will  get to in c++) is more favored than inheritence
# "inheritence is a poor way to re-use code" because people will often make a 
# child of a class than has nothing to do with that type of class
# for example is you want to make a Speaker class don't re-use the speak method
# of Animal

class Animal(object):
	def speak(self):
		print("%s animal is speaking" % type(self))


# child of parent class Animal
class Dog(Animal):
	pass

animal = Dog()
animal.speak()

class Animal(object):
	def speak(self):
		print("%s animal is speaking" % type(self))

# child of parent class Animal. with specialized Dog method
class Dog(Animal):
	def speak(self):
		print("Woof!")


animal = Dog()
animal.speak()

class Animal(object):
	def speak(self):
		print("%s animal is speaking" % type(self))

# child of parent class Animal. with specialized Dog method
class Dog(Animal):
	def speak(self):
		print("Woof!")

# child of child
class Wolf(Dog):
	pass

animal = Dog()
animal.speak()
animal = Wolf()
animal.speak()

class Animal(object):
	def speak(self):
		print("%s animal is speaking" % type(self))

# child of parent class Animal. with specialized Dog method
class Dog(Animal):
	def speak(self):
		print("Woof!")

# child of child with specialized Wolf method
class Wolf(Dog):
	def speak(self):
		print("Growl!")

# when creating a child class, you can over-write the parent method or you
# can add new and specific methods.
class Bird(Animal):
	def fly(self):
		print("Flapping my wings!")

class Penguin(Bird):
	def fly(self):
		raise TypeError("I can't fly!")  # exception handling causes program to quit

	def swim(self):
		print("Some birds can swim.") # further specialization is an example of code reuse.

animal = Dog()
animal.speak()
animal = Wolf()
animal.speak()
animal = Bird()
animal.speak()
animal.fly()
bird = Bird()
bird.fly()
penguin = Penguin()
# penguin.fly() 
penguin.swim()


# re-defining speak all the time is laborious. using variables...
class Animal(object):
	def __init__(self):
		# self.sound = sound
		pass
	
	def speak(self):
		# print("%s animal is speaking" % type(self))
		print(self.sound)

# child of parent class Animal. with specialized Dog method
class Dog(Animal):
	def __init__(self):
		self.sound = "Woof"

# child of child with specialized Wolf method
class Wolf(Dog):
	def __init__(self):
		self.sound = "Growl!"


# when creating a child class, you can over-write the parent method or you
# can add new and specific methods.
class Bird(Animal):
	def __init__(self):
		self.sound = "Tweet"

	def fly(self):
		print("Flapping my wings!")

class Penguin(Bird):
	def __init__(self):
		self.sound = "Chirp"

	def fly(self):
		raise TypeError("I can't fly!")  # exception handling causes program to quit

	def swim(self):
		print("Some birds can swim.") # further specialization is an example of code reuse.

# polymorphism means "many forms" or "many shapes"
# in comp sci polymorphism looks like the following:
# because it can take on different data types
# the speak() method is defined in each data type.

def talk_to_an_animal(some_animal):
	print("Hello", type(some_animal))
	some_animal.speak()
	some_animal.speak()
	some_animal.speak()
	print("Great!")

def main():
	bird = Bird()
	bird.speak()
	bird.fly()

	penguin = Penguin()
	penguin.speak()
	penguin.swim()
	print("A penguin is type:", type(penguin))
	print("Is this a penguin?", isinstance(penguin, Penguin))
	print("Is this a bird?", isinstance(penguin, Bird))
	print("Is this an animal?", isinstance(penguin, Animal))

	talk_to_an_animal(bird)
	talk_to_an_animal(penguin)

main()
