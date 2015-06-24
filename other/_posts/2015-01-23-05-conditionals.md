---
layout: post
categories: lectures
title: Conditional expressions & relational operators
---

# Conditional expressions & relational operators

In recitation this week, you worked with command-line arguments, which
provide a way for passing information into your program. The user is
able to give inputs that your code then uses in some way. Using the
command-line arguments in your code required a few things that we haven't
discussed yet, but will now. Here was the code from recitation:

    import sys
    radius = float(sys.argv[1])
    circ = 2 * 3.14 * radius
    area = 3.14 * radius ** 2
    print("circumference:", circ)
    print("area:", area)

The first line in the code is an import statement: `import sys`. The Python interpreter
has a set of base commands that it will recognize built-in.

When you write code in your text editor and save
the the file as a `.py`, you automatically get access to that base set and you
can use those commands in your code. But, those commands are not the
extent of the Python language. There are many, many more commands stored
in libraries that can be included in your program. You just need to import
the library that contains those commands.

The import statement here is
importing the `sys` library, which includes commands for interacting with
the interpreter and the system on which the code is running. This is a
way to get access to the operating system of the computer, or the name
of the running file, for example.

The second line: `radius = float(sys.argv[1])` is using one of the sys
library commands to get the command-line argument for the program. The
syntax here is to use the name of the library, then ., and then the
name of the command. argv is a list of command-line arguments, where
argv[0] is used by Python to store the name of the program, and argv[1]
is the first command-line argument. You could have an argv[2], argv[3],
etc, if you needed them in your program.

To see that argv[0] really is the name of the program, print it.

    print(sys.argv[0])

### Conditional expressions

In the programs we've written so far, there has been one path through
the code. In the code listed above, for example, first the import sys
line executes, then the radius = float(sys.argv[1]) line executes, and then
the circ line, then the area line, and then each of the print statement
lines, in order. Every time you run this code, the code will always run
in that order, and all lines will run.

However, most of the time in programming, you will want to execute one
set of code in some cases and another set of code in other cases. You can
also think of this as under certain conditions, one block of code will
run and under another set of conditions a different block of code.

To run different code under different conditions, we need to generate a
branch in the code, where each branch is controlled by whether a
condition is true or false. We do this with an if statement, where one
branch of the code executes if a condition is true and other branch
executes if the condition is false.

The syntax looks like this:

    a = 3
    if a < 4:
        print("a is less than 4")

    print("program done")

The conditional is the if a < 4: We create a variable "a" so that it can
be used in the if statement. The value of a is 3, since we've set it to
3. In the next line, the expression a < 4 will evaluate to True, and the
code that is indented under the if statement will execute. When we run
this code, you will see "a is less than 4" printed to the screen.

Notice the if statement syntax. It starts with word if, this is a Python
keyword, and it's built into the language that the next expression is
what will be evaluated. Following the if keyword is the variable name,
followed by the relational operator, and then what the variable is being
checked against, in this case 4. The colon signifies the end of the
statment and the indentation is used to signify what executes if the
statement is true. Everything indented will execute.

The `print("program done")` is not required, but it lets us know that the
code did run even if the print statement inside the if block didn't.

### Relational operators

There are many different relational operators available:

- `<` less than
- `>` greater than
- `<=` less than or equal to
- `>=` greater than or equal to
- `==` equal to
- `!=` not equal

These relational operators all before the same task of specifying
a relation in an if statement, that is then evaluated to be true or false.

For example, to check if a is equal to 3, you use

    # Notice the ==
    if a == 3:
        print("a equals 3")

There's a difference between `=` and `==`. The single `=` is the *assignment* operator
and binds a value to a variable name. The double `==` is the *comparison* operator and
tests equivalence.

    # another example using the <=
    if a <= 5:
        print("a is less than or equal to 5")

With the if statements so far, there's only one branch, we only do
something if the condition is true. But, what if you want to do one thing
if something is true, and something else if it's false. You can think of
this if something is true then do X, else do Y. The syntax matches this
logic, here is an example

    a = 5
    if a < 4:
        print("a is less than 4")
    else:
        print("a is greater than or equal to 4")

When the code runs, first the if statement will be evaluated, and since
a = 5, it is not less than 4. This will make the if evaluate to false
and the code in the if block will not execute. The else block will
execute because there are no conditions on it. The only time it doesn't
run is when the if is true. If the if is false for any reason, the else
is the alternative path in the code execution.

### Exercise

Write a program that asks for an input number. If the number is less than 100,
print "your number is less than 100". Otherwise, print "your number is greater
than 100".

<cite>Lecture material by Rhonda Hoenigman.</cite>

