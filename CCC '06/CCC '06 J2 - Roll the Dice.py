'''
Author: Ri Hong
Date AC'd: Mar 23, 2020
Problem: https://dmoj.ca/problem/ccc06j2
'''

#Explanation
'''
Try all the combinations of rolls and cound the number of combinations that add up to 10.
'''
#Code
a = int(input())
b = int(input())
aList = [] #Stores all the possible rolls on the first dice
bList = [] #Stores all the possible rolls on the second dice
#Fill the two lists
for i in range(1, a+1):
  aList.append(i)
for i in range(1, b+1):
  bList.append(i)

#Loop through the lists and see how many combiantions add up to 10
counter = 0
for i in aList:
  for j in bList:
    if i + j == 10:
      counter += 1

#Output
if counter == 1:
  print("There is 1 way to get the sum 10.")
else:
  print("There are {} ways to get the sum 10.".format(counter))
