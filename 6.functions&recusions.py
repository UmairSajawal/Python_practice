# Functions in python
#Block of statements that perform a specific task.
'''
Syntax: 
def func_name( param1, param2..) : 
    #some work
return val 
func_name( arg1, arg2 ..) #function call
'''
"""
#function defination
def calc_sum(a, b):   #(a, b) are called parameters
    sum = a + b
    print(sum)
    return sum

calc_sum(5, 6)   #Function call #(5, 6)  are called arguments   #Ouput : 11
calc_sum(2, 10)  #Function call #(2, 10) are called arguments   #Ouput : 12

def cal_avg(a, b, c):
    sum = a + b + c
    avg = sum / 3
    print(avg)
    return avg

cal_avg(3 , 3, 3)

#in short and better way to use funtion:
#function defination
def calc_sub(c, d):    #(c, d) are called parameters
    return c - d
subt = calc_sub(6, 3)  #(6, 3) are called arguments
print(subt)   #Output : 3

#simple and without nput and output functions :
def print_hello():
    print("Hello World!")

print_hello() #Output : Hello World!


# Types of fintions
'''
Two types of functions:
1. Built-in functions: print(), len(), type(), range()
2. User-defined funnctions
'''
# Default Parameters
#Assigning a default value to parameter, which is used when no argument is passed. For example:
def calc_prod(a, b):
    print(a * b)
    return a * b
calc_prod()  #Output : error of missing parameters

#But if i write:
def cal_prod(c=2, d=3):  #considered default values if the arguments not passed in below.
    print(c * d)
    return c * d
cal_prod()      #Output : 6
cal_prod(3, 3)  #Output : 9
"""
# Practice Set:
'''
# WAF to print the length of a list. ( list is the parameter)
cities = ["sialkot", "lahore", "rawalpindi", "islamabad"]
heroes = ["ironman", "superman", "spiderman"]
def calc_len(list):
    print(len(list))
    return list

calc_len(cities)
calc_len(heroes)

#WAF to print the elements of a list in a single line. ( list is the parameter)
cities = ["sialkot", "lahore", "rawalpindi", "islamabad"]
def print_cities(list):
    for items in cities:
        print(items, end=" ")  #end is built-in vaiable in print() function

print_cities(cities) #Output as it is : sialkot lahore rawalpindi islamabad 

# WAF to find the factorial of n. (n is the parameter)
def calc_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)
calc_fact(5)  #Output : 120

#WAF to convert USD to INR. 
#if INR = 83
def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD =", inr_val, "INR")

converter(1)  #Output : 1 USD = 83 INR

#home work:
def even_odd(n):
    if(n%2 == 0):
        print("Even")
    else:
        print("ODD")

even_odd(2)
'''

# Recursion
#When a function calls itself repeatedly. 
#prints n to 1 backwards
"""
def show(n):      #recursive function
    if(n == 0):   #Base case  #decide to stops recursion
        return
    print(n)
    show(n-1)
show(5)
'''Output:
5
4
3
2
1
'''
#returns n!
'''
4! = 1 * 2 * 3 * 4  = 3! * 4
3! = 1 * 2 * 3 = 2! * 3
2! = 1 * 2
1! = 1
0! = 1
n! = (n-1)! * n   #recurance relation
fact(n) = fact(n-1) * n
fact(n-2) = fact(n-2) * (n-1)
'''
def fact(n):
    if(n == 1 or n == 0):
        return 1
    return fact(n-1) * n     #Base case  #decide to stops recursion

print(fact(5)) #Output: 120
"""
# Practice set:
#Write a recursive function to calculate the sum of first n natural numbers. 
'''
def cal_summ(n):
    if(n == 0):
        return 0
    return cal_summ(n-1) + n
sum = cal_summ(5)
print(sum)

#Write a recursive function to print all elements in a list.
#Hint : use list & index as parameters.
def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

fruits = ["mangoes", "bananas", "peaches", "guavas"]
print_list(fruits)
'''
