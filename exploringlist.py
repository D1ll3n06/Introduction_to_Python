# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 12:32:45 2023

@author: dille
"""

# square braces = list
# heterogenous, ordered, indexable/scriptable, mutuable (add,remove,replace)
# can have duplicate values
# can keep complex items 

courses = [ 'IS1003', 'IS3003', 'IS2063', 'IS4703', 'IS2053' ]

print ( courses )

# prints out the data type of the variable courses
print ( "The type associated with 'courses' is %s." % #percent line == break line
               type( courses ) )

# prints out the length of the list
print ("The length of the variable 'courses' is %d." %
               len (courses) )

# prints out the third item in the list or 2 indexed item
print ("The THIRD item in the LIst is: ", courses[2])

print() # gives a space between different outputs 

# print items in a list using the range of the variable course
# len will give the length 5 which range will then use it for the range (0-4)
for subscript in range ( len(courses) ):
    print(subscript, courses[subscript]) #prints out the item using its index
# end iteration


print() # gives a space between different outputs 

# python version of the enhanced for loop in java
# print items in a list 
for each in courses:
    print(each)
# end iteration

print() # gives a space between different outputs 

# Traverse the list:
courses [ 3 ] = "IS1403"
print (courses[3])

# add
courses.append ("IS3073")
courses.append ("IS3003")
# delete
courses.pop(1) #if you don't put anything in pop it will delete the last item
#can use remove function too

#sort 
courses.sort() #ascending order is default sort
