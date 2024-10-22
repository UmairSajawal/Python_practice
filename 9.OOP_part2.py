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
"""
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass   #for making private write "__"on start of the word like __acc_pass
    
    def reset_password(self):    #but show private in function when call it
        print(self.__acc_pass)

acc1 = Account("12345", "abcde")
print(acc1.acc_no)
#print(acc1.__acc_pass)
print(acc1.reset_password()) #successfully display password in function

class Person():
    __name = "anomynus"

    def __hello(self): #this isprivate function and not called directly but possible to call and display in another function
        print("Hello everyone...")
    
    def welcome(self):
        self.__hello()

p1 = Person()
print(p1.welcome())
"""


# Inheritance
'''
When one class(child/derived) drives the propertyies & methods of another class(parent/base). 

class
    class Car
       ...

    class ToyotaCar(Car):
        ....
'''
# Types Of Inheritance
'''
1. Single Inheritance        #base class -> derived class   #like previous example or car 
2. Multi-level Inheritance   #base(parent class) -> derived(child class + parent class) -> derived(child class)
3. Multiple Inheritance
'''

"""
#1. Single Inheritance:
class Car:
    color = "Black"
    @staticmethod
    def start():
        print("Car started...")
    
    @staticmethod
    def stop():
        print("Car stopped...")
    
class ToyotaCar(Car):    #this class is inherited to the previous class "Car". So all things in class Car are accessible for new class "ToyotaCar(car)"
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("Revo 4x4")
car2 = ToyotaCar("Fortuner")

print(car1.name)    #Output : Revo 4x4
print(car2.name)    #Output : Fortuner
print(car2.color)   #Output : Black
print(car1.start()) #Output : Car started...
print(car1.stop())  #Output : Car stopped...
"""

#2. Multi-level Inheritance:
class Car:
    @staticmethod
    def start():
        print("Car started...")
    
    @staticmethod
    def stop():
        print("Car stopped...")
    
class ToyotaCar(Car):  
    def __init__(self, brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self, car_type):
        self.car_type = car_type

car1 = Fortuner("Petrol")
car1.start()
