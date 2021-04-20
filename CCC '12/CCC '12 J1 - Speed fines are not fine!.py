'''
Author: Ri Hong
Date AC'd: Feb 1, 2020
Problem: https://dmoj.ca/problem/ccc12j1
'''

#Explanation
'''
Get the speed limit and speed of the car. Calculate the 'over speed' by subtracting the car's speed from the speed limit.
Then output the correct fine amount.
'''
#Code
speedLimit = int(input())
carSpeed = int(input())
overSpeed = carSpeed - speedLimit #Calculate the over speed
#Output the correct fine message
if overSpeed <= 0:
  print ("Congratulations, you are within the speed limit!")
elif overSpeed > 0 and overSpeed <= 20:
  print("You are speeding and your fine is $100.")
elif overSpeed > 20 and overSpeed <= 30:
  print("You are speeding and your fine is $270.")
elif overSpeed > 30:
  print("You are speeding and your fine is $500.")
