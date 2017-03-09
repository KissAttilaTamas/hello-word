#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 14:04:16 2017

@author: attilakiss
"""
import numpy as np
a = np.ones((3, 3))
print(a)

np.lookfor('delete array') 


np.array?

x=np.array(np.mat('1 2 3; 3 4 5; 4 4 3 '))
y=(x+1)

np.con*?
np.delete?

arr = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(arr)
c=np.delete(arr, 2, 1)
print(c)
print(arr," \n",c, arr.ndim, arr.shape, c.ndim, c.shape) 

s=np.array(range(100))
print(s)
print(s[20:])
print(s[:20])

# Exercise: Simple arrays
# Create a simple two dimensional array. First, redo the examples 
# from above. And then create your own: how about odd numbers 
# counting backwards on the first row, and even numbers
# on the second?
# Use the functions len(), numpy.shape() on these arrays. 
# How do they relate to each other? And to the ndim attribute
# of the arrays?
np.append?
range?
x=np.array(range(20,10,-2))
y=np.array(range(1,11,2))
print(x,y)
t=np.append([x[:4]],[y[:4]],axis=0)
print("\n",t, t.shape)

f=np.arange(20,10,-2)
g=np.arange(1,11,2)
g1=np.append([f[:4]],[g[:4]],axis=0)
print("\n",g1, g1.shape)

print(f)
np.append?

np.empty?
p=np.empty([2,2])


import matplotlib.pyplot as plt  # the tidy way
print(x,y)
plt.plot(x, y)       # line plot    
plt.show()           # <-- shows the plot (not needed with interactive plots) 

x = np.linspace(0, 3, 20)
y = np.linspace(0, 9, 20)
plt.plot(x, y)       # line plot    
plt.plot(x, y, 'x')  # dot plot


image = np.random.rand(30, 30)
plt.imshow(image, cmap=plt.cm.hot)    
plt.colorbar()  
print(image)  

a = np.diag(np.arange(3))
print(a)

a[1, 1]

a[2, 1] = 10 # third line, second column
print(a)


a = np.arange(10)
a

a[2:9:3] # [start:end:step]

k1=np.arange(0,6)
g1=np.append([f[:4]],[g[:4]],axis=0)


A = np.arange(10)
print(A[1:])
print(A[:-1])
print(A[:-2])
print(A[:8])
print(A[::2]) # starting from 0 position by 2
print(A[1::2]) # starting from 1 position by 2
print(A[1:8:2])# starting from 1 till 8. position by 2
print(A[-3:])# staring with the 3. position from the top till the last one
print(A[:-3:2])
print(A[::-1])
print(A[:-1])
print(A[:1:-1])
print(A[5:3:-1])
print(A[3:5:-1])
print(A[::-2])
print(A[-2::-1])
print(A[:8:-1])
print(A[:8:1])
B=np.array([[0, 1, 2],
       [3, 4, 5],
       [6, 7, 8]])
print(B)
print(B[:2,:])
print(B[:2,:])
print(B[0,::-1])
print(B[0,:1:-1])
print(B[0,:1:1])
print(B[0,1::1])
print(B[:,0:1])


a = np.arange(10,20)
idx = np.array([[3, 2], [5, 8]])
idx.shape

print(a)
print(idx)
print(a[idx])

