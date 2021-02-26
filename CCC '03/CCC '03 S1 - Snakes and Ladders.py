'''
Author: Ri Hong
Date AC'd: Jan. 31, 2020
Problem: https://dmoj.ca/problem/ccc03s1
'''

#Explanation
'''
Have a variable keep track of the current square and add the value of the dice roll to that variable every time. If the current square is a 'special' square,
then set the current square to the square that the 'special' square brings us to.
'''

#Code

specialSquares = { #stores the squares that allow you to travel to other squares (Squares at snake heads or at the bottom of ladders). Index stores the 'from' square and the value stores the 'to' square
  #ladders
  9 : 34,
  40 : 64,
  67 : 86,

  #snakes
  54 : 19,
  90 : 48,
  99 : 77
}

squareNumber = 1 #Stores the square the player is currently on. Initialized to 1
while True: #loop for all the moves
  diceNumber = int(input()) #get the value of the dice roll as an integer
  if diceNumber == 0: #if it is a 0, exit the loop
    print("You Quit!")
    break

  squareNumber += diceNumber #add the dice roll to our square number
  if squareNumber > 100: #handle if the current square is larger than 100
    squareNumber -= diceNumber
  if squareNumber == 100: #handle if the current square is square 100
    print("You are now on square 100")
    print("You Win!")
    break
    
  if squareNumber in specialSquares.keys(): #if the current square is a special square, travel to the appropriate square
    squareNumber = specialSquares[squareNumber]

  print ("You are now on square", squareNumber) #output the current square after every turn

