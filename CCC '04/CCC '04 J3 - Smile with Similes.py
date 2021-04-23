'''
Author: Ri Hong
Date AC'd: Feb 1, 2020
Problem: https://dmoj.ca/problem/ccc04j2
'''

#Explanation
'''
Get each adjective and store them in an adjective list
Get each noun and store them in an noun list

Loop through each element of the adjective list. For each element of the adjective list, loop through all the elements of the 
noun list and print each combination of adjective and noun.
'''

#Code
#get input
numAdjectives = int(input())
numNouns = int(input())

#create the adjective and noun lists
adjectiveList = []
nounList = []

#get the adjectives and nouns and place them in their respective lists
for i in range(numAdjectives):
  adjectiveList.append(input())
for i in range(numNouns):
  nounList.append(input())

#loop through teh adjectives and nouns and print each combination of adj + noun
for adj in adjectiveList:
  for noun in nounList:
    print("{} as {}".format(adj, noun))
