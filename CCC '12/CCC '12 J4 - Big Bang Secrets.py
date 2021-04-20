'''
Author: Ri Hong
Date AC'd: Aug 31, 2020
Problem: https://dmoj.ca/problem/ccc12j4
'''

#Explanation
'''
We can loop through each character in the word and compute the shift value using the formula S = 3*letter index + inputted number
Keep in mind that the letter index is indexed at 1 in the problem statement, so we need to add 1. Then we can shift the letter
by the calculated shift value using ord() and subtraction. Finally we need to check if the value is less than ord('A') (invalid
character)
'''
#Code
number = int(input()) #Get the number used to compute the shift value
word = input() #Get the word we want to shift
for i in range(len(word)): #Loop through each character in the word
  shift = 3 * (i + 1) + number #Calculate the curent shift value
  newPosistion = ord(word[i]) - shift #Get the new character
  if newPosistion < ord('A'): #Handle underflow from subtraction
    newPosistion += 26
  print(chr(newPosistion), end="")
