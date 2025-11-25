#File input and output in python(Notes by apnacollege)

#Python can be used to perform operations on a file.(read and write data)

#Type of all files:
#1 Text files: .txt,.docx,.log etc
#2 binary files:.mp4,.jpg,.mov etc 
#3 CSV(comma separted vaues) files:

# open,read and close a file:

# We have to open a file before reading and writing

#Syntax:
# f=open("Filename",mode)
# open() is built in function to open a file
# f is a file object 

#data = f.read()
# read() is a built in function to read data from a file

#f.close()
#close() for to close the file

#Different modes in file handling
# 1 "w" for write mode
# 2 "r" for read mode
# 3 "x" create a new file and open it for writing
# 4 "a" for append mode(Add data at the end of the file). cursor at the last of the file
# 4 "r+" for read and write from the file. cursor is in the begining from the file

# Reading from the file:
# 1 f.read()  read all data from the file
# 2 f.readline() read one line at a time
# 3 f.readlines() read all the lines from the file

#ChatGPT said:
#Bhai simple aur clear difference dekh:

#✅ read()

#Poora file ek hi string me read karta hai.
#Saari lines continuous string ban jaati hain.
 
# ✅ readlines()

#File ki har line ko ek list ke element me read karta hai.
#Har line ek string hogi. 

# With syntax:

# with open("File name",'mode') as f:
#  data=f.read()
#  print(data)

# It is not necessary to close the file when we are using with synatx,because it automatically close the file()

# Deleting a file:
# Using os module
# Module(like a code libaray) is a file written by another programmer that generally has a function we can use

# import os
# os.remove(filename)