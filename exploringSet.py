# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 11:57:50 2023

@author: dille
"""

# Sets are unordered, can not be indexable, 
# Set items are unchangeable, meaning that we cannot change the items after the set has been created.
# Duplicates Not Allowed
# Can remove and add items
# Curly brace = set

grades = { "A+","A","A-",
           "B+","B","B-",
           "C+","C","C-",
           "D+","D","D-", }

# sTANDARD cHECKS
print ("Here are %d elements in set 'grades'. " %
       len(grades) )
print ("The structure 'grades' is a %s." % type(grades) )


# add a element
grades.add("F")

# iteration
for grade in grades:
    print(grade)
#end iteration

# remove elements
grades.remove("F")