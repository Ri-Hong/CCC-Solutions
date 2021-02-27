'''
Author: Ri Hong
Date AC'd: Feb 27, 2021
Problem: https://dmoj.ca/problem/ccc21j2
'''

#Explanation
'''
We can use a list to store the list of bidder's names and another list to store the bidder's corresponding bid value. A bidder will have their bid value at the same index as their name.
Then we can use the max function to get the highest bid value. 
Then search the bid values list to get the index of the highest bid.
Then use that index to find the person who bid that amount from the bidder's name list.
'''

#Code
numBidders = int(input()) #get the number of bidders as an integer
bidders = [] #stores the bidder's names
bidValues = [] #stores the bidder's bid value

for i in range(numBidders): #loop through each bidder
  personName = input() #get the person's name as input
  bidValue = int(input()) #get the person's bid value as an integer
  bidders.append(personName) #add the person's name to the bidders list
  bidValues.append(bidValue) #add the person's bid value to the bidValues list

highestBid = max(bidValues) #get the highest bid value

for i in range(numBidders): #loop through the number of bidders by index
  if bidValues[i] == highestBid: #if the index of the highest bid is found,
    print(bidders[i]) #print the person at that index
    break #exit the loop so that if there are people with the same bid value, only the first person gets printed

