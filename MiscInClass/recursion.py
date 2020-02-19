# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 13:18:10 2020

@author: jubco
"""

def sum_range(start, finish, total = 0):
    if start <= finish:
        total += start
        start += 1
        sum_range(start,finish, total)
    else:
        #print(total)
        return total
        
"""        
def SRR(a,b):
    if a != b:
        a + SRR(a+1,b)
"""
             
#SRR(1,4)
sum_range(1,4)

def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n-1)
    
#print(fac(5))

def rRev(l):
    if len(l) != 0:
        return [l[-1]] + rRev(l[:-1])
    else:
        return l
      
#print(rRev([1,2,3,4]))


def recursiveFib(num1, num2, n):
    if n == 0:
        return num1
    elif n == 1:
        return num2
    else:
        return recursiveFib(num1,num2,n-1) + recursiveFib(num1,num2,n-2)
    
#print(recursiveFib(1,2,9))
"""
def dFib(num1, num2, n, cache=()):
    if n == 0:
        return num1
    elif n == 1:
        return num2
    elif not ((num1,num2, n) in cache):
        cache[(num1,num2,n)] = dFib(num1,num2,n-1) + dFib(num1,num2,n-2)
    return cache[(num1,num2,n)]

print(dFib(1,2,165))
"""
"""
* sets
take first set and hold it off, find the cart prod of all the rest first (start at your tail)

for each element in A, get the cart prod of the cart product of the rest?

"""
a = ([1,2],[3,4])
b = [5,6]
c = [7,8]

def cartProd(*sets):
    if not sets:
        return [[]]
    else:
        return [[x] + p for x in sets[0] for p in cartProd(*sets[1:])]
   
#print(cartProd([1,2,3],[4,5,6]))

"""
def kComb(elements, k):
    if k ==1:
        return[[x] for x in elems]
    if len(elems) == x:
        return[elems]
    else:
        return[[elements[0]] + x for x in kComb(elements[1:], k-1)]
        
    """
    """
    [[elements[0]] + x for x in kComb(elements[1:], k-1)]
    + kComb(elements[1:], k) if not base case
    
    kComb([1,2,3,4],1) = [[1],[2],[3],[4]]
    
    [[i] for i in elements]
    what are any other base cases??
    """
    
