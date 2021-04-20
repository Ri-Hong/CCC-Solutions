'''
Author: Ri Hong
Date AC'd: Jan 18, 2020
Problem: https://dmoj.ca/problem/ccc19s2
'''

#----------Explanation----------
"""
For each test case, we want go from 1 to N(the test case number) to look for A and B (the two numbers 
that when added together will equal the test case). Then for each number from 1 to N (let A represent 
this), we want to  check if it is prime. The way we check primeness is we go from every integer starting 
from 2 to S(the square root of A, let D represent every integer from 2-S) and we divide N by D. If D 
divides evenly into A, then we know A is not prime. If all instances of D cannot divide evenly into A, 
then A is prime. After an instance of A being prime is found, we check if A's compliment (let this be B) 
is prime. For every A, there can only be one B, because N = (A + B) / 2, and therefore we can calculate 
a value for B based on that formula. If B is prime, then we have found the two answers for the 
particular test case.
"""

#--------Code--------
#import the math module because we need to square root feature
import math

#Function isPrime takes an integer as a paramater and returns true if the integer is a prime and false if it isn't
def checkPrime(numberToCheck): #numberToCheck is the number we are checking to see if it is a prime
  #assume the number is prime to begin with
  isPrime = True
  #Loop from two to the square root + 1 of the number to check. 
  #math.sqrt() will return a float, with the range() function cannot work with, so we have to make it an integer. int() rounds the float down, we we have to add one to make sure that all the necessary numbers are accounted for
  for currentNum in range(2, int(math.sqrt(numberToCheck))+1):
    #If the current number divides evenly into the number to check, then it isnt a prime
    if numberToCheck % currentNum == 0:
      isPrime = False
      break
  #if all the numbers from 2 to the square root of the number to check cannot divide evenly into it, then the numberToCheck is prime and we return true
  return isPrime


#-----------MAIN-------------
#get the number of test cases as an integer
numberOfTestCases = int(input())
#loop through each test case
for i in range (numberOfTestCases):
  #get the test case
  currentTestCase = int(input())
  #loop from 2 to the test case number
  for firstNumber in range(2, currentTestCase):
    #see if the current number is prime
    if checkPrime(firstNumber) == True:
      #if the first number is prime, then we will set compliment to be the compliment of the first number. i.e. set it to be the number that when added to the first number, their sum will be the test case number
      compliment = currentTestCase * 2 - firstNumber
      #check if the compliment is prime
      if checkPrime(compliment) == True:
        #if it is then we can break out of the for loop and go to the next test case
        print(firstNumber, compliment)
        break