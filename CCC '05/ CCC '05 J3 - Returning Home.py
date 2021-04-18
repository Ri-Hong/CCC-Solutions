'''
Author: Ri Hong
Date AC'd: Feb 20, 2020
Problem: https://dmoj.ca/problem/ccc05j3
'''

#Explanation
'''
Take in each turn and road name and store it in 2 lists. Reverse all the directions (All Rs become Lefts and all Ls become Rights and the order in which they
appear is flipped too) and print out the road names in reverse, excluding SCHOOL and adding HOME at the end
'''
#Code
locationList = [] #Stores the road names/destinations/locations
leftOrRightList = [] #Stores the directions
flippedLeftOrRightList = [] #Stores the directions but in reverse

#Get input and fill up the first two lists
location = ""
while location != "SCHOOL":
  leftOrRightList.append(input())
  location = input()
  locationList.append(location)

locationList.pop() #remove SCHOOL

#Construct the flippedLeftOrRightList (Rs become Lefts and vice versa)
for i in range(len(leftOrRightList)):
  if leftOrRightList[i] == "R":
    flippedLeftOrRightList.append("LEFT")
  else:
    flippedLeftOrRightList.append("RIGHT")

#Reverse the lists
flippedLeftOrRightList.reverse() 
locationList.reverse()

#Loop through the lists and print out the corresponding direction and location
for i in range(len(leftOrRightList)-1):
  location = locationList[i]
  direction = flippedLeftOrRightList[i]
  print ("Turn " + direction + " onto "+ location + " street.")

#Print out the direction and HOME
direction = flippedLeftOrRightList[len(flippedLeftOrRightList)-1]
print ("Turn " + direction + " into your HOME.")
