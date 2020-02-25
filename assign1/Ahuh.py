# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 13:24:25 2020

@author: jubco
"""
p = [[1,2,4],[5,6],[2,3,4]]

def flatten(listBoi):
    result = []
    for x in listBoi:
        if isinstance(x, list): 
            if len(x) > 1:
                for i in x:
                    result.append(i)
            else:
                if x:
                    result.append(x)
        else:
            if x:
                result.append(x)
    return result

print(flatten(p))
print(flatten([[1,2,3], [[4],[5]], 6,7,8]))