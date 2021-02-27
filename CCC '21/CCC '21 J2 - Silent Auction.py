'''
Author: Ri Hong
Date AC'd: Feb 27, 2021
Problem: https://dmoj.ca/problem/ccc21j2
'''

#Explanation
'''
We can use a dictionary to store each person and their bid value. (person name as the key, their bid value as the value)
Then we can use the max function to get the highest bid value. 
Then search the dictionary to find the first person who has that highest bid value.
'''

#Code
numBidders = int(input()) #get the number of bidders as an integer
bidders = {} #stores the bidder's name as the key and bid value as the value. 
for i in range(numBidders): #loop through each bidder
  personName = input() #get the person's name as input
  bidValue = int(input()) #get the person's bid value as an integer
  bidders[personName] = bidValue #create a new entry in the dictionary with the person's name as the key and their bid value as the value

highestBid = max(bidders.values()) #get the highest bid value

#search for the person with the highest bid value. Once that person is found, the loop with exit so that only the first person with that bid amount is printed
for person in bidders.keys():
  if bidders[person] == highestBid:
    print(person)
    break