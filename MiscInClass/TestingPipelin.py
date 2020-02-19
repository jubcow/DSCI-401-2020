# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 13:51:31 2020

@author: jubco
"""
from functools import reduce

list(zip([1,2,3,4,5],[5,6,7,8])) #Zip gives us the transpose of a matrix

def fzip(f, *lists):
    #TODO: Assuming f applies to len(lists) arguments, apply f to the combined elements at each index of the lists
    return[f(*list(c)) for c in list(zip(*lists))]
    
"""
def iterativeFzip (f, *lists):
    output = []
    for i in lists:
        return output.append(f(list))
    return output
"""

a = [[1,2,3,],[4,5,6]] 

print(fzip(lambda x,y: x + y,*a)) # => [1 + 4, 2 + 5, 3 + 6] = [5,7,9]

def my_sum(*args):
    return sum(list(args))

print(fzip(my_sum, [1,2,3],[4,5,6]))

