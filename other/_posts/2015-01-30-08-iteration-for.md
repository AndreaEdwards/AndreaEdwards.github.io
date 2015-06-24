---
layout: post
categories: lectures
title: Iteration over a collection
---

# Iteration over a collection

There is another kind of loop that is similiar to the `while` loops that is
used to iterate through a collection of items. You can also think of this
as looping over a collection, where each time through the loop, a
different item in the collection is being evaluated. This type of loop
is called an iterator and in Python it uses the keyword `for`.

## An example

    for letter in "hello world":
      print(letter)

In that example, the variable `letter` takes on the properties of each
item in the collection, in order. The collection in this case is the
string `"hello world"`. The first time through the loop, the
value of letter is `"h"`, the second time it is `"e"`, the third time it is
`"l"`, and so on, until the end of the collection is reached. This type of
loop will execute a fixed number of times, unlike the while loop which
will execute as long as the looping condition is true.

The variable `letter` is an arbitrary name, there's nothing special about
it. We could use:

    for puppies in "hello world":
      print(puppies)

and achieve the same result. It's noteworthy here that the iterator
variable, the letter and puppies in these examples, takes on the same
type as the type of the collection. In this case, they're strings.

Another type of collection is a sequence of numbers, such as 1,2,3,4,5.
Python has a built-in command for generating sequences of a specified
length called `range`.

    numbers = range(1,6)

numbers contains 1,2,3,4,5. The upper value is not included in the
sequence, but the lower value is.


    print(numbers)

To iterate through the collection, you do the same thing as when you
iterate over a collection of letters. In the example here, the value of
`x` each time through the loop is one of the items in numbers, one at a
time, in order. The first time through the loop, `x = 1`, the second time,
`x = 2`, and so on.

    for x in numbers:
      print(x)

    # We could also do something to the x variable in the
    # loop, such as x * 2
    for x in range(1,6):
      print(x * 2)


One of the other collection types we saw was a list. In a list, it's a
collection of items that can be of different types and we can iterate
over the list in the same way that we iterate over a string or a sequence
of numbers.

    myList = ['a', 2, 'puppies', 4]
    for item in myList:
      print(item)


You can also iterate over a collection by using the index of each item
in the collection. One way to do this is to incorporate the range command
into the for loop and use the range item as the index into the list

    for x in range(0, 4):
      print(myList[x])

In this example, the `x` will be a value in the sequence 0,1,2,3 in order,
so x can be used as the index of `myList`.

When you iterate over a collection, it's because you want to know
something about the items in the collection, or modify items in some
ways.

For example, you may want to count the number of times a letter
occurs in a sentence. In this example, the sentence is declared as a
string:

    sentence = "The quick brown fox jumped over the lazy dog"

    # for example, given the sentence,
    # The quick brown fox jumped over the lazy dog
    # How many times does the letter d appear

    # Think about the algorithm first.

    d = 0
    for letter in sentence:
      if letter == "d":
        d = d + 1
    print("there are ", d, "ds")

## Exercise

Using the sentence The quick brown fox jumped over the lazy dog,
How many of the letters in the sentence are vowels?
Answer is in Lecture9ForLoop.py
Think first about the algorithm.

<cite>Lecture material by Rhonda Hoenigman.</cite>

