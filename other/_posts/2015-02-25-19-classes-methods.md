---
layout: post
categories: lectures
title: Classes, functions, and methods
---

# Classes, functions, and methods

Chapters 16 and 17 in [Think Python]({{ site.baseurl }}/resources/)
cover defining class methods. The sample code we worked through in lecture
is below.

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

        def add_player(self, player):
            self.players.append(player)
            # send_email_to_espn("Quarterback changed teams! %s", player.name)

    class League:
        def __init__(self):
            self.teams = []

        def move(self, team_to_move, destination):
            for team in self.teams:
                if team.location == destination:
                    print("Can't move here!")
                else:
                    team_to_move.location = destination



    peyton = Quarterback("Peyton Manning")
    # peyton.name = "Peyton Manning"
    peyton.number = 18

    print(peyton)

    print("peyton's name is", peyton.name)

    brady = Quarterback("Tom Brady")
    # brady.name = "Tom Brady"
    brady.number = 12

    print("tom's name is", brady.name)

    broncos = Team("Denver Broncos")
    # broncos.name = "Denver Broncos"
    broncos.location = "Denver, CO"
    broncos.stadium = "Mile High Stadium"
    broncos.players = []

    patriots = Team("New England Patriots")
    # patriots.name = "New England Patriots"
    patriots.location = "Foxborough, MA"
    patriots.stadium = "Gilette Stadium"
    patriots.players = []

    # brady.team = patriots
    # patriots.players.append(brady)
    patriots.add_player(brady)

    print("Displaying qb team")
    # brady.team.display()

    broncos.display()
    patriots.display()


    nfl = League()
    nfl.move(patriots)


    # display_team(patriots)
    # print("team is", team_city(broncos))
    # print("team is", team_city(patriots))

    broncos.city()
    patriots.city()

    print(peyton)
    print(brady)

    peyton.display()
    brady.display()

