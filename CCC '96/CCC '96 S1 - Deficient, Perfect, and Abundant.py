#Explanation
'''
For each number, we want to loop through all the numbers from 1 to the number/2 to get a list of its proper divisors
The reason we only need to check up to number/2 is because the largest divisor of a number that is not itself can only be
the number/2.
PDs of 10: 1, 2, 5 
PDs of 33: 1, 3, 11
PDs of 45: 1, 3, 5, 9, 15
In every case, the largest PD does not exceed the number/2
After we have a list of PDs, we can then get the sum of them and print out the answer accordingly
'''

#Code
numOfCases = int(input()) #get number of test cases as an integer

for j in range(numOfCases): #loop through the number of cases
  listOfPD = [] #for each case we create an empty list for storing PDs
  num = int(input()) #get the number for the test case

  #loop from 1 up to half of the number. +1 beacause for loops check up to but not including the parameter number. 
  # Int() because division results in floating point numbers and parameters for a for loop must be integers
  for i in range(1, int(num / 2 + 1)): 
    if num % i == 0: #check if the number we are on is a factor
      listOfPD.append(i) #if it is, add it to the list

  sumPD = sum(listOfPD) #get the sum of the list

  #do comparisons and print out the answer
  if sumPD == num:
    print("{} is a perfect number.".format(num))
  elif sumPD < num:
    print("{} is a deficient number.".format(num))
  elif sumPD > num:
    print("{} is an abundant number.".format(num))
