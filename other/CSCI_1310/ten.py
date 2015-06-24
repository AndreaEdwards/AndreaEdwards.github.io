#!/usr/local/bin/python3

text = "The quick brown fox jumped over the lazy dog."

print(text[0:3])
print(text[0:])

print(text[:])

#Because strings are a collection, we can iterate through them
for character in text:
	print("character is", character)

index = 0
while index < len(text):
	character = text[index]
	print("character is", character)
	index += 1

index = text.find("fox")
print("index is", index)

#what's the difference between object and variable?
#variable is the name that points at an object

how_many = text.count("fox")
print("count is", how_many)

elephant = text.replace("fox", "elephant")
print("replaced text is", elephant)
print("original is", text)

#formatting
number = 22.3
some_string = "the number is %f and %.2f" % (22.3, number)
print("some string is", some_string)

formatted = some_string.format(number, 22.3)
print("formatted is", formatted)

some_string = "the number is {:>10f}"
formatted = some_string.format(number, 22.3)
print("formatted is", formatted)

some_string = "the number is {:>15f}"
formatted = some_string.format(number, 22.3)
print("formatted is", formatted)

#how similar are two different strings?
text1 = "The quick brown fox jumped over the lazy dog."
text2 = "The quick brown ant jumped over the lazy dog."
#text2 = "The quick brown elephant jumped over the lazy dog."

#Hamming distance
distance = 0
length = len(text1)
for x in range(0, length):
	character1 = text1[x]
	character2 = text2[x]
	print("1 is ", character1, "2 is ", character2)
	if character1 != character2:
		distance += 1

print("distance is", distance)

text1 = "david.malcom.graham@gmail.com"
text2 = "david.malcom.graham-text1@yahoo.com"

at = text1.find("@")
text1 = text1[0:at]

at = text2.find("@")
text2 = text2[0:at]

print("text1 is now", text1)
print("text2 is now", text2)

distance = 0
length = len(text1)
for x in range(0, length):
	character1 = text1[x]
	character2 = text2[x]
	print("1 is ", character1, "2 is ", character2)
	if character1 != character2:
		distance += 1

print("distance is", distance)

###turn string into array (list)

fox = "The quick brown fox jumped over the lazy dog."
word = fox.split(" ")
#below also works because white space is default value
# word = fox.split()
print("word list is", word)
sentence = " ".join(word)
#bad == sentence = words.join(" ")
print("sentence is", sentence)

#give an exit code
#exit(20)
#return exit code
#ten.py && $?

#if everything worked return 0 else 1