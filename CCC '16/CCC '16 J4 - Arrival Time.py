'''
Author: Ri Hong
Date AC'd: Jan 27, 2020
Problem: https://dmoj.ca/problem/ccc16j4
'''

#Explanation
"""
We know that it takes Fiona exactly 2 hours to get to work. So we can use a for loop to loop through each of those 120 minutes. 
Normally, we would increment the time by one minute for every iteration of the loop, but if the time is currently rush hour time, 
then instead we increment the time by 2 minutes since it would take her twice as long to travel one minute in rush hour time. 
"""
#----------------Code----------------
currentHour, currentMinute = map(int, input().split(":")) #this will get the input string and 
#assign the hour portion to currentHour as an int and the minute portion to currentMinute as an int


for minutesElapsed in range(120): #We want to loop 120 times because it takes Fiona 2h(120 min) to get to work
  if (currentHour >= 7 and currentHour < 10) or (currentHour >= 15 and currentHour < 19): #check if it is rush-hour time
    currentMinute += 2 #if it is rush-hour time, then it will take use two minutes for every one non-rush-hour minute
  else:
    currentMinute += 1 #if its not rush hour time, each minute passes by regularly

  #deal with overflows
  if currentMinute >= 60: #if the current minute is greater or equal to 60, then subtract 60 from it and increment currenHour by 1
    currentMinute -= 60
    currentHour += 1
  if currentHour == 24: #if the current hour is equal to 24, then subtract 24 from it 
    currentHour -= 24


if currentHour < 10: #add an extra zero to the beginning of the output if the hour is less than 10
  print("0", end = "")
print(currentHour, end = ":") #print the hour along with a colon

if currentMinute < 10: #if the current minute is less than 10, add a zero to the beginning
  print("0", end = "")
print(currentMinute, end = "") #make sure the minute is an integer as it could be ex. 24.0