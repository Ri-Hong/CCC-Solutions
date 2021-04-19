'''
Author: Ri Hong
Date AC'd: Jan 30, 2020
Problem: https://dmoj.ca/problem/ccc11s2
'''

#Explanation
'''
Get the student response and the answer key and put them in their own list. Then loop through both lists at the same time
and check how many elements match.
'''
#Code
N = int(input())
studentAnswer = []
correctAnswer = []
#Construct the lists
for i in range(N):
  studentAnswer.append(input())
for i in range(N):
  correctAnswer.append(input())

correctCounter = 0 #Stores the number of questions the student got correct
#Loop through the lists
for i in range(N):
  if studentAnswer[i] == correctAnswer[i]: #Check if the student's answer matches the answer key's answer
    correctCounter += 1 #If it does, increment the counter by 1
print(correctCounter)
