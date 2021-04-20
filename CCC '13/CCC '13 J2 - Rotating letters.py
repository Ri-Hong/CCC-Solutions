'''
Author: Ri Hong
Date AC'd: Feb 22, 2020
Problem: https://dmoj.ca/problem/ccc13j2
'''

#Explanation
'''
Loop through each letter in the word and check if the character is one of: I, O, S, H, Z, X, or N. If there is even one 
character that is not, then the output will be NO.
'''
#Code
word = input()
validWordList = ["I", "O", "S", "H", "Z", "X", "N"] #Stores the valid characters
isValid = True #Stores whether the word can be flipped
#Loop through each character
for i in word:
  if i not in validWordList:
    isValid = False
    break
#Output
if isValid == True:
  print ("YES")
else:
  print ("NO")