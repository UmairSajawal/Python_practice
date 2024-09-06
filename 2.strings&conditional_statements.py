# Strings
# For new line use escape character \n to move to next line
# For tab space use escape character \t to move to give space beteen two words
"""
str1 = "This is a string variable.\nI am Umair Sajawal"
print(str1)
str2 = "This is a second string variable.\tI am Umair Sajawal"
print(str2)
"""


# Strings basic operations (1.concatenation & 2.legnth of str)
# 1.Concatenation:
"""
str1 = "Hello"
str2 = "World"
final_str = str1 + str2
print(final_str)  #Output: HelloWorld
"""
# 2.Length os str
"""
str1 = "Python"
len1 = len(str1)
print(len1)

str3 = "umair"
str4 = "sajawal"
final_string = str3 + " " + str4
print(len(final_string))   #Output is: 13. Because space is also count
"""


# Indexing. Starts from 0 [0,1,2,3,4,....]
"""
str4 = "umair sajawal"
print(str4[4]) 
"""


# Slicing : Accessing parts of the string. syntax:
# srt[starting_index : ending_index]. Note: starting index included but ending index is not incuded
"""
str = "python developer"
print(str[1:5]) #output is : ytho
'''Negtive index. starts from last from -1 to so on ... like [-5,-4,-3,-2,-1]. and other method same as positive''' 
str6 = "hello"
print(str6[-5:-1]) #output is : hell
"""

# String Functions
"""
'''
str = "i am a coder"
str.endswith("er.") #Returns true if string ends with substr. Means the words match output is true otherwise false
str.capitalize( ) #capitalizes 1st char
str.replace( old, new ) #replaces all occurrences of old with new
str.find( word ) #returns 1st index of 1st occurrence
str.count(“am“) #counts the occurrence of substr in string. Inshort, how many time occurthe words

'''
str = "i am a developer"
print(str.endswith("er")) #output : True
print(str.capitalize())   #output : I am a developer

print(str.replace("developer", "programmer"))  #output : i am a programmer
print(str.replace("a", "e"))  #output : i em e developer

print(str.find("o"))      #output : 12
print(str.count("am"))    #output : 1. because "am" occurs only for one time
"""


# Practice set
"""
str = input("Write your name : ")
print(str)
str0 = len(str)
print(str0)

str7 = "$ How are u ?"
print(str7.count("$"))
"""

# Conditional Statements
# if-elif-else (syntax). Use unlimited ifs or elifsbut else only one time use only
"""
str = "green"
if(str == "red"):
    print("Stop")
elif(str == "yellow"):
    print("Wait")
elif(str == "green"):
    print("Go")
else:
    print("Light is broken.")

age = 21
if(age >= 18):
    print("You are eligible to drive")
else:
    print("Not eligible")

marks = int(input("Please enter yiur marks :"))
print(marks)
if(marks >= 90):
    print("A")
elif(marks < 90 and marks >= 80):
    print("B")
elif(marks < 80 and marks >= 70):
    print("C")
elif(marks < 70 and marks >= 60):
    print("D")
else:
    print("F")
"""

# Nesting
"""
'''Imagine if you age is 80 or 80+ you cannot drive'''
age = 25
if(age >= 18):
    if(age >= 80 ):
        print("You cannot drive")
    else:
        print("You can drive")
else:
    print("You cannot drive")
"""

# Prctice set:
"""
num = int(input("Write a number to check even or odd"))
print(num)
if((num%2) == 0):
    print("Even")
else:
    print("Odd")

num1 = int(input("Write a first number:"))
num2 = int(input("Write a second number:"))
num3 = int(input("Write a third number:"))
if(num1 > num2):
    print("First entered number is greatest")
elif(num2 > num3):
    print("Second entered number is greatest")
else:
    print("Third entered number is greatest")

num1 = int(input("Write a number ckeck is multiple of 7 or not:"))
if((num1%7) == 0):
    print("The number is multiple of 7")
else:
    print("Not multiple of 7")
"""