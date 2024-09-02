# These are simple outputs with print() built in function
"""
print("Hello World")
print("Umair Sajawal")
print("Hello world,", "Its me Umair Sajawal")
print(32)
print(10+2)
print(10-2)
print(10*2)
print(10/2)
print(10%2)
"""
# This is variables in python. syntax: var_name = value
"""
name = "Umair Sajawal"
age = 21
price = 25.99
print(name)
print(name, age, price)
age2 = age
print(age2)
print("My name is :", name)
print("My age is :", age)

# type(): This is used now the type of the variable
print(type(name))
print(type(age))
print(type(price))
"""
# Datatypes in python:
"""
'''
1. Integer (+ve, -ve, 0)
2. String  ('hello' or "hello" or ''hello'')
3. Float   (for example: 25.5, 65.29, ...)
4. Boolean (only two conditions 1.True or 2.False. Note in boolean syntax T and F always write capital)
5. None    (for example: a = None, means want not to store any value in variable a)
'''
age = 25
old = False
a = None
print(type(age))
print(type(old))
print(type(a))
"""

# Simple sum code. Also arithmetic operators (+,-,*,/,%,**)
"""
a = 5
b = 4
sum = a+b
print(sum)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)  #Remainder
print(a**b) #power a^b
"""
# Relational / Comparison operators (==,!=,<,>,<=,>=)
"""
a = 50
b = 20
print(a == b) #False
print(a != b) #True
print(a >= b) #True
print(a > b)  #True
print(a <= b) #False
print(a < b)  #False
"""
# Assignment operators (=,+=,-=,*=,/=,%=,**=)
"""
num = 10
num += 10 #num = num + 10 
print(num)

num2 = 20
num2 *= 10 #num = num + 10 
print(num2)
...
"""
# Logical operators (and, not, or) Note: "not" operator work on single value while "and" and "or" works on two values
"""
print(not True)   #False
print(not False)  #True
a = 5
b = 3
print (not a > b) #output: False due to not operator

value1 = False
value2 = True
print("AND operator is :", value1 and value2)
print("OR operator is :", value1 or value2)
print("OR operator is :", (a == b) or (a > b))
"""

# Type Convertion (convert datatype to another datatype)

'''
 Two types of conversion : 1.conversion and 2.casting
 1.conversion: python automatically converts to true datatype
 2.casting: the user manually converts to another datatype
'''
'''
1. convertion method example:
'''
a = 2
b = 3.25
sum = a + b
print(sum)  #Output is: 5.25

c = "2"
d = 3.25
#sum = c + d
#print(sum)  #output is: error because in python string to float convertion not allowed (only in conversion (default) method).

'''
2. casting method example
Note: type casting is only works with integers or numbers like "3". and if write this "umair", it not works.
'''
a = int("2")
b = 3.25
sum = a + b
print(type(a))  #int
print(sum)      #Output is: 5.25

a = float("2")
b = 3.25
sum = a + b
print(type(a)) #float
print(sum)     #Output is: 5.25

a = 4.25
a = str(a)     #Convert float to string manually
print(type(a))
