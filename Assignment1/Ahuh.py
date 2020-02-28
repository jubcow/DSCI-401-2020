# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 13:24:25 2020

@author: jubco
"""

def flatten(listBoi, memory=[]):
    for x in listBoi:           #for every element in the list
        if isinstance(x, list): #If it is another list, then:
            flatten(x,memory)   #We repeat the last few steps on that list
        else:
            memory.append(x)    #Otherwise, we add it to our memory 
                
    return memory

print("Flatten on example: ", flatten([[1,2,3], [[4],[5]], 6,7,8]))
############################################################################

def powSet(setBoi):
    if len(setBoi) > 0:             #If not an empty set
        start = powSet(setBoi[:-1]) #split with recursion so you get everything minus the last element each recurse
        #print("First: ", first)
        return start + [elem + [setBoi[-1]] for elem in start] #Return every start + one of every element + last element
    else:
        return [[]]
    
print("\nPowerset of 1 2 3: ", powSet([1,2,3])) 
############################################################################

from itertools import permutations #I knew about the import already so i just used that

def allPerms(listBoi):
    result = list(permutations(listBoi))  
    return(result)

print("\nPermutations of 1 2 3: ", allPerms([1,2,3]), "\n")
############################################################################

import numpy as np

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
    
    for i in range(n):
        #If we are going right, keep decrementing to the right until you hit the last col or a non -1
        while(cardinality == 'east' and curpos[1]+1 != n and mat[(curpos[0]),(curpos[1])+1] == -1): 
            curpos = ((curpos[0]),(curpos[1])+1)
            curnum -= 1
            mat[curpos] = curnum 
        #Change direction
        if cardinality == 'east':
            if curpos[1]+1 == n or (mat[(curpos[0]),(curpos[1]+1)] != -1):
                cardinality = 'south'
            
        #If we are going south
        while(cardinality == 'south' and curpos[0]+1 != n and mat[(curpos[0]+1),(curpos[1])] == -1): 
            curpos = ((curpos[0])+1,(curpos[1]))
            curnum -= 1
            mat[curpos] = curnum 
        if cardinality == 'south':
            if curpos[0]+1 == n or (mat[(curpos[0]+1),(curpos[1])] != -1):
                cardinality = 'west'
            
        #If we are going west
        while(cardinality == 'west' and curpos[1]-1 != -1 and mat[(curpos[0]),(curpos[1]-1)] == -1): 
            curpos = ((curpos[0]),(curpos[1])-1)
            curnum -= 1
            mat[curpos] = curnum 
        if cardinality == 'west':
            if curpos[0]+1 == n or (mat[(curpos[0]),(curpos[1]-1)] != -1):
                cardinality = 'north'
            
        #If we are going north
        while(cardinality == 'north' and curpos[0]-1 != -1 and mat[(curpos[0]-1),(curpos[1])] == -1): 
            curpos = ((curpos[0]-1),(curpos[1]))
            curnum -= 1
            mat[curpos] = curnum 
        if cardinality == 'north':
            if curpos[0]-1 == n or (mat[(curpos[0]-1),(curpos[1])] != -1):
                cardinality = 'east'
            
    return mat
    
print("Spiral:\n",spiral(10,4))
    
