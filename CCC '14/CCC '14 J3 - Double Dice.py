'''
Author: Ri Hong
Date AC'd: Jan 4, 2020
Problem: https://dmoj.ca/problem/ccc14j2
'''

#Explanation
'''
For each pair of input, see who rolled the least and subtract the amount shown on the higher die from their total score. Both
players start with 100 points.
'''
#Code
nRounds = int(input())
#Initialize Antonia and David's starting totals to 100
aTotal = 100
dTotal = 100
#Loop through each round
for i in range(nRounds):
  #Get rolls and convert to integer
  aRoll, dRoll = input().split()
  aRoll = int(aRoll)
  dRoll = int(dRoll)

  #Compare rolls
  if aRoll < dRoll:
    aTotal -= dRoll
  elif aRoll > dRoll:
    dTotal -= aRoll
#Output
print(aTotal)
print(dTotal)