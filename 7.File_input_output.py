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
