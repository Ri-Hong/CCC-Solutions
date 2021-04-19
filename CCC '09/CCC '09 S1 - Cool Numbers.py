'''
Author: Ri Hong
Date AC'd: Mar 25, 2020
Problem: https://dmoj.ca/problem/ccc09s1
'''

#Explanation
'''
Instead of checking every integer from the lower bounds to the upper bounds, we make it more efficient by only checking in the
range of the cube roots of the lower and upper bounds. For every number in between the cube roots, check if the square
root of it's cube is an integer. If it is, then increment a counter by 1.
'''
#Code
import math #Used for sqrt function

def sqrt(n): #Checks if the square root of n is an integer
  if math.sqrt(n) == round(math.sqrt(n)):
    return True
  else:
    return False

a = int(input()) #Lower bounds
b = int(input()) #Upper bounds
c = 0 #Cool number counter

#Update the boundaries by cube rooting them. a and b also need to be rounded in case the given numbers are not perfect cubes
a = round(a**(1/3))
b = round(b**(1/3))

#Loop through the boundaries
for i in range(a, b+1):
  if sqrt(i**3) == True: #Check if the square root of i's cube is an integer
    c+=1
print(c)