'''
Author: Ri Hong
Date AC'd: Feb 1, 2020
Problem: https://dmoj.ca/problem/ccc04j2
'''

#Explanation
'''
Since the mayor is elected every 4 years, the treasurer is appointed every 2 years, the chief programmer is elected every 3 years and the dog-catcher is 
replaced every 5 years, we want to find out the years where they are all elected. In other words, we want to find the lowest common multiple of all those
numbers, which is 60. So now that we know that their positions all change every 60 years, we can just loop from year X to year Y by 60s and print out all
the results.
'''

#Code
X = int(input()) #get year X as an integer
Y = int(input()) #get year Y as an integer
for i in range(X, Y+1, 60): #loop from year X up to year Y by 60s
  print ("All positions change in year {}".format(i)) 
