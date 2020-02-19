# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 12:44:50 2020

@author: jubco
"""
from functools import reduce

i = 0

def test():
    return 'p1'

def test3(pp):
    print(pp + ' p3')
 
f = lambda x: x + 1

g = lambda x: x + 2
    
def pipeline(*args): #Lambda pipeline
    return lambda x: reduce(lambda f,g: g(f), [x] + list(args))

def pipeline2(*args): #My for loop try
    def p(x):
        for i in args:
            return i(x)
    return p

def pipeline3(*args): #His for loop example
    def p(x):
        for i in list(args):
            x = f(x)
        return x
    return p

pipeline3(test(),test3(test()))
