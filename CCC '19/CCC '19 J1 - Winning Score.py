'''
Author: Ri Hong
Date AC'd: Jan 10, 2021
Problem: https://dmoj.ca/problem/ccc19j1
'''

#Explanation
'''
We want to get the # of 3 pointers for team Apples, multiply that by 3, get the # of 2 pointers, multiply that 
by 2, and get the # of 1 pointers and add them together to get a total score of team Apples
We do the same for team Bananas and then we compare who's score is larger
'''

#Code
# declare variables
scoreA = 0 #scoreA holds the total score for team Apples
scoreB = 0 #scoreB holds the total score for team Bananas

# get the scores for team Apple
for idx in range(3):
    apple = int(input()) #get the input and change it into an integer
    if idx == 0:  # first line of input (# of 3-pointers)
        scoreA += apple * 3 # multiply the number of 3 pointers by 3 and add it to scoreA
    elif idx == 1:  # second line of input (# of 2-pointers)
        scoreA += apple * 2  # multiply the number of 2 pointers by 2 and add it to scoreA
    elif idx == 2:  # third line of input (# of 1-pointers)
        scoreA += apple  # add the number of 1-pointers to scoreA

# get the scores for team Banana
for idx in range(3):
    banana = int(input())
    if idx == 0:  # first line of input (# of 3-pointers)
        scoreB += banana * 3  # multiply the number of 3 pointers by 3 and add it to scoreB
    elif idx == 1:  # second line of input (# of 2-pointers)
        scoreB += banana * 2  # multiply the number of 2 pointers by 2 and add it to scoreB
    elif idx == 2:  # third line of input (# of 1-pointers)
        scoreB += banana  # add the number of 1-pointers to scoreB

# check which score is larger
if scoreA > scoreB:  # scoreA is bigger than scoreB
  print("A")
if scoreA == scoreB:  # scoreA is equal to scoreB
  print("T")
if scoreA < scoreB:  # scoreB is bigger than scoreA
  print("B")