'''
Author: Ri Hong
Date AC'd: Jan 10, 2021
Problem: https://dmoj.ca/problem/ccc05j1
'''
#--------Explanation-----------
#First we want to get the sequence of Hs and Vs
#Notice that the operations are commutative in that if you flip the mirror twice horizontally, 
#you end up with the original mirror and the same is true for vertical flips
#This means that we only have to know whether the mirror will end up horizontally the same or 
#flipped compared to the original mirror. We can do this using the modulus (%) operator, which 
#will return a 0 if the number of H's are even (meaning that the mirror will be horizontally 
#identical to the original) or a 1 (meaning that the mirror will be horizontally flipped compared
# to the original). The same is can be done for the vertical flips

#--------Code-----------
flipSequence = input() #get the sequence of flips as a string

numHorizontalFlips = flipSequence.count("H") #count the number of times a horizontal flip occurs and assign it to numHorizontalFlips
numVerticalFlips = flipSequence.count("V") #count the number of times a vertical flip occurs and assign it to numVerticalFlips

#if the number of horizontal flips is even, then we do not need to flip horizontally
if numHorizontalFlips % 2 == 0:
  doHorizontalFlip = False;
else:
  #if the number of horizontal flips is odd, then we do need to flip horizontally
  doHorizontalFlip = True;

#if the number of vertical flips is even, then we do not need to flip vertically
if numVerticalFlips % 2 == 0:
  doVerticalFlip = False;
else:
  #if the number of vertical flips is odd, then we do need to flip vertically
  doVerticalFlip = True;

#print out the correct final orientation based on the whether a vertical or horizontal flip is needed

if doHorizontalFlip == False and doVerticalFlip == False:
    print("1 2")
    print("3 4")
elif doVerticalFlip == True and doHorizontalFlip == False:
    print("2 1")
    print("4 3")
elif doHorizontalFlip == True and doVerticalFlip == False:
    print("3 4")
    print("1 2")
elif doVerticalFlip == True and doHorizontalFlip == True:
    print("4 3")
    print("2 1")