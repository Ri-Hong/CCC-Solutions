'''
Author: Ri Hong
Date AC'd: Feb 20, 2020
Problem: https://dmoj.ca/problem/ccc05j1
'''

#Explanation
'''
Get the number of each type of minutes and calculate the total cost based on the given rates for each type of minute.
'''
#Code
#Get the number of each type of minute
daytimeMins = int(input())
eveningMins = int(input())
weekendMins = int(input())

#Calculate the cost for plan A (in cents)
if daytimeMins > 100:
  planACost = (daytimeMins-100)*25 + eveningMins * 15 + weekendMins * 20
else:
  planACost = eveningMins * 15 + weekendMins * 20  

#Calculate the cost for plan B (in cents)
if daytimeMins > 250:
  planBCost = eveningMins * 35 + weekendMins * 25
else:
  planBCost =eveningMins * 35 + weekendMins * 25

#Divide by 100 to convert to dollars
print("Plan A costs", planACost/100)
print("Plan B costs", planBCost/100)

#Compare the total cost of each plan
if planACost > planBCost:
  print ("Plan B is cheapest.")
elif planACost < planBCost:
  print ("Plan A is cheapest.")
else:
  print("Plan A and B are the same price.")
