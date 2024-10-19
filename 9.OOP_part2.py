# del keyword
'''
Used to delete object properties or object itself.

del s1.name  #delete object properties
del s1       #delete object
'''
"""
class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("umair")
del s1
print(s1)
"""

# Private(like) attributes and methods    (For example: public: private concept in C++ language)
#Conceptual Implementations in Python:
'''
Private methods and attributes are meant to be used only within the class and or not accessible from outside the class.
'''
