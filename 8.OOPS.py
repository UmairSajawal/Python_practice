# OOP in Python
'''
To map with real world scenarios, we started using objects in code.
This is called object oriented programming.
'''
# Class is a blueprint for creating objects.
'''
#creating class
class Student:   
name = “ahemd ali”

#creating object (instance)
s1 =  Student( )
print( s1.name )
'''
"""
class Student:          #class
    name = "umair"      #every student name in class is "umair"

s1 = Student()   #object   
print(s1.name)   #Output: umair

s2 = Student()   #object   
print(s2.name)   #Output: umair


class car:
    color = "blue"
    brand = "mercedes"
car1 = car()
print(car1.color)
print(car1.brand)
"""

# Class & Instance Attributes
'''
Class.attr
obj.attr
'''


# _ _init_ _ Function
'''
Constructor: #invoke(execute) when object is creted
All classes have a function called __init__(), which is always executed when the object is being initiated.
 
#creating class
class Student: 
def __init__(self, fullname):
self.name =  fullname

#creating object
s1 =  Student( “khuram” )
print(s1.name) 

The self parameter is a reference to the current
instance of the class, and is used to access variables
that belongs to the class.
'''

"""
class Student:
    name = "zubair"
    def __init__(self):    #Default Constructor  #(self) basically point to Student()
        print("adding new student in the databse...")
    
s1 = Student() #Output when run this code: adding new student in the databse...
#counstructor invoke automatically

class Student:
    def __init__(self, fullName):   #Parameterized Constructor()
        self.name = fullName
        print("adding new student in database...")
s1 = Student("Umair Sajawal")
print(s1.name)    #Output : Umair Sajawal


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new record in database")
s1 = Student("jameel ahmed", 80)
print(s1.name, s1.marks)

s2 = Student("Shahaan jutt", 90)
print(s2.name, s2.marks)
"""

#Methods
'''
Methods are functions that belong to objects.

#creating class
class Student: 
    def __init__( self, fullname ):
    self.name =  fullname
def hello( self ):
print( “hello”, self.name)

#creating object
s1 =  Student( “karan” )
s1.hello( )
'''
"""
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new record in database")

    def welcome(self):
        print("Welcome student...", self.name)
    
    def get_marks(self):
        return self.marks

s1 = Student("ahmed tahir", 70)
s1.welcome()
print(s1.get_marks())
'''Output:
adding new record in database
Welcome student... ahmed tahir
70
'''
"""

# Practice Set:
'''
Create student class that takes name & marks of 3 subjects as arguments in constructor. 
Then create a method to print the average.
'''
"""
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi", self.name, "your average score is:", sum/3)

s1 = Student("Umair Sajawal", [99, 98, 97])
s1.get_avg()

s1.name = "shahaan"  #directly change attribute name possible
s1.fet_avg()
"""

# Static Methods
'''
Methods that don’t use the self parameter (work at class level)
class Student: 
    @staticmethod   #decorator
    def college( ):
        print( “ABC College” )

Decorators allow us to wrap another function in order to
extend the behaviour of the wrapped function, without
permanently modifying it
'''
"""
class student:
    def college():
        print("ABCD College") #Output : Error. beacuse this is not static method.

class student:
    @staticmethod   #decorator
    def college():
        print("ABCD College") 
s1 = student()
s1.college()  #Output:  ABCD College
"""

# Important:
#Abstraction
''' Hiding the implementation details of a class and only showing the essential features to the user '''
