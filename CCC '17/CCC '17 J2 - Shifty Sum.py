'''
Author: Ri Hong
Date AC'd: Mar 22, 2020
Problem: https://dmoj.ca/problem/ccc17j1
'''

#Explanation
'''
A for loop can be used to shift a certain amount of times. For each shift, we have to add our current number to a total and
we need to 'shift' our current number by multiplying it by 10.
'''
#Code
#Get input
a = int(input())
b = int(input())
sum = 0 #Stores the shift sum
for i in range(b+1): #Loop through all the shifts
  sum += a #Add to sum
  a *= 10 #Shift
print(sum)