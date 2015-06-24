---
layout: post
categories: lectures
title: Iterating with while loops
---

# Iterating with while loops

With if statements, we were creating branches in the code that could
control the execution path of the code.

There's another control structure for controlling the path through the
code called loops. There are often times in our programs when we want
to do something over and over and over until some condition is met. This
is similar to the if code in that we want to do something if something
is true. However, the syntax is different and instead of doing something
only once, we do it as long as our condition is true.

As an example, imagine walking across campus. You would take a step
over and over and over until you reached your destination. You can think
of that process as being in a loop, where the action inside the loop is
to take a step.

For example, if you want to read all items in a list, you would loop
over the list. If you wanted to ask the user for input and continue asking
until they entered a valid value, you could put your question in a loop.
You may also want to do something like read all lines in a file, you
could put this action in a loop that runs until you've reached the end
of the file.

We'll start with a while loop, it looks like this:

    x = 0
    while x < 5:
      x = x + 1 #this line is very important, without it, code runs forever and crashes your computer
      print(x)

    print("done")

In this example, the while serves a similar purpose to the if. The x < 5
is evaluated to determine if it's true or false. The if true or false is
implicit in the while, or you might think of it as being included in the
while even though you don't see the word if. If it is true that x < 5,
then the code indented under the while executes. The x = x + 1 will update
the value of x by taking whatever the current value of x is and adding 1
to it. The first time through the loop, x is 1 at the print statement, and
then Python goes back up to the while on 155 and evaluates the true value
again. If it's true again, then again we go into the loop and add 1 to x
again. This time, a 2 will print. This continues until x = 5. When x = 5
and the while is evaluated, the expression is false and we fall out of the
loop and the "done" will print.


The relational operators that you can use for the while loop are the same
as those for the if statement,  <,>,<=,>=,==,!= . The difference between
an if and a while is that the while can repeat. You can think of the
while as a repeating if.


Let's look at how we could use our earlier choose your own adventure code
to force the user to enter a valid selection. With the if statement, we
could only check one time, and if the user entered something invalid, we
could print a message saying "Invalid selection", but there was no way
to ask again. What we really want to do is ask over and over and over
again until they enter a valid choice. That code would look something
like this

    #Start with two options only and check that user input is one of those
    my_str = input("Do you want to fight (d)ragon or (g)o home?: ")
    #if my_str is not "d" and it's not "g", then go into the loop
    while my_str != "d" and my_str != "g":
      print("not a valid selection")
      #update my_str by asking again, prepares us for going through the loop again
      my_str = input("Do you want to fight (d)ragon or (g)o home?: ")
    #At this point, we've received a valid selection because we're not in
    #the loop, so we know my_str must be either "d" or "g"
    if my_str == "d":
      print("You lose")
    else: #if it's not "d", it must be "g"
      print("wimp")


Another example of how while loops work can be found in the number
guessing game that we've all played. In this game, one player has a number
in mind and the other player is trying to guess the number. The person
guesses and the number holder responds with higher or lower depending on
the guess. In this game, it's not known how many guesses there will be,
that depends on what the guesses are.

This game can be implemented in code using a while loop and if statements
that we have discussed. We let the computer be one of the players by
using the random number generator.

Think first about the algorithm before writing the code. Things to consider,
we need a number, we need input from the user, we need a loop and
something to control the loop, and we need a way of checking the value
of the user's guess against the number that the computer is "thinking"
of, and then a way of getting a new guess from the user.

    #first, we need a number and we'll use Python's random number generator
    import random
    #generate a number between 0 and 100
    number = random.randint(0,100)
    #make the first guess
    guess = int(input("Guess a number between 0 and 100: "))
    numFound = False
    while numFound == False:
      if guess > number:
        print("You guessed too high")
        guess = int(input("Guess again: "))
      elif guess < number:
        print("You guessed too low")
        guess = int(input("Guess again: "))
      else:
        print("That's it. The number was ", number)
        numFound = True

<cite>Lecture material by Rhonda Hoenigman.</cite>

