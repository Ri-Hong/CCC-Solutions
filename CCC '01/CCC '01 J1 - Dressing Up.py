'''
Author: Ri Hong
Date AC'd: Feb. 19, 2021
'''

#Explanation
'''
If we look at the top half of the bow tie, we notice a pattern. The number of stars (asterisks) on each end of the bow tie increases by 2 for every row and the
number of spaces between the stars decrease by 4 for each following row. For the bottom half of the bow tie, the pattern is flipped. The stars on each end decrease
by 2 each row and the number of spaces increases by 4 each row.
'''

#Code
import math #import the math library. We will need it for the ceil and floor functions
height = int(input()) #get the height of the bow tie
numStars = 1 #this stores the number of stars on each end of the bowtie for a particular row. Initialized to 1
numSpacesBetweenStars = height * 2 - 2 #this stores the number of in between the stars on each row. Initialized to 2 times the height -2

#loop through the top of the bow tie (not including the middle row)
for row in range(math.floor(height/2)): #handle the lesser first half of the rows. E.g if height = 5, we want to handle rows 1-2. if height = 9, we want to handle rows 1-4
  #print stars on the left
  for star in range(numStars): 
    print("*", end = "")
  #print spaces in between
  for space in range(numSpacesBetweenStars):
    print(" ", end = "")
  #print stars on the right
  for star in range(numStars):
    print("*", end = "")

  print() #go to a new line
  numStars += 2 #add 2 to the number of stars on each end
  numSpacesBetweenStars -= 4 #subtract 4 spaces

for row in range(math.ceil(height/2)):
  #print stars on the left
  for star in range(numStars): 
    print("*", end = "")
  #print spaces in between
  for space in range(numSpacesBetweenStars):
    print(" ", end = "")
  #print stars on the right
  for star in range(numStars):
    print("*", end = "")

  print() #go to a new line
  numStars -= 2 #add 2 to the number of stars on each end
  numSpacesBetweenStars += 4 #add 4 spaces