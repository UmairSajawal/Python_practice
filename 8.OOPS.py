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
'''
class Student:
    name = "zubair"
    def __init__(self):    #(self) basically point to Student()
        print("adding new student in the databse...")
    
s1 = Student() #Output when run this code: adding new student in the databse...
#counstructor invoke automatically

