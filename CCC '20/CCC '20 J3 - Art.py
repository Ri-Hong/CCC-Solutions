'''
Author: Ri Hong
Date AC'd: Aug 27, 2020
Problem: https://dmoj.ca/problem/ccc20j3
'''

#Explanation
'''
Basically, we want to get the minimum x and y coordinates for the bottom left corner and the maximum x and y coordinates for 
the top right corner. Note that the frame needs to be not covering the edge so we need to subtract 1 from the x and y coordinates
for the bottom left corner and add 1 to the x and y coordinates on the top right corner. We can easily get the minimum and
maximum x and y coordinates by putting all the x coordinates and all the y coordinates into two seperate lists and use the python
min() and max() function.
'''
#Code
amount = int(input())
#Lists to store the x and y coordinates.
listx = []
listy = []
#Get coordinates and add them to their respective lists
for i in range(amount):
  x, y = input().split(",")
  x = int(x)
  y = int(y)
  listx.append(x)
  listy.append(y)

#Output
print(str(min(listx) - 1) + "," + str(min(listy) - 1)) #Bottom left corner
print(str(max(listx) + 1) + "," + str(max(listy) + 1)) #Top right corner
