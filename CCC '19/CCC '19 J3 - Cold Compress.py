'''
Author: Ri Hong
Date AC'd: Jan 25, 2021
Problem: https://dmoj.ca/problem/ccc19j3
'''

#--------Explanation-----------
"""
For each line of input, we want to loop through each character of it. 
We keep track of how many times we have seen a certain character and the actual character itself.
Each time we loop onto a character, we compare it to the previous character. If they match, then
we increment the counter by one. If they dont match, then we save the counter value and the character 
"""

#--------Code-----------

n = int(input()) # get the number of lines of input

for i in range(n): #for each line of input
  string = input() #get each line of input
  counter = 0 #stores how many times the previous character appears

  previousChar = string[0] #keep track of what the previous character is. Initialize it to the first character in the beginning
  for character in string: #loop through the characters in the string
    if character == previousChar: #if the character we are currently looking at is the same as the previous character, increment the counter by 1
      counter += 1
    else: #if the character we are currently looking at is not the same as the previous character, then we add the counter and the previous character to the output list 
      print(counter, end = " ")
      print(previousChar, end = " ")

      previousChar = character #reset the precious character (make it the current character)
      counter = 1 #reset the counter to one

  print(counter, end = " ")
  print(previousChar, end = " ")
  print()
