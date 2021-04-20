'''
Author: Ri Hong
Date AC'd: Feb 20, 2020
Problem: https://dmoj.ca/problem/ccc05j1
'''

#Explanation
'''
Loop through both rows of parking spaces at the same time and if there is a 'C' at the same index, then that space is occupied
on both days
'''
#Code
#Get input
n = int(input())
yesterday = input()
today = input()
counter = 0 #Keeps track of the # of spaces that are occupied on both days
for i in range(n):
  #Check if there is a 'C' at the same index
  if "C" in yesterday[i] == today[i]:
    counter += 1
print(counter)
