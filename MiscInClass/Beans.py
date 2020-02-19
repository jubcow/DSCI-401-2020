# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 13:10:58 2020

@author: jubco
"""

i = 1
while i in range(11):
    print (i)
    i+=1
    
for(x,y) in points:
    print(x+y)
    
for(_,y) in points:
    print(y)
    
[w for w in range(1,101,2)]
[w for w in range(0,101,2)]
[w for w in range(1,20,**2)]
[w for w in range(1,20,w)]
[w for w in range(1,20,**)]
clear
[w for w in range(1,20,*w)]
clear
[w** for w in range(1,20)]
[w for w** in range(1,20)]
clear
[w for w in range(1,20)**]
[w for w in range(1,20)]
clear
[w for w in range(1,21)]
[w for w in range(1,21)]**
clear
[w*i for w in range(1,21)]
[w*w for w in range(1,21)]
clear
[w*w for w in range(1,21)]
nums = [5,6,7,8,9,1,2,3,4]
[w*w for w < 50 in range(1,21)]
[w*w for w*w<50 in range(1,21)]
[i for i in nums]
[i for i in nums if i<=50]
[i for i in nums if i*i<=50]
clear

## ---(Mon Jan 27 12:59:35 2020)---
w for w in range(1,100,2)
[w for w in range(1,100,2)]
[w for w in range(0,101,2)]
%pprint
[w for w in range(0,101,2)]
[(x,y) for x in range(1,6)]
[(x,y) for x in range(1,6) for y in range(1,6)]
[(x,y) for x in range(1,101) for y in range(1,6) if x*y==100]
[(x,y) for x in range(1,101) for y in range(1,101) if x*y==100]
[(x,y) for x in range(1,101) for y in range(1,101) if x+y==100]
def boi(x,y):
    return x + y


boi(1,2)
def betterAdd(x,y,mult=1,power=1):
    return mult * (x+y) ** power


betterAdd(5,10)
betterAdd(5,10,2)
betterAdd(5,10,1,2)
def something(a, b, *c):
    print(a)
    print(b)
    print(c)
    
something(1,2,"TEsting ", 1,2,3,4,5)
def something_else(*inputs):
    print(inputs)
    return sum(inputs)


something_else(1,2,3,4,5,6)
something_else(1,2,3,4,5,6, "Test")
clear
args = list(range(15))
args
something_else(args)
clear
something_else(*args)
args.reverse()
args
sorted(args)
args.sort()
sorted(args)
coords = [(x,y) for x in range(1,6)[::-1]for y in range(1,6)[::-1]]
coords
sorted(coords)
sorted(coords, key=lambda x: x[0])
sorted(coords, key=lambda x: y[0])
sorted(coords, key=lambda y: y[0])
sorted(coords, key=lambda x: x[1])
clear
sorted(coords, key=lambda x: x[1]+x[0])
from untitled0.py import betterAdd2
from untitled0 import betterAdd2
betterAdd2(1,3)
clear
from basic_functions import betterAdd2

## ---(Wed Jan 29 13:03:47 2020)---
(lambda x,y: (3*x) + (2*y))(4,5)
from functools import *
inc = lambda x: x + 1
nums = list(range(15))
nums
list(map(inc, nums))
list(map(lambda x: x * x, range (1,26))


)
%pprint
list(map(lambda x: x * x, range (1,26)))
clear
list(map(lambda x: x * x, range (1,26)))
names = ["joe","shane","bob"]
list(map(lambda x: "Hello " + x)(names))
list(map(lambda x: "Hello " + x,(names))
0
)
list(map(lambda x: "Hello " + x,(names))
)






)
list(map(lambda x: "Hello " + x,(names))
)
squares = list(map(lambda x: x ** 2, range(1,51)))
list(filter(lambda x: x < 1500, squares))
squares
['Hello ' + str(x) for x in names]
[inc(x) for x in range(20)]
[x**2 for x in range(1,51) if x < 1500]
[x**2 for x in range(1,51) if x**2 < 1500]
[inc(x) for x in range(20)]
step_maker: lambda x: lambda y: x + y
step_maker(7)
step_maker = lambda x: lambda y: x + y
step_maker(7)
step_maker(7)(5)
step_7 = stepmaker(7)
step_7 = step_maker(7)
[step7(x) for x in range(20)]
[step_7(x) for x in range(20)]
[step(10)(x) for x in range(20)]
[step_maker(10)(x) for x in range(20)]
reduce(lambda x,y: x + y, range(1,11))
sum(range(1,11))
ssq = lambda s: reduce(lambda x,y: x + y, [w ** 2 for w in s])

ssq(range(5))
mxs = lambda s: reduce(lambda x: [w for w in s if w > s])
li = [1,2,3,4]
mxs(range(10))
mxs = lambda s: reduce(lambda x: x,[w for w in s if w > s])
mxs(range(10))
mxs = lambda s: reduce(lambda x: x,[w for w in s if w[w] > s])
mxs(range(10))
reduce( lambda x,y: x if x > y else y, li)
reduce(lambda x,y: x if x > y else y, li)
maxi = lambda s: reduce(lambda x,y: x if x >y else y, li)
maxi(li)
maxi(nums)