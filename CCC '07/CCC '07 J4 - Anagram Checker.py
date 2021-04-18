'''
Author: Ri Hong
Date AC'd: Feb 1, 2020
Problem: https://dmoj.ca/problem/ccc07j4
'''

#Explanation
'''
Count the number of each character in the first string and count the number of each character in the second string. If they match, 
the strings are an anagram
'''
#Code
phrase1letterList = {} #Stores the number of each character in the first string
phrase2letterList = {} #Stores the number of each character in the second string
phrase1 = input()
phrase2 = input()

#Construct the letterlists dictionaries
for j in range(2):
  if j == 0:
    phrase = phrase1
    letterList = phrase1letterList
  else:
    phrase = phrase2
    letterList = phrase2letterList

  for i in range(len(phrase)):
    if phrase[i] not in letterList:
      letterList[phrase[i]] = 1
    else:
      letterList[phrase[i]] += 1
  letterList[" "] = 0

#Count the number of letters that have a matching number across the two strings
correctCounter = 0
for x in phrase1letterList:
  if x in phrase2letterList:
    if phrase1letterList[x] == phrase2letterList[x]:
      correctCounter += 1
    else:
      break
  else:
    break

#If the number of matching letters equals the length of the string, then the strings are an anagram
if correctCounter == len(phrase1letterList):
  print("Is an anagram.")
else:
  print("Is not an anagram.")