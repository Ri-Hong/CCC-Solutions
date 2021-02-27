'''
Author: Ri Hong
Date AC'd: Feb 27, 2021
Problem: https://dmoj.ca/problem/ccc21j1
'''

#Explanation
'''
The formula for atmospheric pressure given by the problem statement is P = 5 x B - 400. Where P is the atmospheric pressure and B is the boiling point of water.
Simply calculate and print that out.
Next we need to determine if we are at, below, or above sea level. 
"At sea level, atmospheric pressure is 100"
"As you go above sea level, atmospheric pressure decreases" 
"As you go below sea level, atmospheric pressure increases"
Meaning, if atmospheric pressure is 100, then we are at sea level. If atmospheric pressure is below 100, then we are above sea level. If atmospheric pressure is
above 100, we are below sea level
'''
#Code
boilingPoint = int(input())

atmosphericPressure = 5 * boilingPoint - 400

print(atmosphericPressure)
if atmosphericPressure == 100:
  print(0)
elif atmosphericPressure < 100:
  print(1)
else:
  print(-1)