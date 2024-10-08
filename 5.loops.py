# Loops in python
# Loops are used ti repeat instructions

#1. while loop:
'''
syntax:
while condition:
   # some work
'''
"""
count = 1
while count <= 5 :
    print("Umair")
    count += 1  #count=count+1
print(count)  

i = 5
while i >= 1 :
    print(i)
    i -= 1
print("Loop Ended")
"""
#Practice Set:
'''
x = 100
while x >= 1:
    print(x)
    x -= 1

n = int(input("Enter a number:"))
i = 1
while i <= 10 :
    print(i*n)
    i += 1


nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1

heroes = ["superman", "batman", "ironman", "spiderman", "thor"]
idex = 0
while idex < len(heroes):
    print(heroes[idex])
    idex += 1
'''
num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 100
i = 0
while i < len(num):
    if(num[i] == x):
       print("Found at index", i)
    else:
        print("Founding")
    i += 1