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

students.update({"gender" : "male"})
print(students) #Output: {'name': 'Haider', 'subjects': {'phy': 70, 'chem': 60, 'math': 50}, 'age': 18, 'city': 'lahore', 'gender': 'male'}

new_dict = {"name" : "ali", "Province" : "Punjab"} #Duplicate "keys" are not allowed in Dictionaries
students.update(new_dict)
print(students)  #Output: {'name': 'ali', 'subjects': {'phy': 70, 'chem': 60, 'math': 50}, 'age': 18, 'city': 'lahore', 'gender': 'male', 'Province': 'Punjab'}





