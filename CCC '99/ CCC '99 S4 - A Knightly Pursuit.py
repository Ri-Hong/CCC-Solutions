'''
Author: Ri Hong
Date AC'd: June 27, 2020
'''
#Explanation
'''
This problem has two quirks we need to look out for before we even start solving the problem. 
1) The starting positions of the knight and the pawn are in real-world coordinates, not programming indexes.
Meaning, if we have a 3x3 grid, the first row would be index 0, second row wold be index 1 and third row would
be index 2. However, In the real world, if you wanted to reference the top left most cell, you would say the cell
on row 1 and column 1 not row 0 and column 0. So for example, if the test case was:
1
3
3
1
1
2
3
pr (starting row of the pawn) is 1 and pc (starting column of the pawn) is also 1. But in the 2d array, you would want the
starting cell to be array_name[0][0]

2) The row and column number system is also not the same as programming indexes. In programming, if we have a 2d array, we count
from left to right and top to bottom. Heres the grid coordinates as indexes:
(0,0) (0,1) (0,2)
(1,0) (1,1) (1,2)
(2,0) (2,1) (2,2)
However, the problem specifies that Row 1 is at the bottom of the board and Row r is at the top of the board. Column 1 is at the 
left and column c is at the right. Their number system is as follows:
(3,1) (3,2) (3,3)
(2,1) (2,2) (2,3)
(1,1) (1,2) (1,3)
Converting to programming indexes gives us:
(2,0) (2,1) (2,2)
(1,0) (1,1) (1,2)
(0,0) (0,1) (0,2)

So basiclly, we have to invert the row numbers and subtract each coordinate the problem gives us by one. Doing so will
allow us to get the identical board and starting positions indexed in programming indexes. 

Now let's move onto the problem
We construct a 2D array called "board" with the exact dimensions of the chessboard. All cells of board are initially
set to 10000. Each cell of board will store the number of moves it will take the knight to reach that cell. The knight's starting
cell will be set to 0. We can use BFS to fill the cells for the knight
In the case of:
1
3
3
1
1
2
3
Initially, the board will be
10000 10000 10000
10000 10000 0
10000 10000 10000 
because the knight starts on row 2 col 3 (board[1][2]). Then the board will be
1 10000 10000
10000 10000 0
1 10000 10000 
because the knight can move 1 space up/down and two spaces left. Next,
1 2 10000
10000 10000 0
1 2 10000 
The knight at (0, 0) moves to (2, 1) and the knight at (2, 0) moves to (0, 1). Next,
1 2 3
10000 10000 0
1 2 3 
The knight at (0, 1) moves to (2, 2) and the knight at (2, 1) moves to (0, 2). Finally,
1 2 3
4 10000 0
1 2 3 
Either the knight at (2, 2) and the knight at (0, 2) moves to (1, 0). 
Note that it is impossible to get to (1, 1) so the value at (1, 1) remains as 10000.

Now that we have a 2d array with the knight's movements, we can deal with the pawn's movements. We check
each cell above the pawn and along the way, we keep track of how many cells the pawn has moved. If the pawn
can reach a cell on the same number of moves as the knight, then the knight wins. If the knight can reach a cell
that in n moves and the pawn reaches the cell below it in n moves, then a stalemate is achieved. If there is a win, 
then then we dont have to look at the stalemate moves or losses. If there is no win, then we check if there is a stalemate.
If there is no win or no stalemate, then we process a loss.

There is a problem we need to solve with this method. So far we only assume that the knight cannot travel back to visited cells.
Consider this testcase: let K represent the starting cell of the knight and P the starting cell of the pawn and . empty cells
. . 
. . 
. . 
K . 
. P 
After we handle the knight travelling, board would look like:
10000 10000 
10000 1
10000 10000
0 10000
10000 10000 
or
. .
. 1
. .
0 . 
. P 
Using our current algorithm, it would determine that it would be impossible for the knight to win. However, the knight can win if it:
starts on (3, 0)
move to (1, 1)
move back to (3, 0)
move back to (1, 1) to capture the pawn

As you can see, we need handle the knight being able to travel back to visited cells. This is how we can account for this:
1) Check if it is even possible for the knight to reach our current cell before the pawn. Do this by checking if our current cell on 
the board holds a value that is greater than the number of moves it takes the pawn to get there. If its not, it means that the pawn 
arrives earlier than the knight and thus we do not need to check further. If it is, it means that the knight will arrive at that cell 
before the pawn. Next we check if the knight can arrive at the cell on the same turn as the pawn. We can do this by using the mod function.
we mod the value of our current cell by 2 and do the same with the number of moves it takes the pawn to reach the same cell. if the two modded
values are the same, then it means the knight can reach that specific cell on the same turn as the pawn by cycling to already visited cells. 
Consider the previous testcase.
. .
. .
. .
K . 
. P 
With the knight starting on cell (3, 0), it can reach cell (1, 1) on turns: 1, 3, 5, 7..... We can observe that the knight can reach that cell on every odd turn,
so as long as the pawn reaches that cell on any odd turn, the pawn will be captured. The pawn can arrive on turn 1, 3, 9, 213712893123121, it doesn't matter, as long
as it is odd. The same is true with even turns. If a knight can arrive on a cell on an even turn before the pawn, the pawn will be captured if it arrives on an even turn.

'''

