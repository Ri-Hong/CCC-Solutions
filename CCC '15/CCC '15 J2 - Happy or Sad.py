'''
Author: Ri Hong
Date AC'd: Feb 11, 2021
Problem: https://dmoj.ca/problem/ccc15j2
'''

#Explanation
'''
Count the number of happy emoticons and sad emoticons using .count(). Then compare the two values and output the correct answer

'''
#Code
string = input() #Get input

#Count the number of each emoticon
numHappys = string.count(":-)")
numSads = string.count(":-(")

#Compare the 2 numbers
if numHappys == 0 and numSads == 0:
  print("none")
elif numHappys > numSads:
  print("happy")
elif numHappys < numSads:
  print("sad")
elif numHappys == numSads:
  print("unsure")