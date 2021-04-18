'''
Author: Ri Hong
Date AC'd: Mar 22, 2020
Problem: https://dmoj.ca/problem/ccc06s2
'''

#Explanation
'''
For each character in the second ciphertext message, we can find that character in the second ciphertext message, get the index, and look for the character at 
that index in the plaintext message.
'''
#Code
#Get the threemessages
plaintext = input()
cyphertext = input()
message = input()
key = {} #Stores the mapping for each character. The key is the character in the first ciphertext message and the value is the character at the corresponding index in the plaintext message
#Fill up the key dictionary
for i in range(len(plaintext)):
  key[cyphertext[i]] = plaintext[i]

#Loop through each character in the second ciphertext message
for i in message:
  #If the character exists as a key in the key dictionary, then output the corresponding value. If not, output a period
  try:
    print (key[i], end = "")
  except:
    print (".", end = "")
