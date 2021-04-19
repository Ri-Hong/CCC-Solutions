'''
Author: Ri Hong
Date AC'd: Mar 22, 2020
Problem: https://dmoj.ca/problem/ccc10s2
'''

#Explanation
'''
Store each character and it's corresponding binary code in a dictionary with the binary as the key and the character as the value.
Then loop through the dictionary and check if which key matches the beginning of the sequence. Then print out the corresponding
letter and update the sequence by removing the already processed binary portion
'''
#Code
codeDict = {} #Stores the binary sequence and it's corresponding characters as a key-value pair
k = int(input())
#Construct the dictionary
for i in range(k):
  bCode = input()
  a,b = bCode.split(" ")
  codeDict[b] = a
bSeq = input() #Get the binary sequence to decode

while len(bSeq) != 0: #Keep looping until all the entire sequence is processed
  for i in codeDict: #Loop through the dictionary
    if i == bSeq[:len(i)]: #Check if the beginning of the sequence matches the current binary sequence in the dictionary
      bSeq = bSeq[len(i):] #Remove the processed binary sequence
      print(codeDict[i], end = "") #Output the character
