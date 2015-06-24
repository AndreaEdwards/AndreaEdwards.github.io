---
layout: post
categories: lectures
title: Classes & objects
---

# Classes & objects

Chapter 15 in [Think Python]({{ site.baseurl }}/resources/)
covers defining classes and creating objects. The sample code we worked
through in lecture is below.

## Sample code

    class Quarterback:
        def __init__(self, qb_name):
            print("custom constructor was called")
            self.name = qb_name

        def __str__(self):
            return "Quarterback: %s" % self.name

        def display(self):
            print(self.name, " jersey number is", self.number)

    class Team:
        def __init__(self, name):
            self.name = name
            self.players = []

        def display(self):
            print(self.name, "play in", self.stadium, "located in", self.location)

        def city(self):
            pieces = self.location.split(",")
            return pieces[0]


    peyton = Quarterback("Peyton Manning")
    peyton.number = 18

    print(peyton)

    print("peyton's name is", peyton.name)

    brady = Quarterback("Tom Brady")
    brady.number = 12

    print("tom's name is", brady.name)

    broncos = Team("Denver Broncos")
    broncos.location = "Denver, CO"
    broncos.stadium = "Mile High Stadium"

    patriots = Team("New England Patriots")
    patriots.location = "Foxborough, MA"
    patriots.stadium = "Gilette Stadium"

    broncos.display()
    patriots.display()

    broncos.city()
    patriots.city()

    print(peyton)
    print(brady)

    peyton.display()
    brady.display()

