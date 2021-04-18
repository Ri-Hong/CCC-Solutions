'''
Author: Ri Hong
Date AC'd: July 20, 2020
Problem: https://dmoj.ca/problem/ccc07s4
'''

#Explanation
'''
Slide paths can be stored in a dictionary with the starting point as the key and the destination points in a list as the value.
To improve the time complexity and not TLE, we can have another dictionary that stores the # of paths that lead to the bottom 
from a specific point, where the starting point is the key and the # of paths is the value. We can continuously update this 
dictionary every time we return from a path. Before we go down a path, we check to see if the point is in the shortcuts 
dictionary and if it is, we use that value instead of DFSing down the path.
'''

#Code
gSlideDict = {} #Stores the slide paths
gShortCuts = {} #Stores the shortcuts

#A recursive DFS function that returns the number of paths there are to reach the bottom
def findPaths(dest, currNode):
  if currNode == dest: #Destination found
    return 1

  if currNode not in gSlideDict: #If the current point does not exist as a key in the slide dict
    return 0
  
  if currNode in gShortCuts: #If there is a shortcut
    return gShortCuts[currNode]

  paths = 0
  for i in gSlideDict[currNode]: #Loop through al the connecting nodes
    paths += findPaths(dest, i) #Find the # of paths and add it to the total
    gShortCuts[currNode] = paths #Update the shortcuts dictionary
  return paths


#----------------main---------------------
#Get input and construct gSlideDict
gDestination = int(input())
while True:
  pair = input()
  a, b = pair.split()
  a = int(a)
  b = int(b)
  if a == 0 and b == 0:
    break
  if a in gSlideDict:
    gSlideDict[a].append(b)
  else:
    gSlideDict[a] = [b]

#Run DFS and print output
numPaths = findPaths(gDestination, 1)
print(numPaths)
