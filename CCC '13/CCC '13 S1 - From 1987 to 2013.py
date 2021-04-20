'''
Author: Ri Hong
Date AC'd: Mar 14, 2020
Problem: https://dmoj.ca/problem/ccc13s1
'''

#Explanation
'''
Loop through all the years from the given year all the way until a distinct year is found. To check if it is a distinct year, 
convert it into a string and count all the possible characters/numbers in the string to see if they appear more than once.
'''
#Code
a = input()
disc = False
while(not disc):
  a = str(int(a) + 1) #Increment the current year and turn it into a string
  disc = True #Set distinct to true for now
  for i in range(10): #Count each possible number in the string
    if(a.count(str(i)) > 1): #If there is more than 1 of any digit, then the year is not distinct
      disc = False
    
print(a)
