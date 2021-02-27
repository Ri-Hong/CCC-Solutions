'''
Author: Ri Hong
Date AC'd: Feb 27, 2021
Problem: https://dmoj.ca/problem/ccc21j3
'''

#Explanation
'''
For each 5 character instruction, take the sum of the first two digits and see if it is 0, odd or 1. 
If the sum is 0, then the direction is the same as the previous direction.
If the sum is odd, then the direction is left
If the sum is even, then the direction is right
After every instruction, we have a variable that keeps track of this instruction so that if the next instruction's sum of the first 2 digits is 0, then we can use the direction stored in this variable.

Finally, to get the number of steps we need to move in that direction, just splice the last three characters of the instrution
'''

instruction = input() #get the 5 character instruction as a string
prevDirection = "xxxxx" #stores the previous direction. Initialized to a nonsense string

#loop through each instruction
while instruction != "99999": #keep looping until the instruction is "99999"
  codedDirection = int(instruction[0]) + int(instruction[1]) #add the first 2 digits of the instruction to get the coded direction

  #process the coded direction
  if codedDirection == 0: #if the coded direction is 0, then the direction is the previous direction
    direction = prevDirection
  elif codedDirection % 2 == 1: #if the coded direction is odd, then the direction is left
    direction = "left"
  elif codedDirection % 2 == 0: #if the coded direction is right, then the direction is right
    direction = "right"

  prevDirection = direction #update the previous direction
  numSteps = instruction[2:] #calculate the number of steps (last 3 digits of instruction)
  print(direction, numSteps) #print the direction and number of steps

  instruction = input() #get a new instruction for the next iteration of the loop
