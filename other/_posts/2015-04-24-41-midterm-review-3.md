---
layout: post
categories: lectures
title: Midterm 3 review
---

# Midterm 3 review

This is a sample of the types of questions that will appear on the
third midterm exam. We'll discuss them in class together. Answers are
**in bold**.

## Sample questions

1. The double colon `::` is known as the **scope resolution** operator.

1. Who can access private members in a class? **Only member functions (a.k.a. methods).**

1. The name of a constructor is the same as the name of the **class**.

1. In the following class constructor definitions, the part of the header
   starting with a single colon is called the **initialization list**. What does this do?

       BankAccount::BankAccount() : balance(0), interest(0.0)

   **Assigns 0 to the balance member variable and 0.0 to the interest member.**

1. A class in which modifications to the implementation appear to be invisible
   to the user of the class is known as an **abstract data type**. Hint: ADT.

1. A member function that allows the user of the class to find out the value
   of a private data type is called a **getter or accessor**.

1. What can a constructor return? **Nothing.**

1. The constructor of a class that does not have any parameters is called
   a **default** constructor.

1. In the statement `cout << *p1;`, the `*` is called the **dereference operator**.

1. Write the code to declare a dynamic array of strings (use the string
   pointer variable `p1`) that has as many elements as the variable `arraySize`.

        string *p1 = new string[arraySize];

1. A **pointer** is the memory address of a variable.

1. Declare a pointer variable, named `ptr`, to an integer.

        int *ptr;

1. The `&` operator is called the **address-of operator**.

1. Write the code that assigns to `p1` (an integer pointer variable) the
   pointer to a dynamically created integer.

        int *p1 = new int;

1. Dynamic variables are created at **the heap**.

1. Write the code to return the dynamic memory pointed to by `p1` to
   the freestore.

        delete p1;

1. Write the code to declare an array of 10 doubles named `list`.

        double list[10];

1. How many indexed variables does the following array have? **9.**

       int myArray[] = { 1, 2, 3, 6, 5, 4, 7, 1, 1 };

1. Write the declaration for a function named `fn1` that expects an array of
   floats, the number of elements in the array, and does not return any value.

        void fn1(float values[], int length);

1. The modifier that guarantees that an array argument will not be changed is called **const**.

1. The computer remembers the address of which indexed variable(s) in an array?
   **The first element.**

1. An **array** is used to process a collection of data, all of which are the same
   type. Hint: `int a[10]`

1. What is the correct way to call the following function? Assume that you have
   two variables named `intArgument` (int) and `floatArgument` (float).

       void doThings(float x, int y);

   **doThings(floatArgument, intArgument)**

1. Given the following function definition fragment, for which values of
   `myInt` should the function be tested? Hint: 3 values.

       int doSomething(int myInt) {
           if (myInt < 0) {
               // do some stuff here
           }
       }

   **-1, 0, 1**

1. The variables passed to a function are called **arguments or parameters**.

1. A function that does not return a value is known as a **void** function.

1. Write the correct C++ code to convert the value in an integer variable named
   `count` to a `double`. (There is an older way that still works but is not
    considered correct C++).

    **static_cast<double>(count);**

1. Converting from one type to another is called **casting**.

1. What is the value of `(pow(2, sqrt(9.0) + ceil(0.99)))`? **16**

1. What is the output produced by the following code fragment?

       int i = 3;
       cout << "The value of i is " << sqrt(pow(i, 4.0)) << endl;

   **The value of i is 9**