#Code
#get input
numGames = int(input()) #get the number of games as an integer
for i in range(numGames): #loop through each game
  r = int(input()) #get the number of rows of the chessboard
  c = int(input()) #get the number of columns of the chessboard
  pr = r - int(input()) #get the starting row of the pawn but adjust it to be the programming grid
  pc = int(input()) - 1 #get the starting column of the pawn but adjust it to be the programming grid
  kr = r - int(input()) #get the starting row of the knight but adjust it to be the programming grid
  kc = int(input()) - 1 #get the starting column of the knight but adjust it to be the programming grid
  win = 0 #this stores how many moves it takes the knight to capture the pawn. If it's 0, it means the knight has not captured the pawn
  stalemate = 10000 #if this value is 10000 (the initial starting value), then that means there is no stalemate. Otherwise, this will store the number of knight moves it takes to stalemate
  board = [[10000 for x in range(c)] for x in range(r)] #create a 2d array with r rows and c columns and fill each cell with 10000
  board[kr][kc] = 0 #initialize the starting cell of the knight to be 0
  queue = [[kr,kc]] #this list stores the list of knight moves that need to be processed on a specific turn

  #fill board with knight positions using BFS
  while queue: #while there are still values in the queue
    row, col = queue.pop(0) #take out the first set out coordinates and assign them to row and col. row will be the index for rows and col will be the index for cols
    valueOfCurrSquare = board[row][col] #get the value of the cell and assign it to valueOfCurrSquare

    #now we process each possible movement of the knight starting from row, col
    #up 1 left 2
    if row > 0 and col > 1: #make sure there is enough room to go up 1 left 2
      if board[row - 1][col - 2] > valueOfCurrSquare + 1: #if the value of the cell of up 1 left 2 is greater than than the number of moves it will take us to get there from our current position (valueOfCurrSquare + 1)
        board[row - 1][col - 2] = valueOfCurrSquare + 1 #update the cell at up 1 left 2 to valueOfCurrSquare + 1
        queue.append([row - 1, col - 2]) #add the coordinates at up 1 left 2 to the queue
    #do the same checks for the other possible positions the knight can move to
    #up 2 left 1
    if row > 1 and col > 0:
      if board[row - 2][col - 1] > valueOfCurrSquare + 1:
        board[row - 2][col - 1] = valueOfCurrSquare + 1
        queue.append([row - 2, col - 1])
    #up 1 right 2
    if row > 0 and col < c - 2: #remember, c is the number of columns in the chessboard
      if board[row - 1][col + 2] > valueOfCurrSquare + 1:
        board[row - 1][col + 2] = valueOfCurrSquare + 1
        queue.append([row - 1, col + 2])
    #up 2 right 1
    if row > 1 and col < c - 1:
      if board[row - 2][col + 1] > valueOfCurrSquare + 1:
        board[row - 2][col + 1] = valueOfCurrSquare + 1
        queue.append([row - 2, col + 1])
    #down 1 left 2
    if row < r - 1 and col > 1: #remember, r is the number of rows in the chessboard
      if board[row + 1][col - 2] > valueOfCurrSquare + 1:
        board[row + 1][col - 2] = valueOfCurrSquare + 1
        queue.append([row + 1, col - 2])
    #down 2 left 1
    if row < r - 2 and col > 0:
      if board[row + 2][col - 1] > valueOfCurrSquare + 1:
        board[row + 2][col - 1] = valueOfCurrSquare + 1
        queue.append([row + 1, col - 1])
    #down 1 right 2
    if row < r - 1 and col < c - 2:
      if board[row + 1][col + 2] > valueOfCurrSquare + 1:
        board[row + 1][col + 2] = valueOfCurrSquare + 1
        queue.append([row + 1,col + 2])
    #down 2 right 1
    if row < r - 2 and col < c - 1:
      if board[row + 2][col + 1] > valueOfCurrSquare + 1:
        board[row + 2][col + 1] = valueOfCurrSquare + 1
        queue.append([row + 2,col + 1])

  #process the pawn movements pr is the pawn's starting row, pc is the pawn's starting column
  pawnMoveCounter = 0 #stores the number of moves the pawn has made
  for row in range(pr, 0, -1): #loop through all the rows above the pawn's starting row in reverse. E.g. if the pawn started on row 4, we want to loop through 4, 3, 2, 1, 0
    if board[row][pc] == pawnMoveCounter: #if the pawn and knight arrive to the same cell at on the same move
      win = pawnMoveCounter #knight wins. Assign the number of moves it takes to win to the variable win
      break #exit the loop
    elif board[row - 1][pc] == pawnMoveCounter: #if the knight lands on the cell ahead of the pawn on the same move (stalemate)
      if pawnMoveCounter < stalemate: #if the number of moves it takes to stalemate is less than the stored number of moves to stalemate
        stalemate = pawnMoveCounter #set the number of moves it will take to achieve a stalemate to the variable stalemate
    #deal with cycles
    elif pawnMoveCounter > 1: #only check for cycles if the pawn moves is greater than 1. This is because there is no way a knight can cycle when a pawn has only moved once or less
      if board[row][pc] < pawnMoveCounter: #check if the knight can arrive earlier than the pawn. Aka check if the value of the cell on board is less than the # of moves the pawn has taken
        if board[row][pc] % 2 == pawnMoveCounter % 2: #check if the knight and the pawn can arrive at the same cell in an odd or even number of moves. If they are both odd or both even:
          win = pawnMoveCounter #the knight wins. Store the number of moves it took to win in the variable "win"
          break #no need to check further. Exit the loop
        elif board[row - 1][pc] % 2 == pawnMoveCounter % 2: #check if the knight can arrive at the cell above the pawn in an odd or even number of moves. If both arrive in an odd or even number of moves:
          if pawnMoveCounter < stalemate: #if the number of moves it takes to stalemate is less than the stored number of moves to stalemate
            stalemate = pawnMoveCounter #set the number of moves it will take to achieve a stalemate to the variable stalemate

    #increment the number of pawn moves before going onto the next iteration of the loop
    pawnMoveCounter += 1

  #handle output
  if win: #if win has a value other than 0 (the initial value), that means a win has been achieved
    print ("Win in", win, "knight move(s).") #print how many moves it took to win (value that's stored in the variable "win")
  elif stalemate != 10000: #if stalemate has a value other than 10000, that means a stalemate has been achieved
    print ("Stalemate in", stalemate, "knight move(s).") #print the number of moves it took to stalemate (value that's stored in stalemate)
  else: #if there is no win or no stalemate, then it must be a loss
    print ("Loss in", r - (r - pr) - 1, "knight move(s).") #print the number of rows the pawn has to travel to get to the top row. (aka # moves it took to produce a loss)