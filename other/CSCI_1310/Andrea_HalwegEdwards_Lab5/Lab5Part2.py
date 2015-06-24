#!usr/local/bin/python3

myString = "Hi, my name is FirstName LastName."

name_index = myString.find('name')

print("The starting index of 'name' is: ", name_index)


myString = myString.replace('FirstName', 'Andrea')
myString = myString.replace('LastName', 'Halweg-Edwards')
print(myString)

myWordList = myString.split(' ')
for word in myWordList:
    lowercase = word.lower()
    print(lowercase)