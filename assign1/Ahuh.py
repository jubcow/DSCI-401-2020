# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 13:24:25 2020

@author: jubco

II. Power Set
The power set is the set of all possible subsets for a set. Please provide an implementation of
power set as follows:
1) Function: powerset(List)
2) Example output: powerset([1,2,3]) = [[1,2,3], [1,2], [1,3], [2,3], [1], [2], [3], []]
III. All Permutations
Please implement a function which will produce all permutations of a list as follows:
1) Function: all_perms(List)
2) Example output: all_perms([1,2,3]) = [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]
IV. Number Spiral
Given a number n and ending corner (1, 2, 3, or 4), print a number spiral with 0 in the middle
and n^2 – 1 in the ending corner, which spirals in the clockwise direction. Here’s an example for
n = 8 ending in corner 2:
"""

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

print("Flatten of example: ", flatten([[1,2,3], [[4],[5]], 6,7,8]))
############################################################################

from itertools import chain, combinations
# https://stackoverflow.com/questions/1482308/how-to-get-all-subsets-of-a-set-powerset
#TODO own
def powSet(setBoi): #maybe a dict idk   
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(setBoi)
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))
    
print("Powerset of 1 2 3: ", powSet([1,2,3])) 

############################################################################
#TODO
def allPerms(listBoi):
    if len(listBoi) == 0:
        return []
    if len(listBoi) == 1:
        return listBoi

############################################################################
import numpy as np
"""
use a list of lists
We know where the last number will be because of the input, so work backwards from there
make your matrix a bunch of -1's and then overwrite them as ou're moving, this way you can tell when to change direction because you'll either hit null or a non -1 number.

#0 always in middle, always end at end_corner
def spiral(n, end_corner):
    cur_num = (n**2)-1
    cur_pos = (0, n-1)
    ### TODO cur_dirIndex = <choose based on starting corner>
    matrx = np.initialize(n,n,-1)
   
    direction_vectors = [(1,0),(0,-1),(0,1),(-1,0)]
   
    while cur_num >= 0:
        matrx[cur_pos] = cur_num
        if (change_dir(mat, curpos)):
            cur_dirIndex += 1
        cur_pos = cur_pos + direction_vectors[cur_dirIndex %% 4] #mod 4
        cur_num -= 1
"""

    
