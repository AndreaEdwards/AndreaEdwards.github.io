---
layout: post
categories: lectures
title: Final exam review
---

# Final exam review

A selection of sample exam questions with answers.

## Sample questions

1. Convert each of the following expressions into C++ expressions:

   - 4 times x to the 4th power plus 5 all divided by 23

          (4 * pow(x, 4) + 5) / 23

   - 0 ≤ b and b ≠ 5

          b >= 0 && b != 5

2. What does the following code print?

        int score = 25;
        cout << score % 9;
        cout << "BOOK" << endl;
        if (score < 25 || score > 0) {
            cout << "FLOW" << endl;
            if (score != 25)
                cout << "PHONE" << endl;
        } else
            cout << “GOOD” << endl;
        score++;
        if (score == 25)
            cout << "KEYS" << endl;

   Answer:

        7BOOK
        FLOW

3. Write one line of code to declare an integer constant named `BIG` and
   assign it the value 347.

        const int BIG = 347;

4. Write the code to prompt the user for a number, and store the result
   in an integer variable named quantity.

        int quantity;
        cin >> quantity;

5. Write the code to read in the first command-line argument and store it
   into an integer variable named `frequency`.

        int main(int argc, char *argv[]) {
            int frequency = stoi(argv[1]);
            return 0;
        }

6. What is the correct way to assign the address of `name` to the pointer
   variable `ptr`?

        int *ptr;

   - a)	*ptr = &name;
   - **b)	ptr = &name;**
   - c)	ptr = %name;
   - d) None of these

7. Write a function named `getStart` that takes a string as a parameter and
   returns a string with the first 3 characters of that string. Assume
   the string parameter has 3 or more characters in it. You must use the
   return keyword in your solution.

        string getStart(string text) {
            return text.substr(0, 3);
        }

        // Alternative solution.
        string getStart(string text) {
            string result = "";
            result += text[0];
            result += text[1];
            result += text[2];
            return result;
        }

8. Given an array of string named `teammates` that contains `NUM_PLAYERS` number of
   names in the list, write a loop to print out each element in the array as a
   comma-separated list.

   For example, a list with three names in it may look like
   `Sue, Marty, Jo`, and a list with two names may look like `Sam, Jax`.
   Do not put an extra comma in the beginning or end of the output list!

        for (int i = 0; i < NUM_PLAYERS; i++) {
            cout << teammates[i];
            if (i < NUM_PLAYERS - 1) {
                cout << ", ";
            }
        }
