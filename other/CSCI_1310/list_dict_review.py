#!usr/local/bin/python3

# given an english dictionary. for any given series of random
# letters, how do you find if there is an anagram of that word
# in the dictionary?

#  "cat" and "act"

words = {
	     "cat": "A friendly pet",
	     "act": "Something actors do",
	     "wolf": "A scary dog",
	     "fowl": "a bird"

}

# step 1. discard definitions because we don't need them
# step 2. reformat ...
# must get them all in the same order. need to sort words
# into letters

def sort(text):
	letters = list(text)
	letters.sort()
	return "".join(letters)


def process(words):
	mangle = {} # in this case key will be string and value will be list
	for word in words:
		sorted = sort(word)
		if sorted in mangle:
			mangle[sorted].append(word)
		else:
			mangle[sorted] = [word]
	return(mangle)



word = "tac"
print(sort(word))
print(process(words))

word = "tac"
sorted = sort(word)
new_dictionary = process(words)
english_words = new_dictionary[sorted]
print("anagrams for ", word, "=", english_words)





