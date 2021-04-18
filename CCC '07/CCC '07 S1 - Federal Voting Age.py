'''
Author: Ri Hong
Date AC'd: Feb 1, 2020
Problem: https://dmoj.ca/problem/ccc07s1
'''

#Explanation
'''
Subtract each person's birth year, month and day from Feburary 27, 2007. Then, if any of those values are negative, we have to 
carry from the next unit. For example, if the month was -1, then we would subtract 1 from the year and make the month 11.
If the final year was 18 or greater, then they are eligible to vote.
'''
#Code
numOfInput = int(input())
for i in range(numOfInput):
  #Get the birth year, month and day
  birthday = input()
  BYear, BMonth, BDay = birthday.split(" ")

  #Perform subtraction
  votingAgeYear = 2007 - int(BYear)
  votingAgeMonth =  2 - int(BMonth)
  votingAgeDay = 27 - int(BDay)

  #Deal with the carrying
  if votingAgeDay < 0:
    votingAgeMonth -= 1
    votingAgeDay += 7
  if votingAgeMonth < 0:
    votingAgeYear -= 1
    votingAgeMonth += 12
  if votingAgeYear < 0:
    print("No")

  #Check if the person's age is 18 or greater
  if votingAgeYear >= 18:
    print("Yes")
  else:
    print("No")
