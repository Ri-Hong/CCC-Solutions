'''
Author: Ri Hong
Date AC'd: Mar 25, 2020
Problem: https://dmoj.ca/problem/ccc13j4
'''

#Explanation
'''
To maximize the amount of chores that can be done, we should complete the chores that require the least time first.
'''
#Code
#Get input
time = int(input())
numChores = int(input())
choreList = []
choreCounter = 0
for i in range(numChores):
  choreList.append(int(input()))

#Sort the list from least to greatest
choreList.sort()

#Loop through the chores, stopping when I am out of time
for i in choreList:
  if i <= time:
    time -= i
    choreCounter += 1

print(choreCounter)