'''
# exception handling 
try :
    print (10/0)
except ZeroDivisionError 
except Exception as e:
    print(e)

try:
    number = int(input())
    print(10/ number)

except (ValueError, ZeroDivisionError):
    print("Something went wrong")

#lambda function 
s = lambda x: x//x 
print(s(5))

# for loop
ls = [1,4,5,6,7,3]
for  items in ls:
    print(ls)

for i in range(2,21): # start, stop, step
    if i%2 == 0:
        print(i)

        
# maths for AI matrix multiplication
import numpy as np
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
print(A&B)

lt =[0,1,3]
for i in lt:
    i = i**2
    print(i)

import numpy as np
ls = np.array([10,20,30])
a=np.add(ls,10)
print(a)
'''




