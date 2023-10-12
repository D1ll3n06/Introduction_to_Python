# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 12:28:51 2023

@author: dille
"""

# Tuples = ()

# heterogenous, can't change them, can have duplicates, 
# ordered (the order you put the elements in the tuple)
# indexable, is not mutuable (no change, no)
# can be unpacked!!!!!!!!!!!
# behind the scenes you are calling the tuple constructor because you are using
# paranthesis. This is known as an implicit constructor call 

# you use implicit contructor calls when building sets, lists, dics, etc

# if your are building an object you are using a constructor !!!!!!!!
courses = ("IS1003", "IS1403", "IS3003", "IS2053", "IS2063")


# prints the data type of the dictionary
print ("The TYPE associated with the variable 'courses' is", type(courses) )

# prints the number of elements (entries) in the dictionary
print ("The variable 'courses' has %d elements" % ( len(courses) ) )

 
# ITERATE through TUPLE using an Index
print ("Course Codes")

for pointer in range ( len (courses) ):
    print (courses [pointer])
# end iteration

# 9/12/2023



# commonly use tuple as a return type of a method
# tuple can contain different objects such as lists, sets, dictionary


# looking at specific index (last one)
print("\n\nThe Last entry in my Tuple: ")
print( courses[-1] )


# We can use the ENHANCED interation structure ....
for course in courses:
    print(course)
# end iteration

"""
    We can also SEARCH a TUPLE for a Value 
"""

findThis = input ("What course are you looking for?    ")

print ("Your course is located at index %d in 'courses'. " %
       courses.index(findThis) )

# sets are unordered, can not be indexable, 
# Set items are unchangeable, meaning that we cannot change the items after the set has been created.
# Duplicates Not Allowed


