'''
Author: Ri Hong
Date AC'd: Feb 3, 2020
Problem: https://dmoj.ca/problem/ccc10j2
'''

#Explanation
'''
Walking can be simulated using a while loop. Inside the while loop, we process the forward steps before the backward steps
for Nikky and Byron. For each type of step, we can use a for loop to simulate stepping. On each iteration of the for loop,
we check to see if the number of total steps the person took has reached the limit when the gym teacher blows the whistle (s).
If it is, break from the for loop and if it isn't update the distance counter and step counter.

'''
#Code
#Get input
NForward = int(input())
NBackward = int(input())
BForward = int(input())
BBackward = int(input())
steps = int(input())

#Stores the number of steps Nikky and Byron took
NstepCounter = 0
BstepCounter = 0
#Stores the distance Nikky and Byron are from the starting position
NDistance = 0
BDistance = 0
#Simulate walking
while True:
  #If both Nikky and Byron have walked s steps, exit the while loop
  if NstepCounter == steps and BstepCounter == steps:
    break
  #Handle Nikky's forward steps
  for i in range(NForward):
    if NstepCounter == steps: #Check if Nikky has walked enough steps
      break
    else: #Update the distance and step counter for Nikky
      NDistance += 1
      NstepCounter += 1
  #Handle Nikky's backward steps
  for i in range(NBackward):
    if NstepCounter == steps: #Check if Nikky has walked enough steps
      break
    else: #Update the distance and step counter for Nikky
      NDistance -= 1
      NstepCounter += 1
  #Handle Byron's forward steps
  for i in range(BForward):
    if BstepCounter == steps: #Check if Byron has walked enough steps
      break
    else: #Update the distance and step counter for Byron
      BDistance += 1
      BstepCounter += 1
  #Handle Byron's backward steps
  for i in range(BBackward):
    if BstepCounter == steps: #Check if Byron has walked enough steps
      break
    else: #Update the distance and step counter for Byron
      BDistance -= 1
      BstepCounter += 1

#Compare the distances and output the result
if NDistance > BDistance:
  print("Nikky")
elif NDistance < BDistance:
  print("Byron")
elif NDistance == BDistance:
  print("Tied")