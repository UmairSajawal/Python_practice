# Lists in python. lists are similliar to array but not same concept in C++ and JavaScript
# Can store multiple datatype data in one string like [int, float, string, ...]
# Strings are immutable (not change) in python but mutable in lists.
"""
marks = [20.5, 50.2, 23,0 ,80.7]
print(marks)
print(len(marks))  #Output : 5
print(type(marks)) #Output : list
print(marks[0])    #Output : 20.5
print(marks[1])    #Output : 50.2

'''
# Try to change string direct:
str = "hello"
print(str[0])
str[0] = z #Output : error....
'''

student = ["Saad", 90, "Sialkot"]
print(student)
print(student[0])     #Output : Saad
student[0] = "Umair"
print(student[0])     #Output : Umair
print(student)        #Output : ['Umair', 90, 'Sialkot']
"""


# List Slicing. similiar to string slicing method. postive and negative index method also same.
# Syntax: list_name[starting_idx : ending_idx] #ending index is not include.
"""
marks = [10, 20, 60, 56, 80]
print(marks[1:4])   #Output : [20, 60, 56]
print(marks[-3:-1])   #Output : [60, 56]
"""

# List Methods or Functions

list = [2, 1, 3]
'''
list.append(4)  #adds one element at the end  [2, 1, 3, 4]

list.sort( )  #sorts in ascending order [1, 2, 3]

list.sort( reverse=True )  #sorts in descending order [3, 2, 1]. Also works on string like 'a', 'b', ...

list.reverse( )  #reverses original list [3, 1, 2]
'''
#list.insert( idx, el )  #insert element at index : .For example, i want to add 5 at 1 index so:
list.insert(1,5)
print(list)  #Output : [2, 5, 1, 3]

list2 = [2, 1, 3, 1]
list2.remove(1)  #removes first occurrence of element
#list2.pop( idx )  #removes element at idx 
list2.pop(2)

'''read more function from: python documentation'''