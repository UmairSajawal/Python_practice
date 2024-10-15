# File Input/Output
'''
 Python can be used to perform operations on a file. (read & write data)
 Types of all files:
 1.Text Files :    .txt, .docx, .log etc.
 2.Binary Files :  .mp4, .mov, .png, .jpeg etc
 '''

# Open, read & close File
'''
We have to open a file before reading or writing.
f = open( “file_name”, “mode”)  => syntax

examle:
file_name = sample.txt,  demo.docx    
mode = r : read mode,  w : write mode

data = f.read( )
f.close( )
'''
"""
f = open("demo.txt", "r")    #r means read mode  #if file is not in same folder then write complete path
data = f.read()              #if you want print limited characters like "f.read(5)", this prints only first five characters.
print(data)
print(type(data))

f.close()

'''Output:
Hello i am umair sajawal and trying to learn  python
<class 'str'>
'''
"""

# Reading a file :    data = f.read( )
#reads entire file:   data = f.readline( ) #reads one line at a time
"""
f = open("demo.txt", "r")

line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

f.close()
'''Output:
Hello i am umair sajawal 

and i'm trying to learn  python
'''
"""


"""
'''
f = open("demo.txt", "w")  #for rewrite use "w" and for write at the last use append "a"
f.write("I want to learn javascript tomorrow. 123")
f.close()
'''
f = open("demo.txt", "a")  #for rewrite use "w" and for write at the last use append "a"
#f.write("now learn ReactJS")
f.write("\n now move to nodejs")
f.close()
'''Output on demo.txt after run this code the output is:
I want to learn javascript tomorrow. 123now learn ReactJS
now move to nodejs
'''

f = open("demo.txt", "r+") #read and write both  #for overwite on start
f.write("abc")
print(f.read())
f.close()
'''Output:
abcant to learn javascript tomorrow. 123now learn ReactJS
now move to nodejs
'''
"""
# for reading more modes like w+, a+, etc... read documentation


#with Syntax
"""
with open("demo.txt", "r") as f:
    data = f.read()
    print(data)  #close() is not compulsory because "with" already create this function automatically

'''Output:
abcant to learn javascript tomorrow. 123now learn ReactJS
now move to nodejs
'''
"""

# Deleting a File
"""
using the os module
Module (like a code library) is a file written by another programmer that generally has
a functions we can use.

import os  #pre installed module
os.remove("filename")  # filename like sample.txt  #this function remove this file
"""

# Practice set:
#Create a new file “practice.txt” using python. Add the following data in it: 
'''
Hi everyone
we are learning File I/O
using Java. 
I like programming in Java.
'''
"""
with open("practice.txt", "w") as f:
    f.write("Hi everyone\nwe are learning File I/O\n")
    f.write("using Java\nI like programming in Java")
"""

#WAF that replace all occurrences of “java” with “python” in above file.
"""
with open("practice.txt", "r+") as f:
    data = f.read()
    print(data)

new_data = data.replace("Java", "python")
print(new_data)
'''Output:
Hi everyone
we are learning File I/O
using python
I like programming in python
'''
"""

# Search if the word “learning” exists in the file or not.
"""
def check_for_word():
    word = "learning"
    with open("practice.txt", "r+") as f:
        data = f.read()
        if(data.find(word) != -1):
            print("Found")
        else:
            "Not Found"

check_for_word()
"""

#WAF to find in which line of the file does the word “learning”occur first. 
#Print -1 if word not found. 
"""
def check_for_line():
    word = "xlearning"
    data = True
    line_no = 1
    with open("practice.txt", "r+") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
    return -1
#check_for_line()
print(check_for_line())
"""

#From a file containing numbers separated by comma, print the count of even numbers.
"""
count = 0
with open("practice.txt", "r") as f:
    data = f.read()
    nums = data.split(",")
    for val in nums:
        if(int(val)%2 == 0):
            count += 1
print(count)
"""
