'''
Author: Ri Hong
Date AC'd: Jan. 29, 2020
'''

#Explanation
'''
*Note that I will be using variable names that are identical to those provided by the problem statment. 
We can loop through all numbers from 1 to 100 to and let us call each of those numbers n. If the remainder upon dividing (x * n) by m is 1, then
n is the modulus inverse. In other words if (n * x) % m = 1, then n is the modulus inverse. If by the end of the 100 ns we have not found a modulus inverse
yet, then we can assume that no such integer exits to satisfy the equation (n * x) % m = 1.
'''
x = int(input()) #get x as an integer
m = int(input()) #get m as an integer

modulusInverseFound = False #this stores whether a modulus inverse has been found

for n in range(100): #loop through all the possible values of n
     if (n * x) % m == 1: #if the remainder upon dividing (x * n) by m is 1
        modulusInverseFound = True #set modulusInverseFound to true because we have found a modulus inverse
        print(n) #print n
        break #exit the for loop

if modulusInverseFound == False: #if a modulus inverse has not been found after all the looping
  print("No such integer exists.") #print No such integer exists.
