import array
a=array.array('i',[10,20,30,40,50])
print(a)

import array as ar
b=ar.array('f',[10.5,20.5,30.5,40.5,50.5])
print(b)

from array import *
c=array('u',['a','b','c','d','e'])
print(c)

for i in range(5):
    print(a[i])

for j in range(5):
    print(b[j])

for k in range(5):
    print(c[k])


#slicing of array
print(a[1:5:2])
print(b[1::2])
print(c[:5:])
print(a[::])
print(b[::3])
print(c[1::])
