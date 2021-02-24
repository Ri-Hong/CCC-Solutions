'''
Author: Ri Hong
Date AC'd: Feb. 24, 2021
'''

#Explanation
'''
Given a revenue total and the cost of each ticket, we need to find all the combinations of tickets bought that will equate the revenue total.

Before we iterate, we have to create two variables to keep track of the number of combinations of tickets that will result in the revenue total and
a variable that keeps track of the minimum # of tickets that need to be printed
We have to go through all possible combinations of tickets. Since there are 4 tickets, we can acomplish this by using a quad nested for loop. (A for loop in a for loop in a for loop in a for loop)

Then for each combination, we have to check if the revenue from selling that combination of tickets is equal to the total revenue. If it is, we have to increment the combination counter by 1.
Then we have to check if the sum of the current combination of tickets is less than the minimum number of tickets that need to be printed (this value is stored in a variable).
'''

#Code
#get input
costPinks = int(input()) #get the cost of each pink ticket
costGreens = int(input()) #get the cost of each green ticket
costReds = int(input()) #get the cost of each red ticket
costOranges = int(input()) #get the cost of each orange ticket
totalRevenue = int(input()) #get the exact amount that is to be raised

numCombinations = 0 #stores the number of possible combinations of ticket purchase numbers. Initialized to 0
minTicketsToPrint = 999999999 #stores the minimum tickets that needs to be printed to achieve the desired revenue amount
for numPinks in range(totalRevenue + 1): #loop for number of pink tickets *Note, we use totalRevenue+1 for the parameter because we want to loop up to and including the totalRevenue
  for numGreens in range(totalRevenue + 1): #loop for number of green tickets
    for numReds in range(totalRevenue + 1): #loop for number of red tickets
      for numOranges in range(totalRevenue + 1): #loop for number of orange tickets
        if numPinks * costPinks + numGreens * costGreens + numReds * costReds + numOranges * costOranges == totalRevenue: #check if the current combination can produce the desired revenue
          numCombinations += 1 #if the desired revenue is achieved, increment the number of possible combiantions by 1
          ticketTotal = numPinks + numGreens + numReds + numOranges # add up the tickets sold
          if ticketTotal < minTicketsToPrint: #if the sum of the current combiantion of tickets is less the the minimum # of tickets
            minTicketsToPrint = ticketTotal #the current sum of the combination of ticktes becomes the new minimum
          print("# of PINK is {} # of GREEN is {} # of RED is {} # of ORANGE is {}".format(numPinks, numGreens, numReds, numOranges)) #print the current combination

print("Total combinations is {}.".format(numCombinations)) #print the total number of combinations
print("Minimum number of tickets to print is {}.".format(minTicketsToPrint)) #print the minimum tickets that need to be printed
