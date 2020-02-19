# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#list comprehension
nums = [1,2,3,4,5,6,9,8,7]
[i for i in nums if i*i<=50]



def areacircle(radius):
    """ Computes the area of a circle of the given radius """
    area = 3.14*radius*2
    print("The area of a circle of radius",radius,"is", area)

areacircle(20)
def areacircle(radius):
    """ Computes the area of a circle of the given radius """
    area = 3.14*radius**2
    print("The area of a circle of radius",radius,"is", area)

areacircle(20)
runfile('C:/Users/jubco/.spyder-py3/ejercicios.py', wdir='C:/Users/jubco/.spyder-py3')

## ---(Wed Jan 15 13:06:20 2020)---
runfile('C:/Users/jubco/.spyder-py3/temp.py', wdir='C:/Users/jubco/.spyder-py3')
3+3

## ---(Wed Jan 15 15:26:50 2020)---
3+3
print("test")
runfile('C:/Users/jubco/.spyder-py3/temp.py', wdir='C:/Users/jubco/.spyder-py3')

## ---(Wed Jan 22 13:04:19 2020)---
4^4
clear
4**4
mat = [[1,2,3],
        [4,5,6],
        [7,8,9]]
        mat
clear
mat = [[1,2,3],[4,5,6],[7,8,9]]
mat
mat[1][2]
x = [3,2,1,4,7,6]
y = x.copy().sort()
y
y = x.copy()
y
x
y.sort()
y
sorted(x)
x
y.reverse()
y
y.sort(asc)
y.sort(reverse = true)
y.sort(reverse = True)
y
y.sort(reverse = False)
y
y[::-1]
y[::1]
s1 = "This is a string"
s2 = "So is this"
s3 = s1 + ". " + s2 + "."
s3
s4 = '1-800-5550-1234'
s4.split('-')
s4.split('-').toInt()
int(s4.split('-'))
s4.split('-')
s4
sum([int(x) for x in s4.split('-')])
s4 = '1-800-550-1234'
sum([int(x) for x in s4.split('-')])
s4 = '1-800-555-1234'
sum([int(x) for x in s4.split('-')])
([int(x) for x in s4.split('-')])
nums = ['1','800','555','1234']
'-'.join(nums)
nums.join('-')
'-'.join(nums)
'---'.join(nums)
range(10)
list(range(10))
list(range(10,21))
list(range(10,21,2))
list(float(range(10,21,2.2)))
set1 = set([1,2,3,4,5,5,4,3,2,2,2])
set1
set1.add('x')
'x' in set1
s1.remove(3)
set1.remove(3)

set1
a = set([1,2,3,4,5])
b = set([6,7,8,3,4])
a.union(b)
a.AND(b)
a.intersection(b)
a
b
a.subset(b)
a.isSubset(b)
a.is_Subset(b)
a.Is_Subset(b)
a.issubset(b)

## ---(Fri Jan 24 13:07:12 2020)---
t1 = ('x', 3, 'y')
t1
points = [(1,1),(2,2),(3,3),(4,4)]
points
points[0]
points[0][1]
points.append((68,54))
a = {'a':2, 'b':4, 'c':6}
a.['a']
a.[a]
clear
a['a']
a
'd' in a
del(a['a'])
a.keys()
a['d'] = 22
a.keys()
b = {5:10,15:20}
a.update(b)
a
c = {10:15,15:55,20:10}
a.update(c)
a
dict(points)
list(a.items())
d1 = {1:2,,3:4}
d1 = {1:2,3:4}
d2 = {5:6,7:8}
d3 = d1+d2
d3 = d1.append(d2)
clear
d3 = {}
d3.update(d1)
d3.update(d2)
d3
dict(list(d1.items()) + list(d2.items())) 
d1
d2
while i in range(11):
    print i
while i in range(11):
    print (i)
    i+=1
    
i = 0
while i in range(11):
    print (i)
    i+=1
    
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