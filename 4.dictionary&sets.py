# Dictionary in python
# Dictionary is mutable (changeable), unordered (no any index number) and don't allow duplicate keys.
# If you want to find index write dict_name[key_name]
'''To know in detail read notes from git hub'''
""""
info = {
    "key" : "value",
    "name" : "umair",
    "age" : 21,
    "is_adult" : True
}
print(info)  #Output: {'key': 'value', 'name': 'umair', 'age': '21', 'is_adult': 'true'}

'''if u want to add lists or tuple you can use easily'''
dic = {
    "name" : "umair",
    "subjects" : ["computer sci", "maths", "physics"],  #List
    "marks" : (90, 80, 70), #Tuple  
    "is_child" : False,
    "age" : 21,
    30.0 : 2.0   #allow in dictionary. Dictionary is mutable/changeable just tuple is not changed
}
print(dic)       #Output: {'name': 'umair', 'subjects': ['computer sci', 'maths', 'physics'], 'marks': (90, 80, 70), 'is_child': False, 'age': 21, 30.0: 2.0}
print(type(dic)) #Output: <class 'dict'>. dict mean dictionary.
print(dic["subjects"])
# For rename
dic["name"] = "sajawal"
# For add new key : value
dic["city"] = "sialkot"
print(dic) #Output: {'name': 'sajawal', 'subjects': ['computer sci', 'maths', 'physics'], 'marks': (90, 80, 70), 'is_child': False, 'age': 21, 30.0: 2.0, 'city': 'sialkot'}

null_dict = {} 
print(null_dict) #Outout: {}
"""
# Nested Dictionary in python
"""
student = {
    "name" : "Hassan",
    "subjects" : {
        "phy" : 80,
        "chem" : 50,
        "math" : 60
    },
    "age" : 15,
    "city" : "sialkot"
}
print(student)  #Output: {'name': 'Hassan', 'subjects': {'phy': 80, 'chem': 50, 'math': 60}, 'age': 15, 'city': 'sialkot'}
#to find only subjects in this dictionary write:
print(student["subjects"]) #Output: {'phy': 80, 'chem': 50, 'math': 60}
#if you find to marks in the specific subject write:
print(student["subjects"]["math"]) #Output: 60
"""
# Dictionary Methods 

'''
myDict.keys( ) #returns all keys
myDict.values( ) #returns all values
myDict.items( ) #returns all (key, val) pairs as tuples
myDict.get( “key““ ) #returns the key according to value
myDict.update( newDict ) #inserts the specified items to the dictionary
'''

students = {
    "name" : "Haider",
    "subjects" : {
        "phy" : 70,
        "chem" : 60,
        "math" : 50
    },
    "age" : 18,
    "city" : "lahore"
}
# 1.keys #returns all keys
'''
print(students.keys())  # Note: Only outer keys are displayed. Nested keys are not displayed
#Output : dict_keys(['name', 'subjects', 'age', 'city'])
print(list(students.keys()))       #Output: ['name', 'subjects', 'age', 'city'] 
print(len(students.keys()))        #Output: 4
print(len(list(students.keys())))  #Output: 4
'''

# 2. Values #returns all values
'''
print(students.values())  #Output: dict_values(['Haider', {'phy': 70, 'chem': 60, 'math': 50}, 18, 'lahore'])
print(list(students.values()))  #Output: ['Haider', {'phy': 70, 'chem': 60, 'math': 50}, 18, 'lahore']
'''
# 3. Items #returns all (key, val) pairs as tuples
'''
print(students.items())  #Output: dict_items([('name', 'Haider'), ('subjects', {'phy': 70, 'chem': 60, 'math': 50}), ('age', 18), ('city', 'lahore')])
print(list(students.items()))  #Output: [('name', 'Haider'), ('subjects', {'phy': 70, 'chem': 60, 'math': 50}), ('age', 18), ('city', 'lahore')
pairs = list(students.items())
print(pairs[0])        #Output: ('name', 'Haider')
'''

# 4. get( “key““ ) #returns the key according to value
'''
print(students.get("name")) #Output: Haider
print(students.get("name2")) #Output: None
print(students("name")) #Output: Haider
print(students("name2")) #Output: Error
'''
# 5. Update( newDict ) #inserts the specified items to the dictionary
"""
students.update({"gender" : "male"})
print(students) #Output: {'name': 'Haider', 'subjects': {'phy': 70, 'chem': 60, 'math': 50}, 'age': 18, 'city': 'lahore', 'gender': 'male'}

new_dict = {"name" : "ali", "Province" : "Punjab"} #Duplicate "keys" are not allowed in Dictionaries
students.update(new_dict)
print(students)  #Output: {'name': 'ali', 'subjects': {'phy': 70, 'chem': 60, 'math': 50}, 'age': 18, 'city': 'lahore', 'gender': 'male', 'Province': 'Punjab'}
"""

# Sets
'''
-Set is the collection of the unordered items.
-Each element in the set must be unique & immutable.
-lists and dictionaries are not stored in Sets because Set elements are immutable (Not Change) while lists and dictionaries are mutable changeable)
-Duplicate values are ignored
-Values in random order or way
'''
"""
set2 = {1, 2, 3, "Hello", "World", "Hello"}
print(set2)  #Output : {1, 2, 3, 'World', 'Hello'}
print(type(set2))

set3 = {} #This not empty Set. This is empty Dictionary
set4 = set() #This is empty Set syntax
print(type(set4))
"""

# Set Methods:
'''
-set.add( el ) #adds an element
-set.remove( el ) #removes the element
-set.clear( ) #empties the set
-set.pop( ) #removes a random value
-set.union( set2 ) #combines both set values & returns new and same value count only one time in output
-set.intersection( set2 ) #combines common values & returns new

Sets -> Mutable
Sets -> Elements -> Immutable
'''
"""
collSet = {6, 7, 8} 
collSet.add(9)  #adds an element
collSet.add(13)
collSet.add("Umair") #string
collSet.add((1,2,3)) #Tuple
print(collSet)     #output : {6, 7, 8, 9, (1, 2, 3), 13, 'Umair'}
collSet.remove(13) #removes the element
print(collSet)     #Output : {6, 7, 8, 9, (1, 2, 3), 'Umair'}

collSet.clear() #empties the set
print(len(collSet)) #Output : 0

collection = {"helo", "word", "umair", "sajawal"}
collection.pop()   #removes a random value
print(collection)  #Output : {'word', 'sajawal', 'umair'}

set6 = {1,2,3}
set7 = {3,4,5}
print(set6.union(set7))        #Union         #Output : {1, 2, 3, 4, 5}
print(set6.intersection(set7)) #Intersection  #Output : {3}
"""

# Practice Set:
'''
dictionary = {
    "cat" : "a small animal",
    "table" : ["a piece of furniture", "list of facts & figures"]
}
print(dictionary)

sets = {"python","java", "C++", "python", "javascript", "java", "python", 'java', "C++", "C"}
print(len(sets)) 
'''
marks = {}
x = int(input("enter your phy marks:"))
marks.update({"phy" : x})

x = int(input("enter your maths marks:"))
marks.update({"maths" : x})

x = int(input("enter your chem marks:"))
marks.update({"chem" : x})
print(marks)
