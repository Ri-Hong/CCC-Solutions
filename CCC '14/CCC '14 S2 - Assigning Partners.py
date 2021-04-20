'''
Author: Ri Hong
Date AC'd: Jan 29, 2020
Problem: https://dmoj.ca/problem/ccc14s2
'''

#Explanation
'''
Construct one dictionary with the first line of names as the key and the second line of names as the value. Then construct 
another dictionary with the second line of names as the key and the first line of names as the value. Then loop through each
dictionary and check if the key-value pair of the first dictinary matches the corresponding value-key pair of the second 
dictionary

'''
#Code
#Get input
numberOfNames = int(input())
firstinput = input()
secondinput = input()
list1 = firstinput.split(" ")
list2 = secondinput.split(" ")

#Construct the dictionaries
d1 = {}
d2 = {}
for i in range(numberOfNames):
  d1[list1[i]] = list2[i]
  d2[list2[i]] = list1[i]

correctCounter = 0 #Stores the number of valid partner pairs

#Compare each key-value pair from both dictionaries
for x in d1:
  if x in d2:
    if d1[x] == x:
      break
    if d1[x] == d2[x]:
      correctCounter += 1
  else:
  break

#Output
if correctCounter == numberOfNames:
  print("good")
else:
  print("bad")
