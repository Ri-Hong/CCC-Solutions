'''
Author: Ri Hong
Date AC'd: Feb 2, 2020
Problem: https://dmoj.ca/problem/ccc04s1
'''

#Explanation
'''
For each testcase, we are given three words and we want to check if each word is a prefix or suffix of another. So we have to compare
word 1 and word 2, word 2 and word 3 and word 1 and word 3.

Let us now compare two words, let's say word 1 and word 2. Note that we can only check if word 2 contains word 1 as a prefix/suffix if
word 2's length 1 greater than or equal to word 1's length. The same applies when we check if word 1 contains word 2 as a prefix/suffix.

To check if word 1 is a prefix of word 2, let us assign the length of word 1 to a variable a.
We want to see if the first n characters of word 2 forms the same string as word 1.
To check if word 1 is a suffix of word 2, we have to check if the last n characters of word 2 forms the same string as word 1. (this can 
be done using negative indexing)
'''

#Code
#It is recommended that you read the main code before the function

#This function compares two words and returns true of both are fix-free of each other
def fixFree(word1, word2):
  if len(word2) >= len(word1): #only search for fixes within word 2 if word 2's length is greater than or equal to word 1's length
    if word2[:len(word1)] == word1: #if word 1 is a prefix of word 2
      return False
    if word2[-len(word1):] == word1: #if word 1 is a suffix of word 2
      return False

  if len(word1) >= len(word2): #only search for fixes within word 1 if word 1's length is greater than or equal to word 2's length
    if word1[:len(word2)] == word2: #if word 2 is a prefix of word 1
      return False
    if word1[-len(word2):] == word2: #if word 12 is a suffix of word 1
      return False

  return True #return true because if the function makes it to this point, it means that there are no fixes in either word

#--MAIN---
words = [] #stores teh three words we need to process for each testcase
numTestcases = int(input()) #get the number of testcases (also known as N in the problem statement) as an integer
for i in range(numTestcases): #go through each testcase
  #add the three words into the words list
  for j in range(3):
    words.append(input())

  #check if all combinations of words are fix free from each other and print the appropriate message
  if fixFree(words[0], words[1]) and fixFree(words[1], words[2]) and fixFree(words[0], words[2]):
    print("Yes")
  else:
    print("No")
  words.clear() #clear the list after each testcase