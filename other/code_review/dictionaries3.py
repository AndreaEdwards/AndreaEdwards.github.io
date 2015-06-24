
text = "the quick brown fox jumped over the lazy dog"

def frequency(text):
    counts = {}
    for character in text:
        if character in counts:
            counts[character] += 1
        else:
            counts[character] = 1
    return(counts)

counts = frequency(text)
print(type(counts))

print(len(counts))

import string
chars = list(string.ascii_lowercase)

for key in counts:
	print(key, counts[key])
	if key in chars: # can't remove something that isn't there
		chars.remove(key)
print("leftover letters", chars)


