'''
Author: Ri Hong
Date AC'd: Jan 27, 2020
Problem: https://dmoj.ca/problem/ccc14j2
'''

#Explanation
'''
Count the number of each character in the votes string. Then compare the two numbers to see if A or B appears more.
'''
#Code
#Get input
length = int(input())
votes = input()
#Count the number of As and Bs
aCount = votes.count('A')
bCount = votes.count('B')
#Compare and output
if aCount < bCount:
    print("B")
elif aCount == bCount:
    print("Tie")
else:
    print("A")
