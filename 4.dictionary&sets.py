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

