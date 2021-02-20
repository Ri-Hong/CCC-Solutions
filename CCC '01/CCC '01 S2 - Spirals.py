'''
Author: Ri Hong
Date AC'd: Feb. 19, 2021
'''

#Explanation
'''
First we have to constuct a 2d array of the approiate size. Here are the possible 2d array sizes in increasing order where the first number
represents the number of rows and the second represents the number of columns: (1, 1), (2, 1), (2, 2), (3, 2), (3, 3)... Notice that
the number of rows and number of columns take turns incrementing. What we can do to find out the exact number of rows and columns required is
start at (1, 1), check if the amount of numbers we can fill can fit into a 2d array of that size. If it cannot, increment row first, check again, 
and then increment column. Keep incrementing and checking until we get to a size that can fit all the numbers we need to fit. For example, if we
take the input from Sample Test Case 2, 7 and 12, the amount of numbers we need to fill is 12 - 7 + 1  = 6(+ 1 because we need to include the 12 too).
Here is a list of all the row and col sizes we would need to loop through:
Row + Col    Number of numbers it can hold
(1, 1)       1
(2, 1)       2
(2, 2)       4
(3, 2)       6

So now we know that we need a 2d array of 3 rows and 2 columns. Create a 2d array of the required size and fill it with 0s as a placeholder.
Next we can find out the starting index of the row and column using this formula: ceil(numRows / 2 - 1).
We have to keep track of several things when we are filling in the numbers.
row, col: the indexes of the cell we are currently on (Initialized to the value given by the formula above)
currentNum: the number we are currently filling in (Starts with the lower bounds number given in the input)
direction: the direction we are currently travelling in (Starts as "down")
numSpacesToTravel: the amount of spaces we need to move in one direction (Initialized as 1)

Here is how we always travel. Starting from the first number in the correct position, we go:
D 1
R 1
U 2
L 2
D 3
R 3
U 4
L 4...
Notice that the direction changes once we are done traversing in one direction numSpacesToTravel times. Also notice that
numSpacesToTravel increments only after the Right direction and left direction. We can use these observations to help
us maneuver through the 2d array.

After the 2d array is filled with numbers, we have to print the numbers in the array, which is more complicated than it sounds.
For each value of each cell, we need to check if it is 0. If it is, that means it should not be printed and we must print spaces to
take up that cell instead. If it is not a 0, we need to check if it is a single digit number. If it is, we need to add a space before we
print the number since single digit numbers take one less space than 2 digit numbers. Finally, if it is not a 0 or a single digit number, 
it must be a 2 digit number, so we can just print it. Take note that when a number is printed, you have to add a end = " " in the print statement
as well. This ensures that the output does not go onto a new line and adds a space between that number and the next. Also, make sure that
at the end of every row you print() to go onto a new line for a new row.
'''

#Code
from math import ceil #import the ceil function from the math library

#this function will print the completed grid at the end
def printGrid(grid): #takes in a 2d array as a parameter
  for row in range(len(grid)): 
    for col in range(len(grid[row])): #loop through each element in the 2d array
      if grid[row][col] == 0: #if the value is 0
        print("  ", end = " ") #then omit it and print 3 spaces instead
      elif grid[row][col] < 10: #if the value is a single digit number
        print("", grid[row][col], end = " ") #add an extra space to the front of the number
      else: #if the value is a 2 digit number
        print(grid[row][col], end = " ") #print it ending with a space
    print() #go onto a new line after each row

#---MAIN---
lowerBounds = int(input()) #get the lower bounds as an integer
upperBounds = int(input()) #get the upper bounds as an integer

numNumbersInGrid = upperBounds - lowerBounds + 1 #calculate the number that will be in the final grid

#calculate the size of the 2d array we will need
numRows = 1 #this stores the number of rows we will have the 2d array. Initialized to 1
numCols = 1 #this stores the number of columns we will have the 2d array. Initialized to 1
while True: 
  if numNumbersInGrid <= numRows * numCols: #if the rows and columns we currently have can fit all the numbers required
    break #exit the loop
  numRows += 1 #if the size of the 2d array is not large enough, increment the number of rows by one for the next iteration of the for loop

  if numNumbersInGrid <= numRows * numCols: #if the rows and columns we currently have can fit all the numbers required
    break #exit the loop
  numCols += 1 #if the size of the 2d array is not large enough, increment the number of columns by one for the next iteration of the for loop

#create the 2d array of the approiate size
grid = [[0 for col in range(numCols)] for row in range(numRows)]

#fill the numbers into the 2d array
row = ceil(numRows / 2 - 1) #calculate the starting row
col = ceil(numCols / 2 - 1) #calculate the starting column
currentNum = lowerBounds #initialize the current number to the first number (the lower bounds number)
grid[row][col] = currentNum #set the first cell to the current number
direction = "down" #initialize the direction to down
numSpacesToTravel = 1 #initialie the number of spaces we need to travel in one direction to 1

while currentNum <= upperBounds: #keep looping until we fill the last number (uppoer bounds)
  for i in range(numSpacesToTravel): #numSpacesToTravel stores the amount of spaces we move in one direction. Loop through it
    currentNum += 1 #add one to the current number we are on
    if currentNum > upperBounds: #check if the current number is greater than the upper bounds
      break #if it is, exit the for loop and the while loop
    #process directions
    if direction == "down": #if the direction is down
      row += 1 #increment the row index by 1
    elif direction == "right": #if the direction is right
      col += 1 #increment the column index by 1
    elif direction == "up": #if the direction is up
      row -= 1 #decrement the row index by 1
    elif direction == "left": #if the direction is left
      col -= 1 #decrement the column index by 1
    grid[row][col] = currentNum #set the current cell we are on to the current number

  #process direction changes after we are done moving in one particular direction for numSpacesToTravel cells
  if direction == "down": #if the direction was down, change it to right
    direction = "right"
  elif direction == "right": #if the direction was right, change it to up
    direction = "up"
    numSpacesToTravel += 1 #also add one to the number of spaces to travel
  elif direction == "up": #if the direction was up, change it to left
    direction = "left"
  elif direction == "left": #if the direction was left, change it to down
    direction = "down"
    numSpacesToTravel += 1 #also add one to the number of spaces to travel

#print the final layout of the numbers
printGrid(grid)