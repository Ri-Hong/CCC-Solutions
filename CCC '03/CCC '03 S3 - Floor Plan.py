'''
Author: Ri Hong
Date AC'd: May 2, 2020
Problem: https://dmoj.ca/problem/ccc03s3
'''

#Explanation
'''
First we construct a 2D array with 'I' representing walls and '.' representing empty room spaces. We then loop through every cell of the 2D array and check if it is an empty room space.

If it is, we start a DFS on that cell to find the size of the entire room. The DFS will look at cells above, below, to the right, and to the left of the current cell.
If even one of them is an empty space, then the function gets called again for that space and turn the current cell into a wall to eliminate infinite loops. The DFS has a 
variable that will keep track of the room size as it goes. The DFS will keep calling itself until it is completely surrounded by walls, after which it returns the room size 
back to whoever called it.

After obtaining a list of room sizes, it is now simply a matter of looping through them from greatest to least to find out how many can be tiled.
'''

#Code
#A recursive function. Fills a room with "I"s using DFS and returns the area of the room
def findRoomSize(floorPlan, row, col, roomSize):
  if floorPlan[row-1][col] == "I" and floorPlan[row][col+1] == "I" and floorPlan[row+1][col] == "I" and floorPlan[row][col-1] == "I": #if the current cell is surrounded by walls
    floorPlan[row][col] = 'I'
    return roomSize

  floorPlan[row][col] = "I" #set the current cell to a wall so that we don't traverse back to this cell again

  #these if statements check if the surrounding cells (up, down, left, right) are occupied by walls. If not, it will recursively call the function again for that cell while incrementing room size by 1
  if floorPlan[row][col + 1] == '.': #check right cell
    roomSize = findRoomSize(floorPlan, row, col + 1, roomSize + 1)
  if floorPlan[row + 1][col] == '.': #check bottom cell
    roomSize = findRoomSize(floorPlan, row + 1, col, roomSize + 1)
  if floorPlan[row][col - 1] == '.': #check left cell
    roomSize = findRoomSize(floorPlan, row, col - 1, roomSize + 1)
  if floorPlan[row - 1][col] == '.': #check up cell
    roomSize = findRoomSize(floorPlan, row - 1, col, roomSize + 1)

  return roomSize

#--------------------main-------------------
availableFlooring = int(input())
numRows = int(input()) 
numCols = int(input())

floorPlan = [['I']*(numCols+2)] #pad the top with walls

#loop through each row and add the row as a list to the floorplan list
for i in range(numRows):
  row = ['I']
  rowString = input()
  for character in rowString:
    row.append(character)
  row.append('I')
  floorPlan.append(row)

floorPlan.append(['I']*(numCols+2)) #pad the bottom with walls

roomSizeList = [] #stores a list of the room sizes
#loop through each cell of the 2D array
for row in range(len(floorPlan)):
  for col in range(len(floorPlan[row])):
    #if the current cell is a room space, change it to a wall and start a DFS on that space to find the size of the room
    if floorPlan[row][col] == '.':
      floorPlan[row][col] == 'I'
      roomSize = findRoomSize(floorPlan, row, col, 1)
      roomSizeList.append(roomSize) 

roomSizeList.sort(reverse = True) #sort the room size list from greatest to least
roomsCovered = 0 #stores the number of complete rooms that can have flooring installed
#loop through the room size list and figure out how many rooms can have flooring installed with the available flooring
for i in roomSizeList: 
  if i <= availableFlooring:
    availableFlooring -= i
    roomsCovered += 1
  else:
    break


if roomsCovered == 1: #if there is only one room covered, don't print an s on the room
  print("{} room, {} square metre(s) left over".format(roomsCovered, availableFlooring))
else:
  print("{} rooms, {} square metre(s) left over".format(roomsCovered, availableFlooring))