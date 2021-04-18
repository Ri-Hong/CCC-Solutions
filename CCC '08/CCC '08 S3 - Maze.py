'''
Author: Ri Hong
Date AC'd: Feb 10, 2021
Problem: https://dmoj.ca/problem/ccc08s3
'''

#Explanation
"""
We have a map of the city arranged in a 2x2 grid. The characters in the city will be stored in a 2D array
Our job is to start at the top left of the grid and find the shortest amount of intersections to arrive at 
the bottom right of the grid. The method I chose is BFS(Breadth First Search), where we start at the beginning 
and travel to all cells(a cell is one grid unit) that we can get to in 1 move. From those cells, we then travel 
to all of the NEW cells that we can get to in one additional move. To make sure we don't backtrack to already 
visited cells, we keep track of all the cells thathave been visited and only travel to new cells that have not 
been visited. Along the way, we also keep track and update how many intersections we have passed. We keep 
visiting new cells until either:
1. We reach the bottom left cell, in which case we print out the number of intersections passed.
2. We run out of new cells, in which case we print -1, because that means there is no way to get to the 
bottom right cell.

For more information on 2D arrays: https://www.tutorialspoint.com/python_data_structure/python_2darray.htm
For more information on BFS: https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/tutorial/
"""

#Code
#this function does the bfs
def bfs():
  coordsToProcess = [[0,0]] #stores the coordinates of the cells needed to be processed structure: [[x1, y1], [x2, y2]...]
  visited = [] #stores the coordinates of the visited cells
  nextCoordsToProcess = [] #temorarily stores the coordinates of the next set of cells to be processed
  intersectionCounter = 1 #stores the number of intersections travelled

  #perform the bfs
  while True:
    for coord in coordsToProcess: #loop through each coordinate in coordsToProcess
      row = coord[0] #assign the first coordinate unit the name "row"
      col = coord[1] #assign the first coordinate unit the name "column"

      if not(row >= 0 and row < numRows and col >= 0 and col < numCols): #make sure row and col are within the grid bounds
        continue #if it not in bounds, then we move onto processing the next coordinate
      if grid[row][col] == "*": #make sure the cell character is not a "*"
        continue #if it is a "*", then we move onto processing the next coordinate
      
      visited.append([row, col]) #add the current coordinates to the visited list
      if row == numRows - 1 and col == numCols - 1: #check if destination is reached
        return intersectionCounter #if it is, return the number of intersections

      #now we move onto the handling of each possible intersection character(excluding "*")
      #We have to check if the cells they lead to are already visited and if they're already in the
      #nextCoordsToProcess list. If they are not visited and are not in the nextCoordsToProcess list,
      #then we add it to the nextCoordsToProcess list

      #handle "|" character
      if grid[row][col] == "|":
        #go down one cell
        if [row - 1, col] not in visited and [row - 1, col] not in visited not in nextCoordsToProcess:
          nextCoordsToProcess.append([row - 1, col])
        #go up one cell
        if [row + 1, col] not in visited and [row + 1, col] not in visited not in nextCoordsToProcess:
          nextCoordsToProcess.append([row + 1, col])
      #handle "-" character
      elif grid[row][col] == "-":
        #go left one cell
        if [row, col - 1] not in visited and [row, col - 1] not in nextCoordsToProcess:
          nextCoordsToProcess.append([row, col - 1])
        #go right one cell
        if [row, col + 1] not in visited and [row, col + 1] not in nextCoordsToProcess:
          nextCoordsToProcess.append([row, col + 1])
      #handle "+" character
      elif grid[row][col] == "+":
        #go down one cell
        if [row - 1, col] not in visited and [row - 1, col] not in visited not in nextCoordsToProcess:
          nextCoordsToProcess.append([row - 1, col])
        #go up one cell
        if [row + 1, col] not in visited and [row + 1, col] not in visited not in nextCoordsToProcess:
          nextCoordsToProcess.append([row + 1, col])
        #go left one cell
        if [row, col - 1] not in visited and [row, col - 1] not in nextCoordsToProcess:
          nextCoordsToProcess.append([row, col - 1])
        #go right one cell
        if [row, col + 1] not in visited and [row, col + 1] not in nextCoordsToProcess:
          nextCoordsToProcess.append([row, col + 1])

    if len(nextCoordsToProcess) == 0: #if the nextCoordsToProcess list is empty, then return -1
      return -1
    coordsToProcess = nextCoordsToProcess.copy() #copy the values from nextCoordsToProcess to the coordsToProcess list
    nextCoordsToProcess.clear() #clear the nextCoordsToProcess list
    intersectionCounter += 1 #increment the number of intersections traversed by 1

#---MAIN---
numTestCases = int(input()) #get the number of test cases as an integer
for i in range(numTestCases): #loop through the number of test cases
  grid = [] #a 2D array that stores all the characters/intersection points within the city
  numRows = int(input()) #get the number of rows of the city as an integer
  numCols = int(input()) #get the number of columns of the city as an integer
  
  for j in range(numRows): #loop through the number of rows
    row = list(input()) #get each row as a list of characters instead of a string
    grid.append(row) #add each row into the grid

  #perform bfs
  print(bfs())