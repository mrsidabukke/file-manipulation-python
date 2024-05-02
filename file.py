# Description: This file is used to write data to a file

# file = open("data.txt", "w")
# file.write("Hello World")

# this is how to read a file

# file = open("data.txt", "r")
# print(file.read())

# this is how to write and read a file

file = open("data.txt", "a+")

file.write("Hello World\n")

file.seek(0)

text = file.read()
print(text)
