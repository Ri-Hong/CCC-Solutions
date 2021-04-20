'''
Author: Ri Hong
Date AC'd: Jan 13, 2021
Problem: https://dmoj.ca/problem/ccc19j2
'''

#--------Explanation-----------
"""
We want to get the # of lines of message. 
Then for each line, read the two inputs: the number of times to repeat the character, 
and the character itself. Then we print that character out repeatdly that many times
"""

#--------Code-----------

# declare variables
numberOfLines = int(input()) #get the number of lines of input and store it as an integer in the variable: numberOfLines

#Use a for loop to perform an operation for each line of input
for i in range(numberOfLines):
  #Get the entire line of input as a string
  entireLine = input()
  #split the input by spaces. This will return a list. For example, "9 +" will become ["9", "+"]
  splitedInput = entireLine.split()

  #Assign the first element of the list(the number of repetitions) to the variable numberOfRepetitions as an integer
  numberOfRepetitions = int(splitedInput[0])
  #Assign the second element of the list(character to be repeated) to a variable character
  character = splitedInput[1]

  #print out the character for the specified amount of times
  for repetitionTimes in range(numberOfRepetitions):
    #print the character. The end = '' is necessary to keep the output on the same line. By default, the print statement ends with a line break
    print(character, end = '')
  
  #Go onto a new line after each line is finished
  print("")