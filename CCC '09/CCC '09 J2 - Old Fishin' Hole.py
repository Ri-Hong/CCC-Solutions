'''
Author: Ri Hong
Date AC'd: Feb 3, 2021
Problem: https://dmoj.ca/problem/ccc09j2
'''

#Explanation
"""
Essentially, we want to find all the combinations of brown trout, northern pike and yellow pickerel that
can be caught while remaining under the total point limit. To go through all the combinations, we can use a 
triple nested for loop, where each for loop is responsible for keeping track of it's corresponding fish amount.
After each combination, we calculate the total point value of each fish by multiplying the number of fish with the 
point value of the fish. Then we add the total point values of all the fish and see if it's under the limit. If it 
is, then we print out that specific combination and we increment our combination counter by 1. If the total points
is not less than equal to the point limit, than we can exit the loop, since at that point, there will be no more
further combinations. Also we have to check if the amount of each fish is 0, because we do not want to print that 
specific combination.
"""

#-----------------Code-----------------
#get input and turn them into integers
brownTroutPointVal = int(input())
northernPikePointVal = int(input())
yellowPickerelPointVal = int(input())
totalPointsAllowed = int(input())


numCombinations = 0 #This will store the number of combinations of fish we can have. Initialized to 0 at the beginning

for amountBrownTrout in range(200): #tracks the number of brown trout
  for amountNorthernPike in range(200): #tracks the number of northern pike
    for amountYellowPickerel in range(200): #tracks the number of yellow pickerel
      if amountBrownTrout == 0 and amountNorthernPike == 0 and amountYellowPickerel == 0: #check if the # of each fish are all 0
        continue #if it is, we want to not do anything and move onto the next combination

      #calculate the point values of each fish
      brownTroutPoints = amountBrownTrout * brownTroutPointVal
      northernPikePoints = amountNorthernPike * northernPikePointVal
      yellowPickerelPoints = amountYellowPickerel * yellowPickerelPointVal

      #check if the sum of the fish's points are within the limit
      if brownTroutPoints + northernPikePoints + yellowPickerelPoints <= totalPointsAllowed:
        #if it is, print out that combination
        print("{} Brown Trout, {} Northern Pike, {} Yellow Pickerel".format(amountBrownTrout, amountNorthernPike, amountYellowPickerel))
        numCombinations += 1 #increment the number of combinaitons by 1
      else: #if the sum of the fish's points exceed the limit, exit the for loops
        break

#print the number of ways the fish can be caught
print("Number of ways to catch fish:", numCombinations)