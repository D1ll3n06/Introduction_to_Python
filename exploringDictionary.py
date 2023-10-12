# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 12:18:17 2023

@author: dille
"""

# 9/5/2023


# curly braces = dictionary
# one element in the dictionary will always have 2 pieces (key:value)
# purpose - look things up, hold environmental data, or authorization data
# heterogenous, always a key and a value, keys are handled differently
# dictionary is ordered (the way we put the elements into the dictionary)
# not indexable
# it is mutable (remove, add, but CANNOT change keys but can change values)
# can not have duplicate keys (can have duplicate values)
# when using a dictionary its best to use one type of data for keys


courses = {"IS3003" : "Unlocking Cyber",
           "IS1413" : "Excell for Business Information Systems",
           "IS1403" :"BUsiness INformation Systems FLuency",
           "IS2053" : "Programming Languages I",
           "IS2063" : "Programming Languages II",
            }

# prints the data type of the dictionary
print ("The TYPE associated with the variable 'courses' is", type(courses) )

# prints the number of elements (entries) in the dictionary
print ("The variable 'courses' has %d elements" % ( len(courses) ) )


# 9/7/2023


# Add an ENTRY to the dicitonary
courses [ "IS1003 " ] = "Unlocking Cyber"
#  [] square braces = mapping/ slicing
#  () curly braces = method or function call


# Let's fix the typo in IS1413....
# we are fixing the data but to python it sees this as a new value to the key
courses[ "IS1413" ] = "Excel for Business Information Systems"

# Did the new value work
print ("New Value for IS1413: ",
       courses["IS1413"])

# let's look at ALL the Value portions
print ()
print ("Extracting the VALUE portions of our ENTRIES")
valuesList = courses.values()
print (valuesList)


# let's extract the KEYS from our Dictionary
print ()
print ("Extracting the KEY portions of our ENTRIES")
keysList = courses.keys()
print (keysList)


# ITERATE through the Dictionary values
print("\n\nITERATING Through courses")
# course represents our key 
for course in courses:
    print ("\t%s" % ( courses [course] )   ) # prints out values 
# end iteration


# learn upacking and multiple assignment (IT'S IMPORTANT)
# ITERATE printing BOTH PORTIONS
print("\n\nEverything - both KEY and VALUE")

for code,title in courses.items():
    print (" KEY: %s\tVALUE: %s\t" %
               (code,title)   )
# end iteration




