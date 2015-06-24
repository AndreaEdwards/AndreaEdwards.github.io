---
layout: post
categories: lectures
title: Inheritance
---

# Inheritance

Chapter 18 in [Think Python]({{ site.baseurl }}/resources/)
covers defining class inheritance relationships. The sample code we worked
through in lecture is below.

## Sample code

    class Animal(object):
        def __init__(self):
            self.sound = "Default sound."

        def speak(self):
            print(self.sound)

    class Dog(Animal):
        def __init__(self):
            self.sound = "Woof"

    class Wolf(Dog):
        def __init__(self):
            self.sound = "Growl"

    class Bird(Animal):
        def __init__(self):
            self.sound = "Tweet"

        def fly(self):
            print("Flapping my wings!")

    class Penguin(Bird):
        def __init__(self):
            self.sound = "Chirp"

        def fly(self):
            raise TypeError("I can't fly!")

        def swim(self):
            print("Some birds can swim.")


    # Polymorphism allows us to pass in any object that
    # implements a `speak` method. This is one of the major
    # advantages of object-oriented programming.
    def talk_to_an_animal(some_animal):
        print("Hello!", type(some_animal))
        some_animal.speak()
        some_animal.speak()
        some_animal.speak()
        print("Great!")


    penguin = Penguin()
    penguin.speak()
    penguin.fly()
    penguin.swim()

    print("A penguin is type: ", type(penguin))

    print("Is this a penguin?", isinstance(penguin, Penguin))
    print("Is this a bird?", isinstance(penguin, Bird))
    print("Is this an animal?", isinstance(penguin, Animal))

    talk_to_an_animal(bird)
    talk_to_an_animal(penguin)

