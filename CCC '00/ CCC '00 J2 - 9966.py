'''
Author: Ri Hong
Date AC'd: Jan. 4, 2020
'''
#Explanation
'''
*Note 9966able means being able to look the same after being flipped upside down
We want to loop through each number from the lower interval up to and including the top interval. For each number, we have to check if it meets the
9966 requirements of looking the same after it is rotated 180 degrees. We have 5 special number we need to look out for. The numbers 0, 1, 8 when flipped
upside down are identical to themselves. The number 6 when flipped upside becomes a 9 and vice versa. Now we can develop our algorithm. 
Suppose we have a number N of length L. If the number contains numbers other than 0, 1, 8, 6 or 9, then it can be automatically ruled out from being 9966able.
Now that N has only digits of 0, 1, 8, 6 or 9, we can check if it is 9966able. For any digit, if it is a 0, 1 or 8, the digit of the same index counting from the
end of N must also be the same digit. For example, if the first digit is 1, then the last digit must also be 1. If the third digit is 8, then the third last digit
must also be an 8 for N to be 9966able. Here are more examples:
(_ denotes any other number 0, 1, 8, 6 or 9) 
1 _ _ _ 1 is ok. 
_ 8 _ _ 8 _ is ok 
_ 8 _ _ 1 _ is not ok 
_ 8 _ 0 _ is not ok

For any digit, if it is a 6, the the digit of the same index counting from the end must be a 9. The inverse is true: if it is a 9, the the digit of the same 
index counting from the end must be a 6. For example, if the second digit is a 6, then the second last digit must be a 9. If the 5th digit is a 9, then the fith
last digit must be a 6. More examples follow:
(_ denotes any other number 0, 1, 8, 6 or 9) 
6 _ _ 9 is ok. 
_ _ 9 6 _ _ is ok 
_ 6 _ _ 6 _ is not ok 
_ 6 9 _ _ is not ok

'''
#Code
from math import ceil #import the ceil function from the math library. The ceil function rounds a float up to the nearest integer

#get input
startInterval = int(input()) #get the lower interval as an integer
endInterval = int(input()) #get the higher interval as an integer

flippableCounter = 0 #stores how many numbers are 9966able


for currentNum in range(startInterval, endInterval + 1): #loops through all numbers in the interval range. Ensure that we loop up to and including the top interval
  currentNum = str(currentNum) #convert the number to a string to make indexing easier
  flippable = True #flippable stores whether the number is 9966able. Set to true initially
  #loop through all the indexes from 0 up to the half of the length of the number rounded up to the nearest integer
  #only loop up to len(currentNum)/2 because we are simultaneously checking the opposite end of the number every time we check a digit
  #ceil because in the case of number with an odd length, we want to check up and including to the middle digit. This also circumvents the need to handle 1 digit numbers seperately
  for index in range(ceil(len(currentNum)/2)): 
    digit = currentNum[index] #name the value of the current index of the number
    oppositeDigit = currentNum[len(currentNum) - index - 1] #name the value of the current index of the number counting from the end of the number. E.g with a number of length 5, when digit = 0, oppositeDigit = 4, when digit = 1, oppositeDigit = 3, etc
    if digit != "0" and digit != "1" and digit != "8" and digit != "6" and digit != "9": #check if the digit is a 0, 1, 8, 6 or 9
      flippable = False #if it isn't, set flippable to false 
      break #exit the loop for the individual digits
    elif digit == "0" or digit == "1" or digit == "8": #check if the digit is a 0, 1 or 8
      if digit != oppositeDigit: #check if the digit is equivalent to the opposite digit
        flippable = False #if it isn't, set flippable to false 
        break #exit the loop for the individual digits
    elif digit == "6" and oppositeDigit != "9": #check if the digit is a 6 and if it is, check if the opposite digit is a 9. If the opposite digit is not a 9:
      flippable = False #set flippable to false
      break #exit the loop for the individual digits
    elif digit == "9" and oppositeDigit != "6": #check if the digit is a 9 and if it is, check if the opposite digit is a 6. If the opposite digit is not a 6:
      flippable = False #set flippable to false
      break #exit the loop for the individual digits

  if flippable: #check if the number is 9966able
    flippableCounter += 1 #if it is, add one to the # of numbers that can be flipped

#output
print(flippableCounter) #print out the # of numbers that can be flipped