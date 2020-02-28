# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 13:24:25 2020

@author: jubco
"""

def flatten(listBoi, memory=[]):
    for x in listBoi:           #for every element in the list
        if isinstance(x, list): #If it is another list, then:
            flatten(x,memory)   #We repeat the last few steps in that list
        else:
            memory.append(x)    #Other wise, we add it to our memory 
                
    return memory

print("Flatten on example: ", flatten([[1,2,3], [[4],[5]], 6,7,8]))
############################################################################

from itertools import chain, combinations
# https://stackoverflow.com/questions/1482308/how-to-get-all-subsets-of-a-set-powerset

def powSet(setBoi):  
    return list(chain.from_iterable(combinations(setBoi, p) for p in range(len(setBoi)+1)))
    
print("\nPowerset of 1 2 3: ", powSet([1,2,3])) 
############################################################################

from itertools import permutations

def allPerms(listBoi):
    result = list(permutations(listBoi))  
    return(result)

print("\nPermutations of 1 2 3: ", allPerms([1,2,3]), "\n")
############################################################################

import numpy as np
import math
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
"""
Must be clockwise!
12
34
Cardinality is where you want to be heading
"""
def spiral(n, end_corner):
    mat = np.full((n, n), -1)
    curnum = (n**2)-1
    if end_corner == 1:         #Upper Left
        curpos = (0,0)
        mat[curpos] = (n**2)-1
        cardinality = 'east'
    elif end_corner == 2:       #Upper Right
        curpos = (0,n-1)
        mat[curpos] = (n**2)-1
        cardinality = 'south'
    elif end_corner == 3:       #Lower Right
        curpos = (n-1,n-1)
        mat[curpos] = (n**2)-1
        cardinality = 'west'
    elif end_corner == 4:       #Lower left
        curpos = (n-1,0)
        mat[curpos] = (n**2)-1
        cardinality = 'north'
    else:
        print("Incorrect input, end_corner must be between 1 and 4")
        return 0
        
    print(mat, "\n")
    
    while(cardinality == 'east' and mat[(curpos[0])(curpos[1])+1 == -1]):
        curpos = mat[(curpos[0])(curpos[1])+1 == -1]
        curnum -= 1
        mat[curpos] = curnum 
    
    print(mat, "\n")
    
spiral(8,1)
    
