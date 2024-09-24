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
"""
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
"""

# Tuples in python
# Note: Tuples are immutable while list are mutable
""""
'''Use () brackets in tuples'''
tup = (1,2,3,5)
tup1 = ()
print(tup1)  #Output: ()
tup2 = (1,)  
print(tup2)  #Output: (1,)
tup3 = (1)  

print(tup3)  #Output: 1. Python understand that this is an integer if you not separate through comma. 
#if write (1.0) understand as float and if write ("hello") understand as string

print(type(tup))
print(tup[0])
print(tup[1])
''' tup[0] = 5 # Not allowed because tuples are immutable (not change) '''
# Tuple slicing method same as the method of list slicing
"""

# Tuple Methods
"""""
tup0 = (2, 1, 3, 1)
tup0.index(3) #Returns the index of the first occurrence. tup0.index(1) is 1. This is use to find index number.
print(tup0.index(3))  #Output: 2

tup0.count(1) #Count total occurrence. how many time exists in tuple. tup0.count(1) is 2 times.
"""

# Pracite Set
'''
movies = []
movie1 = input("Enter first favorite movie name ;")
movie2 = input("Enter second favorite movie name ;")
movie3 = input("Enter third favorite movie name ;")
movies.append(movie1)
movies.append(movie2)
movies.append(movie3)
print(movies)  # Output:  ['carry on jatta', 'load wedding', 'chal mera put']
'''
list1 = [1,2,3,2,1]
list_copy = list1.copy()
list_copy.reverse()
if (list_copy == list1):
    print("Palindrome")
else:
    print("No palindrome")
    
grade = ["b", "c", "d", "a", "e"]
grade.sort()
print(grade) #Output: ['a', 'b', 'c', 'd', 'e']
