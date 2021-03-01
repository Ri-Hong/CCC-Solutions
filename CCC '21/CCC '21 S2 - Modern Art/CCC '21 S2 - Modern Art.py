'''
Author: Ri Hong
Date AC'd: Feb 17, 2021
Problem: https://dmoj.ca/problem/ccc21s2
'''

#Explanation
'''
Instead of storing all the 'cells' in a 5000000 by 5000000 2D array, We can just store how many times each row/column is painted using 2 x 5000000 boolean arrays.
True/1 will mean that the row/col has been painted and False/0 will mean that the row/col has NOT been painted. Using booleans to store the state of the row/column
works since painting a single row/col once is equivalent to painting it three times, 5 times, 7 times, etc.
Along the way, we also keep a running total of how many rows and columns are painted.

We can observe that a square will olny become golden if either: the row is painted and the column isn't OR the row is not painted and the column is. (If row and 
column are painted or row and column are both not painted, then the square will remain black) This is similar to the exclusive or operator. 

Thus, the formula for the number of gold squares is: rowsUnpainted * columnsPainted + rowsPainted * columnsUnpainted.
'''

#Code
#get input
height = int(input())
width = int(input())
nChoices = int(input())

#initialize the arrays used to store the states of each row and column. All filled with 0s (black) initially
rowState = [0 for row in range(height)]
colState = [0 for col in range(width)]

#stores the number of rows and col that are painted
nRowPainted = 0
nColPainted = 0

#loop through all instructions and update the rowState and colState arrays
for i in range(nChoices):
  instruction, rcIndex = input().split() #instruction is 'R' or 'C'. rcIndex is the col/row number to be flipped
  rcIndex = int(rcIndex) #cast into int
  rcIndex -= 1 #make the index zero based

  if instruction == 'R':
    rowState[rcIndex] = (rowState[rcIndex] - 1) * -1; #"flip" the row. If it is currently a 1, make it 0 and vice versa
    nRowPainted += rowState[rcIndex] * 2 - 1; #if the new state is true/gold, then we add one to the counter, if it's false/black, we subtract one from the counter

  elif instruction == 'C':
    colState[rcIndex] = (colState[rcIndex] - 1) * -1; #"flip" the row. If it is currently a 1, make it 0 and vice versa
    nColPainted += colState[rcIndex] * 2 - 1; #if the new state is true/gold, then we add one to the counter, if it's false/black, we subtract one from the counter

#calculate nRowUnpainted and nColUnpainted
nRowUnpainted = height - nRowPainted; 
nColUnpainted = width - nColPainted

#calculate number of gold squares
numGoldSquares = nRowPainted * nColUnpainted
numGoldSquares += nColPainted * nRowUnpainted

#output
print(numGoldSquares)