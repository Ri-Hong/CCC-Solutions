'''
Author: Ri Hong
Date AC'd: June 19, 2020
Problem: https://dmoj.ca/problem/ccc12s5
'''

#Explanation
'''
DFS can be used to find the number of paths it takes to reach the destination while avoiding car coordinates. The grid can be
represented by a 2D array and each cell we be set to -1 initially to represent that it is not yet visited. We traverse through
non-cat coordinates (these can be stored in a list) and cells that are not yet visted. Whenever we reach a cell, if it is 
unvisited, we continue performin DFS and once we get the number of ways we can get to the end from that cell, we update that 
cell's value to that. If the cell is visited, we can use the shortcut value stored at that cell instead of performing DFS again.
'''
#Code
#DFS function. Finds the number of paths to the destination
def findNPath(currentNode):
  #Global variables to store variables that we don't want overrided
  global numPaths
  global grid
  global catCoord, nRows, nColumns

  #If we have reached the goal destination
  if currentNode == (nRows, nColumns):
    numPaths += 1
    return 1
  
  #Rename variables for easy access and readability
  x = currentNode[0]
  y = currentNode[1]

  #If the cell is visited, we can return the shortcut value stored at that cell
  if grid[x][y] !=  -1:
    return grid[x][y]

  sum = 0
  #Move right
  if (x + 1, y) not in catCoord:
    if x + 1 <= nRows:
      sum += findNPath((x + 1, y))

  #Move down
  if (x, y + 1) not in catCoord:
    if y + 1 <= nColumns:
      sum += findNPath((x, y + 1))

  grid[x][y] = sum
  return sum

#-----MAIN-----
#Get input
nRows, nColumns = list(map(int, input().split()))
#Adjust to be 0-indexed
nRows -= 1 
nColumns -= 1
catCoord = [] #A 2D array that represents the grid
#Construct a 2d array
grid = [[-1 for i in range(nColumns + 1)] for i in range(nRows + 1)]

#Get further
numCats = int(input())
for i in range(numCats):
  x, y = input().split()
  catCoord.append((int(x)-1, int(y) - 1))

numPaths = 0

#Find the number of paths starting at (0, 0)
print(findNPath((0, 0)))