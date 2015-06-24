#!usr/local/bin/python3

import sys

radius = sys.argv[0]
print(radius)
#circ = 2 * 3.14 * radius
#print("circumference: ", circ)

score = 10
if score < 10:
    print("NOW")
    if score > 2:
        print("RIGHT")
    elif score == 10:
        print("CHEER")
else:
    print("TIME")
print("GREAT")


#i = 8
#while i in range(10):
#    print(i)


total = 0
for i in range(31):
    total += i
print(total)

result = 5
print(result)
print("Result is %d: " % result)
sport = "kayaking"
print(sport + sport)
#print("one" + 2)
print("three", "four")


number = 3
while number < 30:
    number = number * 4
    print(number)
print(number)


for number in range(31):
    print(number)
    print("Odd") if number % 2 != 0 else print("Even")

x = int(input("What is x? "))
y = int(input("What is y? "))
z = int(input("What is z? "))

if x == y or y == z or x == y:
    equality = True
else:
    equality = False

if equality is False:
    if x > y and x > z:
        print("%d is maximum." % (x))
    if y > x and y > z:
        print("%d is maximum." % (y))
    if z > x and z > y:
        print("%d is maximum." % (z))
else:
    if x == y:
        if x > z:
            print("%d and %d are greater than %d." % (x, y, z))
        else:
            print("%d is maximum." % (z))
    elif y == z:
        if y > x:
            print("%d and %d are greater than %d." % (y, z, x))
        else:
            print("%d is maximum." % (x))
    elif x == z:
        if x > y:
            print("%d and %d are greater than %d." % (x, z, y))
        else:
            print("%d is maximum." % (y))

