'''
Author: Ri Hong
Date AC'd: Aug 30, 2020
Problem: https://dmoj.ca/problem/ccc17s1
'''

#Explanation
'''
Loop through each team's games at the same time while keeping a running total of their individual scores. If the scores are 
equal at any point, increment a counter by 1.
'''
#Code
#Get input
season = int(input())
swifts = input().split()
semaphores = input().split()
#Stores the running total for both teams
sum = 0
sum2 = 0
#Stores the number of days for which their scores are tied
numbofdays = 0
for i in range(season):
  #Convert to int
  swifts[i] = int(swifts[i])
  semaphores[i] = int(semaphores[i])
  #Update sums
  sum += swifts[i]
  sum2 += semaphores[i]
  #If the sums on this day match
  if sum == sum2:
    numbofdays = i + 1
print(numbofdays)