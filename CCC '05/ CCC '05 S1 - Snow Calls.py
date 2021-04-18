'''
Author: Ri Hong
Date AC'd: Mar 1, 2020
Problem: https://dmoj.ca/problem/ccc05s1
'''

#Explanation
'''
Get the initial number, remove all dashes, convert the characters into their corresponding digit and print out the final number with dashes in the correct place
'''
#Code
t = int(input())
for i in range(t):
  numberWithCharacters = input() #Get the number

  noDashes = numberWithCharacters.replace("-", "") #Remove dashes

  #Replace all the text with numbers
  noLetters = noDashes.replace("A", "2")
  noLetters = noLetters.replace("B", "2")
  noLetters = noLetters.replace("C", "2")
  noLetters = noLetters.replace("D", "3")
  noLetters = noLetters.replace("E", "3")
  noLetters = noLetters.replace("F", "3")
  noLetters = noLetters.replace("G", "4")
  noLetters = noLetters.replace("H", "4")
  noLetters = noLetters.replace("I", "4")
  noLetters = noLetters.replace("J", "5")
  noLetters = noLetters.replace("K", "5")
  noLetters = noLetters.replace("L", "5")
  noLetters = noLetters.replace("M", "6")
  noLetters = noLetters.replace("N", "6")
  noLetters = noLetters.replace("O", "6")
  noLetters = noLetters.replace("P", "7")
  noLetters = noLetters.replace("Q", "7")
  noLetters = noLetters.replace("R", "7")
  noLetters = noLetters.replace("S", "7")
  noLetters = noLetters.replace("T", "8")
  noLetters = noLetters.replace("U", "8")
  noLetters = noLetters.replace("V", "8")
  noLetters = noLetters.replace("W", "9")
  noLetters = noLetters.replace("X", "9")
  noLetters = noLetters.replace("Y", "9")
  noLetters = noLetters.replace("Z", "9")

  #Print the final number with dashes
  finalNumber = noLetters[0:3] + "-" + noLetters[3:6] + "-" + noLetters[6:10]
  print(finalNumber)