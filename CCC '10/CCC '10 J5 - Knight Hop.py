'''
Author: Ri Hong
Date AC'd: Apr 27, 2020
Problem: https://dmoj.ca/problem/ccc10j5
'''

#Explanation
'''
Construct a 2D array to represent the grid. Each element in the grid represents the shortest distance it would take for 
the knight to reach that square from the starting position, so initially, it will all be a very large value such as 100
Perform DFS to and each time we we land on a square, we update the square's value if we the number of steps we took is 
less than the value at that square.
'''
#Code
#Get input
i = input()
startingCol, startingRow = i.split()
j = input()
endingCol, endingRow = j.split()

#Convert to int
startingCol = int(startingCol)
startingRow = int(startingRow)
endingCol = int(endingCol)
endingRow = int(endingRow)

count = 0 #Stores the total # of moves made currently

infinite = 100 #A constant value, 100 because it will not take 100 steps to reach any destination from any starting point

shortestDist = [] #2D array that represents the board
#Fill up the 2D array
for c in range(8):
  temp = []
  for r in range(8):
    temp.append(infinite)
  shortestDist.append(temp)

#This function returns a list of a set of coordinates the knight is able to travel to from a given position. It also takes
#in prevCoord so that the knight does not move back and forth between two points
def getNextCoordList (currCol, currRow, prevCoord):
  nextCoordList = []
  if currCol + 1 <=7 and currRow - 2 >= 0:
    nextCoordList.append([currCol + 1, currRow - 2])
  if currCol + 2 <=7 and currRow - 1 >= 0:
    nextCoordList.append([currCol + 2, currRow - 1])
  if currCol + 2 <=7 and currRow + 1 <=7:
    nextCoordList.append([currCol + 2, currRow + 1])
  if currCol + 1 <=7 and currRow + 2 <=7:
    nextCoordList.append([currCol + 1, currRow + 2])
  if currCol - 1 >= 0 and currRow + 2 <= 7:
    nextCoordList.append([currCol - 1, currRow + 2])
  if currCol - 2 >= 0 and currRow + 1 <= 7:
    nextCoordList.append([currCol - 2, currRow + 1])
  if currCol - 2 >= 0 and currRow - 1 >= 0:
    nextCoordList.append([currCol - 2, currRow - 1])
  if currCol - 1 >= 0 and currRow - 2 >= 0:
    nextCoordList.append([currCol - 1, currRow - 2])
  
  if prevCoord != [-1,-1]:
    nextCoordList.remove(prevCoord)

  return nextCoordList

#--------------------------------------------------------
def shortestPath (prevCoord, currCoord, dst, currDist):
  global count
  count += 1 #Increment the move/step counter by 1

  if currCoord == dst: #If the destination is reached
    return 0

  #if the current square isn't 100 or 101(square already found minDist), then we return the current value
  if shortestDist[currCoord[0]][currCoord[1]] == infinite + 1:
    return shortestDist[currCoord[0]][currCoord[1]]    
  if shortestDist[currCoord[0]][currCoord[1]] != infinite:
    return shortestDist[currCoord[0]][currCoord[1]]

  shortestDist[currCoord[0]][currCoord[1]] = infinite + 1
  
  nextCoordList = getNextCoordList (currCoord[0], currCoord[1], prevCoord)
  dist = infinite
  for nextCoord in nextCoordList:
    #only check next square if it is unvisited(infinite)
    #if shortestDist[nextCoord[0]][nextCoord[1]] == infinite:
    dist = shortestPath (currCoord, nextCoord, dst, currDist + 1)+1

    if dist < shortestDist[currCoord[0]][currCoord[1]]:
      shortestDist[currCoord[0]][currCoord[1]] = dist

  return shortestDist[currCoord[0]][currCoord[1]]
#--------------------------------------------------------

d = shortestPath ([-1, -1], [startingCol-1, startingRow-1], [endingCol-1, endingRow-1], 0)
print(d)
