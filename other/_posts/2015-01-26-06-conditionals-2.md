---
layout: post
categories: lectures
title: Conditional expressions
---

# Conditional expressions

In the previous lecture we worked with if/elif/else statements using numbers, and
saw how the value of a number would determine which branch of code
would execute. For example,

    a = 0
    if a > 0:
      print("a is greater than 0")
    elif a < 0:
       print("a is less than 0")
    else:
      print("a = 0")

First, evaluate the if expression, if it's true, code block indented
under it executes.
Otherwise, go on to the `elif`. if this expression is true, run code block.
if neither the if or the elif is true, run the else code

Today, we will look at this same type of evaluation, but with strings
and checking the value of a string to determine which branch to execute.
Next, we will examine using multiple conditions in an if statement.

Think back to those books you may have read, or command-line video games
you've played where you could Choose Your Own Adventure. In these books
and games, the user is presented with a scenario and asked to make a
decision. For example, Imagine you are standing outside a castle and
you are being chased by a dragon.

Do you want to: fight (d)ragon, (s)torm castle, (g)o home?

where, as the user, you would select "d" to fight the dragon, "s" to
storm the castle, and "g" to go home. Depending on the user's selection,
you would turn to a different page in the book, or in the video game, a
different block of code would run. This is another example of an if
conditional, but instead of looking at the value of a number, you're
using a letter.

    my_str = input("Do you want to fight (d)ragon, (s)torm castle, (g)o home?: ")
    if my_str == "d":
      print("You lose")
    elif my_str == "s":
      print("have fun storming the castle")
    elif my_str == "g":
      print("wimp")
    else:
      print("not a valid selection")

The first line gets input from the user. Since we're using the input
function, the type of my_str will be a string. We then use my_str in the
conditionals. In the line if my_str == "d", we're checking if my_str is
a "d". Notice that we use the "". This tells Python that we want to
check for the letter d and not a variable called d. Also notice the ==,
when checking for equality, you always use the == instead of the =. The
single = will assign a value, which is not what you want here.

The rest of the code proceeds in the same way as if we were using numbers.
If my_str is a "d", the "You lose" will print. If it's not a "d", then
the next elif is evaluated, and so on. If my_str does not equal any of
the given strings, then the else block will execute and "not a valid
selection" will print. This "not a valid selection" is how we handle
bad input.

## Exercise

Change the code above to include another option:
(c)ross the flood waters that will print "Good luck" if "c" is selected.

Conditionals can also include multiple conditions on multiple variables.
We saw how we could check a range on a variable, such as `10 < a < 15` to
check that a is greater than 10 and less than 15. But, you may want to
check if a < 0 or a > 10. There is no way to do this by checking that a
is between two numbers because the accepted range on a is discontinuous.

There are another type of operators called boolean operators that are
used to have multiple conditions. The boolean operators we'll talk about
here are AND and OR. For example,

    a = 12
    if a < 0 or a > 10:
      print("a is good")
    else:
      print("a out of range")

In this example, the a < 0 is evaluated and determined whether it is
true or false. Next, the second part, a > 10, is evaluated and
determined whether it is true or false. If either of these expressions is
true, then the whole statement is true and the code in the if block
will execute.

Notice that the OR is used in this example. This is because a can't
satisfy both conditions, it can't be both < 0 and > 10. No number meets
both conditions.

The other boolean operator is the AND operator. This operator is used
when both conditions need to be true, not just one or the other.

For example, if there are two variables and the value of each needs to
meet a certain condition.

    a = 5
    b = 10
    if a < 10 and b > 0:
      print("both are true")
    else:
      print("something is false")

In this case, it needs to be true that both a < 10 and b > 0. If either
of these conditions is not true, then the whole if statement is not true.

## Expression vs statement

There is another form of the if statement: the if __expression__.

    a = 5
    b = 12 if a < 10 else 42

The expression form of the conditional allows us to assign a value to a variable
in one line of code. It's just a shortcut for the longer if/else statements we've
worked with previously.

Both the `if` and `else` clauses are required. This is __not__ valid syntax:

    # not valid, missing else clause!
    b = 12 if a < 10

## Exercise

For example, back to the Subaru example, say you wanted to check both mpg and CO2PerYear
if mpg < 15 and CO2PerYear > 15000, then print "Biggest polluter ever"
Otherwise, print("Not bad")

The answer is in Lecture7SubaruIf3.py, but don't look at it until you've
worked through the code.


<cite>Lecture material by Rhonda Hoenigman.</cite>

