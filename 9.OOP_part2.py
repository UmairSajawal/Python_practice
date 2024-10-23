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
1. Single Inheritance:        #base class -> derived class   #like previous example or car 
2. Multi-level Inheritance:   #base(parent class) -> derived(child class + parent class) -> derived(child class)
3. Multiple Inheritance:
# base(parent class)  base(parent class)
                     |
            drived(child class)
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
"""
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
"""

#3. Multiple Inheritance:
"""
class A:
    varA = "This is class A"

class B:
    varB = "This is class B"

class C(A, B):
    varC = "This is class C"

c1 = C()
print(c1.varC)  #Output : This is class C
print(c1.varB)  #Output : This is class B
print(c1.varA)  #Output : This is class A
"""

# Super Method
''' super() method is used to access methods of the parent class '''
"""
class Car:
    def __init__(self, car_type):
        self.car_type = car_type
    @staticmethod
    def start():
        print("Car started...")
    
    @staticmethod
    def stop():
        print("Car stopped...")
    
class ToyotaCar(Car):    #this class is inherited to the previous class "Car". So all things in class Car are accessible for new class "ToyotaCar(car)"
    def __init__(self, name, car_type):
        super().__init__(car_type)
        self.name = name
        super().start()

car1 = ToyotaCar("prius", "electric")
print(car1.car_type)  #Output : electric
print(car1.start)     #Output : Car started...
"""

# Class Method
''' 
A class method is bound to the class and recieves the class as an implicit first argument.
Note : static method not access or modify class state & generally for utility.

class Student:
    @classmethod    #decorator
    def college(cls):
        pass
'''
"""
class Person:
    name = "anomynous"
    
    #def changeName(self, name):
       # Person.name = name                   #this 1st way 
       # self.__class__.name = "Shahaan"      #this 2nd way
    
    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("Shahaan")
print(p1.name)      #Output : Shahaan
print(Person.name)  #Output : Shahaan
"""

# Property
''' We use property decorator on any method in the class to use the method as a property '''
'''
class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        self.percentage = str((self.phy+self.chem+self.math)/3) + "%"
stu1 = Student(99, 97, 98)
print(stu1.percentage)

#now if change phy marks, it changes successfully
stu1.phy = 86
print(stu1.phy) #Output: 86
#but percentage not change it remain same
print(stu1.percentage)


#so avoid to this situation, when change marks percentage also changes we use @propert decorator:
'''
"""
class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        

    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3) + "%"


stu1 = Student(99, 97, 98)
print(stu1.percentage)   #Output : 98.0%

stu1.phy = 86
print(stu1.phy)          #Output: 86
print(stu1.percentage)   #Output: 93.66666666666667%

#now when changed marks the percentage automatically changes

#read and practice @getter and @setter decorator
"""


# Polymorphism : Operator Overloading
'''
When same operator is allowed to have different meaning according to the conext.

Operators & Dunder functions:
a+b  #addition             a.__add__(b)
a-b  #subtraction          a.__sub__(b)
a*b  #multiplication       a.__mul____(b)
a/b  #division             a.__truediv____(b)
a%b  #remainder            a.__mod__(b)
'''
'''
# operator(+)
print(1 + 2)  #3
print("2" + "3") #23
print("umair" + "sajawal")    #concatenate  #umairsajawal 
print([1, 2, 3] + [4, 5, 6])  #merge        #[1, 2, 3, 4, 5, 6]
'''
''' 
complex number like : 3i + 4j
3i is real part
4j is imaginary part
'''
#make your own class:
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    
    def printNumber(self):
        print(self.real,"i +", self.img,"j")

    #now i want to add num1 and num2 so use dunder (__) function:
    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)
    
    #now i want to subtract num1 and num2 so use dunder (__) function:
    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)

num1 = Complex(1, 3)
print(num1.printNumber())  #Output : 1 i + 3 j

num2 = Complex(4, 6)
print(num2.printNumber())  #Output : 4 i + 6 j

num3 = num1 + num2
print(num3.printNumber())  #Output : 5 i + 9 j

num4 = num1 - num2
print(num4.printNumber())  #Output : -3 i + 9 j

#for read more dundent functions visit "doc.python.org"
