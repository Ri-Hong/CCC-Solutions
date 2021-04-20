'''
Author: Ri Hong
Date AC'd: May 13, 2020
Problem: https://dmoj.ca/problem/ccc12s1
'''

#Explanation
'''
We can get all the combinations of scorers using a triple nested for loop.
'''
#Code
scorer = int(input())
possibleScoringCombinations = 0 #Stores the total number of combinations

#Iterate through all the possible combinations
for a in range(1, scorer-2):
  for b in range(a+1, scorer-1):
    for c in range(b+1, scorer):
      possibleScoringCombinations += 1
      
#Output
print(possibleScoringCombinations)