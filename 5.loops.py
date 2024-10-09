# Loops in python
# Loops are used ti repeat instructions

#1. while loop:
'''
syntax:
while condition:
   # some work
'''
"""
count = 1
while count <= 5 :
    print("Umair")
    count += 1  #count=count+1
print(count)  

i = 5
while i >= 1 :
    print(i)
    i -= 1
print("Loop Ended")
"""
#Practice Set:
'''
x = 100
while x >= 1:
    print(x)
    x -= 1

n = int(input("Enter a number:"))
i = 1
while i <= 10 :
    print(i*n)
    i += 1


nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1

heroes = ["superman", "batman", "ironman", "spiderman", "thor"]
idex = 0
while idex < len(heroes):
    print(heroes[idex])
    idex += 1

num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 100
i = 0
while i < len(num):
    if(num[i] == x):
       print("Found at index", i)
    else:
        print("Founding")
    i += 1
'''

# Break & Continue
'''
-Break:  used to terminate the loop when encountered.
i = 1
while i <= 5:
    print(i)
    if(i == 3):
        break
    i += 1


-Continue: terminates execution in the current iteration & continues execution of the loop with the next iteration.
j = 0
while j <= 5:
    if(j == 3):
        j += 1
        continue  #skip
    print(j)
    j += 1
'''

# Loops in Python
#Loops are used for sequential traversal (travel). For traversing list, string, tuples etc.

# For Loop:

'''
for Loops Syntax:
    for element in list_name:   #for and in are keywords
        #some work
'''
"""
num = [1, 3, 4, 6, 10]
for val in num:
    print(val)
'''Output:
1
3
4
6
10'''

vegies = ["Potatoes", "Tomatoes", "Brinjals", "Bitter gourd"]
for values in vegies:
    print(values)
#for loop on tuple:
tup = (10, 20, 30, 52, 75)
for numbs in tup:
    print(numbs)

#for loop on string:
string = "Umair"
for variable in string: 
    print(variable)
'''Output:
U
m
a
i
r
'''
"""


'''
for Loop with else Syntax:
    for element in list_name: 
        #some work
    else: 
        #work when loop ends
#else used as it doesn’t execute when break is used
#else is used for display or print. Its working not simillar to other laguages else like of else
#the purpose of else in loop when we use break its not print else.The examples are given below:
''' 
"""
str0 = "umair"
for charac in str0:
    if(charac == "a"):
        print("a found")
    print(charac)
else:
    print("END")
'''Output:
u
m      
a found
a      
i      
r      
END 
'''

str1 = "sajawal"
for char in str1:
    if(char == "w"):
        print("w found")
        break
    print(char)
else:
    print("END")
'''Output:
s
a
j
a
w found
'''
#These both examples clear the benefit of use of else in for loop.
"""

# Practice Set:
'''
#Print the elements of the following list using a loop: 
allNum = [1, 4, 9, 16, 25, 36, 49, 64, 81,100] 
for var1 in allNum:
    print(var1)

#Search for a number x in this tuple using loop:
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 49
idx = 0
for el in nums:
    if(el == x):
        print("Found number x : ", idx)
        break
    idx += 1
'''

# Range()
#Range functions returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
#range( start(optional, by default strats from 0), stop, step(optional, by default strats from 1) )
"""
print(range(5))  #Output : range(0, 5)

'''Example:
if range is 5 and  want to print all numbers i write:

seq = range(5)
print(seq[0])
print(seq[1])
print(seq[2])
print(seq[3])
print(seq[4])

Output:
0
1
2
3
4
but i want to print through for loop in range so i write:
'''
seq = range(5)
for i in seq:
    print(i)
'''Output:
0
1
2
3
4

Now i want to print directly in range so:
'''
for num1 in range(7):   #range(stop) #1st number include and not included last number
    print(num1)
'''Output:
0
1
2
3
4
5
6
'''
for num2 in range(2, 10):  #range(start, stop) #1st number include and not included last number
    print(num2)
'''Output:
2
3
4
5
6
7
8
9
'''
for num3 in range(2, 10, 2):  #range(start, stop< step) #1st number include and not included last number
    print(num3)
'''Output:
2
4
6
8
'''
"""

# Pracice Set:
'''
#Print numbers from 1 to 100.
for num4 in range(101):
    print(num4)

#Print numbers from 100 to 1.
for num5 in range(100, 0, -1):
    print(num5)

#Print the multiplication table of a number n.
n = int(input("Enter a number:"))
for i in range(1, 11):
    print(i*n)
'''

# Pass Statement
# pass is a null statement that does nothing. It is used as a placeholder for future code.
'''
Syntax: 
for el in range(10): 
pass
'''
"""
for num6 in range(5)
     #empty   #Output : Error
    
for i in range(5):
    pass

if i <= 6:
    pass
print("Some Usefeul Work")
'''
In output with using "pass" it pause or skip the code.
Output:
Some Usefeul Work
'''
"""

# Practice Set:
#WAP to find the sum of first natural (5) numbers. (using while)
'''
n = 5
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("Total sum of number are: ", sum)

n = 5 
sum = 0
for i in range(0, n+1):
    sum += i
print("Total sum of number are: ", sum)

# WAP to find the factorial of first n numbers. (using for)
n = 5
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print("Factorial : ", fact)
'''
