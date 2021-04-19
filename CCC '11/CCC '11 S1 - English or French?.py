'''
Author: Ri Hong
Date AC'd: Feb 22, 2020
Problem: https://dmoj.ca/problem/ccc11s1
'''

#Explanation
'''
Count the number of s, S, t, and Ts in the given lines. Then if the number of ss is greater than or equal to the number of ts, 
then the language is French. Otherwise, the language is English
'''
#Code
N = int(input())
sCounter = 0 #Stores the # of 's' and 'S'
tCounter = 0 #Stores the # of 't' and 'T'
#Get each sentence
for i in range(N):
  sentence = input()
  #Count the number of ss and ts in the sentence
  for j in sentence:
    if j == "s" or j =="S":
      sCounter += 1
    elif j == "t" or j =="T":
      tCounter += 1
      
#Compare the numbers and determine the language
if sCounter >= tCounter:
  print ("French")
else:
  print ("English")