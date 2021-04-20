'''
Author: Ri Hong
Date AC'd: Aug 27, 2020
Problem: https://dmoj.ca/problem/ccc16s2
'''

#Explanation
'''
For the maximum total speed, we want to pair the fastest Dmojistan riders with the slowest Pegland riders, or vice versa. 
For the minimum total speed, we want to pair the slowest Dmojistan riders with the slowest Pegland riders and the fastest
Dmojistan riders with the fastest Pegland riders. This pairing can be done easily through sorted lists.
'''
#Code
#Get input
question = int(input())
citizens = int(input())
dmoj = input().split()
peg = input().split()
for i in range(citizens):
  dmoj[i] = int(dmoj[i])
  peg[i] = int(peg[i])

#Sort the two lists depending on the question
dmoj.sort(reverse = True)
if question == 1:
  peg.sort(reverse = True)
elif question == 2:
  peg.sort()

#Output the pairs
total = 0
for i in range(len(dmoj)):
  total += max(dmoj[i], peg[i])
print(total)