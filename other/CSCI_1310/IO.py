#!usr/local/bin/python3

#touch bears
#ls -ls
#echo polar > bears
#ls -l bears
#cat bears
#echo koala > bears
#cat bears
#echo polar >> bears
#cat bears

#write python code that mimics above terminal commands
print("File IO")

#open returns a file object. read() and write() are methods that can be called on file objects

file = open("bears")
#files are iterable
for line in file:
	print("this bear is:\n", line)
file.close()


file = open("bears")
#readlines returns a list
bears = file.readlines()
print("bears list is: ", bears)

#another way to read in content is with read() this gives you a string back
content = file.read()
print("file content is ", content)
print(content)
file.close()

#now write to file w = write, r = read, a = append, rw = read and write
#this erases all content and overwrites file
file = open("bears", "w")
file.write("sloth")
file.close()

#this appends into
file = open("bears", "a")
file.write("grizzly")
file.close()

file2 = open("bears", "r")
print(file2.read())

#file = open("bears", "rw")
#print("current contents are", file.read())

#chmod (change mode; or change permissions)
#if you run chmod 000 you get rid of all permissions to do anything
#if you run chmod 777 you grant all permissions
#r = read, w = write, x = execute
#chmod u-x demo.py (u = user subtraction removes the execute permission)
#chmod u+x demo.py (addition adds back the permission to execute the file)
#cat command reads in file and prints it out or if you give cat filename > filename
# then the > symbol redirects output into the second file

#recreate cat command in python
file1 = open("/Users/Andrea/Desktop/panda.txt")
file2 = open("bears")

output = open("/Users/Andrea/Desktop/cat-results", "w")

content1 = file1.read()
content2 = file2.read()

output.write(content1 + content2)
output.close()
file1.close()
file2.close()

#mkdir is make directory

#note: unix treats everything as a file. including mice, keyboards, and websockets. google this.


