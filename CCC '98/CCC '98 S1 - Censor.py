'''
Author: Ri Hong
Date AC'd: March 27, 2020
'''
#Explanation
'''
We have to replace all 4 letter words with "****". We can acomplish this by splitting each sentence by spaces
and storing the words in a list. Then we loop through the list and replace all 4 letter words with "****". 
We can loop through the list at the end and print out the censored sentence.
'''

#Code
#get the number of sentences/test cases as an integer
numLines = int(input()) 

#loop through each line
for i in range(numLines):
  string = input() #get the sentence as input
  splittedSentence = string.split(" ") #split the sentence by spaces and store it in a list

  #loop through the words in the list and censor the 4 letter words
  for wordIdx in range(len(splittedSentence)): 
    if len(splittedSentence[wordIdx]) == 4: #check if the length of the word is 4
      splittedSentence[wordIdx] = "****" #if it is, replace it with "****"

  #print out the censored sentence
  for word in splittedSentence: 
    print(word, end = " ") #print out each word followed by a space
  print() #start output on a new line after each sentence