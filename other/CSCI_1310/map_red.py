#!usr/local/bin/python3

import urllib.request

urls = [
    "https://en.wikipedia.org/wiki/Batman",
    "https://en.wikipedia.org/wiki/Superman",
    "https://en.wikipedia.org/wiki/The_Joker_(The_Dark_Knight)"
]

keyword = "hero"

#Map urls into html page content.
pages = []
for url in urls:
	response = urllib.request.urlopen(url)
	#print(response)
	#print(response.getcode())

	if response.getcode() != 200:
		print("HTTP request failed", response.getcode())
		exit(1)
	body = str(response.read())
	#print(body)
	pages.append(body)

#Map html into keyword indexes.
indexes = []
for page in pages:
	occurrences = []
	index = page.find(keyword)

	if index != -1:
		occurrences.append(index)

	while index != -1:
		index = page.find(keyword, index + 1)
		if index != -1:
			occurrences.append(index)
	indexes.append(occurrences)

#Reduce index lists inot a sinle count of "hero"
#keyword on the page.
counts = []
for found in indexes:
	counts.append(len(found))

print("keyword counts", counts)