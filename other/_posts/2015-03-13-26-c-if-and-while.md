---
layout: post
categories: lectures
title: C++ conditional branches
---

# C++ condtional branches

We discussed data type sizes and what happens when a type overflows its maximum
value. We also covered conditional logic with `if` statements and loops.

    #include <iostream>
    #include <string>

    using namespace std;

    int main() {
        float my_float = 0.0;
        double my_double =  0.0;

        int my_int = 0;

        long my_long_int = 0;
        short my_short = -12;

        char my_char = '\n';
        bool my_boolean = true;

        /* signed long age = 65535; */
        signed short age = 32767;
        age += 1;
        /* age = age + 1; */
        /* age++; */



        string name = "12000";
        int converted = stoi(name);

        cout << "conversion is " << converted << endl;

        cout << "vampire's age is " << age << endl;

        cout << "int = " << sizeof(my_int) << endl;
        cout << "float = " << sizeof(my_float) << endl;
        cout << "long = " << sizeof(my_long_int) << endl;
        cout << "short = " << sizeof(my_short) << endl;
        cout << "char = " << sizeof(my_char) << endl;
        cout << "bool = " << sizeof(my_boolean) << endl;
        cout << "double = " << sizeof(my_double) << endl;


        int answer = 12;
        int i = 0;
        while (i < 10) {
            int guess;
            cout << "What is your guess? ";
            cin >> guess;

            if (guess < answer) {
                cout << "Too low!" << endl;
            } else if (guess > answer) {
                cout << "Too high!" << endl;
            } else {
                cout << "WINNER!" << endl;
                break;
            }
            i++;
        }

        cout << "Game over." << endl;
        return 0;
    }
